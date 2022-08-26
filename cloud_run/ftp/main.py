"""
main.py module
This Module is the main python module which will be triggered by Cloud Run,
this module is responsible read the FTP files fom given GCS
bucket and ingest the data in BigQuery.
"""
import sys
import logging
from flask import Flask, request
import pandas as pd
from io import StringIO

from common import constant
from common.utils import bq_utils, \
  storage_util, job_audit_utils

app = Flask(__name__)


def fetch_filelist_from_bucket(bucket_name):
  """
    This method will fetch list of
    files from provided ftp bucket.
    :return list of FTP files
  """
  try:
    bucket = \
      storage_util.get_storage_bucket(constant.PROJECT_ID, bucket_name)
    files = bucket.list_blobs(delimiter="/")
    filelist = [file.name for file in files]
    filelist = list(filter(lambda x: ".NY1" in x, filelist))
    logging.info("List of files present in bucket is %s", str(filelist))
    return filelist
  except Exception as exception:
    logging.error(
      "An exception occurred  in [fetch_filelist_from_bucket]"
    )
    logging.error("Exception occurred due to %s", str(exception))
    raise exception


def read_csv_and_ingest_into_bq(
        data, table_name, file, schema,
        batch_timestamp, record_date):
  """
    This method will read comma separated values using pandas and
    stored them into BigQuery,
    Also this method inserts the data into audit table.
    :param data: data from .NY file
    :param table_name: table name where data need to be stored.
    :param file: Name of the .NY file which contains data.
    :param batch_timestamp: Timestamp when the pipeline started.
    :param record_date: Date where data ingested to BigQuery.
    :param schema: schema of the table in
    which data needs to be inserted.
  """

  try:
    new_data = StringIO(data)
    df = \
      pd.read_csv(new_data, sep=",", skiprows=0,
                  engine="python", names=schema)
    df["ingestion_timestamp"] = batch_timestamp
    df["file_name"] = file
    df["record_date"] = record_date

    if df["poc"].isnull().values.any():
      logging.info("Null values found for poc")
      raise ValueError(f"Got null values for "
                       f"the poc for file = {str(file)}")

    bq_utils.ingest_dataframe_to_bq(data=df, bq_table_name=table_name)
    logging.info("Data ingested successfully for file %s", str(file))
    job_audit_utils.get_insert_audit_rows(
      data_source="FTP",
      data_source_last_edit_date=None,
      task_name="aqs_ftp_bq_raw_ingestion",
      source_query_url=None,
      batch_timestamp=batch_timestamp,
      layer_name=file,
      destination=table_name,
      count=len(df.index),
      status="SUCCESS")
    return "Success."

  except Exception as exception:
    logging.error("An exception occurred  in "
                  "[read_csv_and_ingest_into_bq]")
    logging.error("Exception occurred due to %s", str(exception))
    sys.exc_info()
    job_audit_utils.get_insert_audit_rows(
      data_source="FTP",
      task_name="aqs_ftp_bq_raw_ingestion",
      source_query_url=None,
      batch_timestamp=batch_timestamp,
      layer_name=file,
      message=(f"Exception occurred due to {str(exception)}" + " " + str(
        sys.exc_info())),
      status="FAILED")
    raise exception


@app.route("/gcs_to_bq", methods=["GET"])
def read_ftp_data_from_gcs_and_ingest_into_bq():
  """
    This method will read the .NY data from GCS Bucket and
    stored it into BigQuery This endpoint/functions expects
    bucket_name, table_name,batch_timestamp and
    number of ftp_files_to_process.
  """
  file = None
  try:
    bucket_name = request.args.get("bucket_name")
    table_name = request.args.get("table_name")
    ftp_files_to_process = (request.args.get
                            ("ftp_files_to_process"))
    batch_timestamp = request.args.get("batch_timestamp")
    if batch_timestamp is None \
            or batch_timestamp == "None" \
            or batch_timestamp == "" \
            or bucket_name is None \
            or bucket_name == "None" \
            or bucket_name == "" \
            or table_name is None \
            or table_name == "None" \
            or table_name == "":
      raise ValueError(
        "the supplied values of query parameters "
        "is not well formatted or none,"
        "the received value of , batch_timestamp "
        f"is {batch_timestamp}, bucket_name "
        f"is {bucket_name}, table_name "
        f"is {table_name} and ftp_files_to_process "
        f"is {ftp_files_to_process}"
      )

    elif ftp_files_to_process is None \
            or ftp_files_to_process == "None" \
            or ftp_files_to_process == "" \
            or int(ftp_files_to_process) > 40:
      ftp_files_to_process = 40

    batch_timestamp = bq_utils.format_batch_timestamp(
      batch_timestamp=batch_timestamp)
    record_date = batch_timestamp.date()

    filelist = fetch_filelist_from_bucket(bucket_name)
    filelist = filelist[:int(ftp_files_to_process)]
    schema = bq_utils.fetch_bq_table_schema(table_name)

    filecycle = 0
    logging.info("Processing total  %s files ",
                 str(len(filelist)))
    for file in filelist:
      try:
        logging.info("Processing for file %s ", str(file))
        data = storage_util.read_data_from_storage(gcs_file_path=file,
                                                   gcs_bucket_name=bucket_name,
                                                   file_type="CSV")
        read_csv_and_ingest_into_bq(data, table_name,
                                    file, schema,
                                    batch_timestamp, record_date)
        filecycle += 1
      except ValueError:
        pass
    logging.info("%s/%s are successfully "
                 "ingested in BigQuery", str(filecycle), str(len(filelist)))
    return f"{filecycle}/{len(filelist)} are " \
           f"successfully ingested in BigQuery."

  except Exception as exception:
    logging.error("Exception occurred due to %s", str(exception))
    raise exception


if __name__ == "__main__":
  app.run(debug=True, host="0.0.0.0", port=constant.PORT)
