"""
utils.py Module
This is the utility module required to run the main module.
"""
import logging
import time
import sys
import requests
import subprocess
import traceback
from logging import info
import pandas as pd
from datetime import datetime
import pytz

import google.auth.transport.requests
import google.oauth2.id_token

import constants
import storage_util
import bq_utils
import job_audit_utils
from last_edit_date_utils import \
  fetch_arcgis_api_last_edit_date, \
  fetch_socrata_api_last_edit_date

logging.basicConfig(level=logging.INFO)


def get_xcom_values(task_instance, task_id, key_name):
  """
      This function will return the data stored in xcom
     :param task_instance: task instance of airflow task.
     :param task_id: task_id of the airflow task on which data pushed in xcom.
     :param key_name: key associated with the data pushed in xcom.
  """

  return task_instance.xcom_pull(task_ids=task_id, key=key_name)


def set_batch_timestamp(**context):
  """
  This method will push the current timestamp in xcom with a key name
  :param context: default parameter of dag
  :return: push the current timestamp in xcom with a key name
  """

  dag_id = None
  task_ids = None
  try:
    task_ids = str(context["task"]).split(":")[1].strip(">")
    dag_id = str(context["dag"]).split(":")[1].strip(">")
    current_timestamp = datetime.now(pytz.timezone(
      "America/New_York")).strftime(constants.TIME_FORMAT)
    unix_current_timestamp = int(time.mktime(datetime.strptime(
      current_timestamp, constants.TIME_FORMAT).timetuple()))
    info("current_timestamp : %s", current_timestamp)
    info("unix_current_timestamp : %s", unix_current_timestamp)
    # setting batch timestamp in a key
    task_instance = context["task_instance"]
    task_instance.xcom_push(key="batch_timestamp_key", value=current_timestamp)

    task_instance.xcom_push(
      key="unix_batch_timestamp_key", value=unix_current_timestamp
    )

  except Exception as exception:
    logging.error("An exception occurred in dag_name=%s, task_name=%s"
                  "[set_batch_timestamp]", str(dag_id), str(task_ids))
    logging.error("Exception occurred due to %s", str(exception))
    sys.exc_info()
    raise exception


def authenticate_and_trigger_cloud_run(
        url, service_endpoint, task_id_name, **context):
  """
  This method will authenticate into the cloud run and trigger it.
  :param url: cloud run service url.
  :param service_endpoint: cloud run service url endpoint with query parameters.
  :param task_id_name: task_id required to get xcom values
  :return: Trigger the respective cloud run service.
  """

  dag_id = None
  task_ids = None
  try:
    task_instance = context["task_instance"]
    batch_timestamp = get_xcom_values(
      task_instance, task_id_name, "batch_timestamp_key"
    )
    unix_current_timestamp = get_xcom_values(
      task_instance, task_id_name, "unix_batch_timestamp_key"
    )
    task_ids = str(context["task"]).split(":")[1].strip(">")
    dag_id = str(context["dag"]).split(":")[1].strip(">").strip()
    auth_req = google.auth.transport.requests.Request()
    info(f"url {str(url)}")
    service_endpoint = \
      str(service_endpoint).format(batch_timestamp, unix_current_timestamp)
    info(f"service_endpoint {str(service_endpoint)}")
    id_token = google.oauth2.id_token.fetch_id_token(auth_req, service_endpoint)

    headers = {
      "Authorization": "Bearer " + id_token,
      "Content-Type": "application/json; charset=utf-8",
    }

    response = requests.get(
      service_endpoint,
      headers=headers,
    )
    req_content = response.content.decode("utf-8")
    info(f"response : {req_content}")

    if response.status_code != 200:
      raise Exception(f"the response code for HTTP request is "
                      f"{response.status_code}: ", traceback.print_exc(),
                      )
    if "Raw" in req_content.strip():
      data_count = int(req_content.split(":")[1].strip())
      if data_count == 0:
        data_layer_name = \
          req_content.split(":")[0].strip().split("->")[1].strip()
        info(f"data_layer_name :{data_layer_name}")
        xcom_key = task_ids.lower().strip(" ") + "_key"
        info(f"xcom_key:{xcom_key}")
        task_instance.xcom_push(key=xcom_key, value=data_layer_name)
        info("XCOM pushed successfully")

  except Exception as exception:
    logging.error("An exception occurred in "
                  "dag_name=%s, task_name=%s"
                  "[authenticate_and_trigger_cloud_run]",
                  str(dag_id), str(task_ids))
    logging.error("Exception occurred due to %s", str(exception))
    sys.exc_info()
    raise exception


def fetch_bq_table_schema(bq_table_name):
  """
  This method will fetch the headers/columns of specified table
  param: bq_table_name BigQuery Table name for which headers need to be
  fetched
  return: list of comma separated columns names
  """
  try:
    logging.info("Fetching %s's schema", str(bq_table_name))

    # establishing a bigquery client connection to fetch column of bq table
    client = bq_utils.get_bq_client()
    table_ref = client.get_table(bq_table_name)
    result = [f"{schema.name.lower()}" for schema in table_ref.schema]
    return result
  except Exception as exception:
    logging.error("an exception occurred while fetching schema!!!")
    logging.error("failed to fetch schema due to %s", str(exception))
    logging.error(traceback.print_exc())
    raise Exception(traceback.print_exc()) from exception


def format_gcs_parse_data(batch_timestamp, data_source_last_edit_date,
                          data_source, gcs_data):
  """
  this function will format the gcs raw data
  :param batch_timestamp : timestamp when pipeline was triggered
  :param data_source_last_edit_date: last edit date of data source
  :param data_source: data source e.g. socrata,aqs, arcgis_apis
  :param gcs_data: raw gcs data
  :return formatted parsed data
  """
  try:

    data = None
    if data_source in ("arcgis_apis", "socrata"):
      data = [
        dict(
          rows,
          **{
            "ingestion_timestamp": batch_timestamp,
            "record_date":
              datetime.strptime(str(data_source_last_edit_date[1]),
                                constants.DATE_FORMAT)
          }
        )
        for rows in gcs_data
      ]

    elif data_source == "aqs":
      data = [
        dict(
          rows,
          **{
            "ingestion_timestamp": batch_timestamp
          }
        )
        for rows in gcs_data
      ]

    return data
  except Exception as exception:
    logging.error("an exception occurred in format_gcs_parse_data")
    logging.error("failed to fetch schema due to %s", str(exception))
    logging.error(traceback.print_exc())
    raise Exception(traceback.print_exc()) from exception


def read_data_from_gcs_and_ingest_to_bq(
        parsed_gcs_file_path, gcs_bucket_name, bq_table_name, data_source,
        layer_name, new_column_audit_table,
        layer_url, ingestion_layer, **kwargs):
  """
  This function will read the files from GCS and ingest into BigQuery.

  :param parsed_gcs_file_path: GCS path in which parsed filed is stored.
  :param gcs_bucket_name: Name of the bucket
  :param bq_table_name: BigQuery table name where the data will be ingested.
  :param data_source: Type of the api e.g (arcgis_apis/socrata/aqs)
  :param layer_name: Data layer name.
  :param layer_url: Webservice/Api endpoint.
  :param new_column_audit_table: BigQuery table name where schema audit logs
  inserted when new column added in source data.
  :param ingestion_layer: Ingestion layer where the data will ingest.
  :return: file/data residing on the GCS bucket
  """
  dag_id = None
  task_ids = None
  data_source_last_edit_date = None
  data = []

  try:
    task_ids = str(kwargs["task"]).split(":")[1].strip(">")
    dag_id = str(kwargs["dag"]).split(":")[1].strip(">")
    task_instance = kwargs["task_instance"]
    batch_timestamp = get_xcom_values(
      task_instance, "RAW_GCS_INGESTION_STARTS", "batch_timestamp_key"
    )
    batch_timestamp = \
      datetime.strptime(batch_timestamp, constants.TIME_FORMAT)

    unix_current_timestamp = get_xcom_values(
      task_instance, "RAW_GCS_INGESTION_STARTS", "unix_batch_timestamp_key"
    )

    parsed_gcs_file_path = parsed_gcs_file_path.format(unix_current_timestamp)

    gcs_data = storage_util.read_data_from_storage(
      gcs_file_path=parsed_gcs_file_path, gcs_bucket_name=gcs_bucket_name
    )

    if data_source == "arcgis_apis":
      data_source_last_edit_date = \
        fetch_arcgis_api_last_edit_date(layer_url)
      data = format_gcs_parse_data(batch_timestamp=batch_timestamp,
                                   data_source_last_edit_date=
                                   data_source_last_edit_date,
                                   data_source=data_source,
                                   gcs_data=gcs_data)
    elif data_source == "socrata":
      data_source_last_edit_date = fetch_socrata_api_last_edit_date(layer_url)
      data = format_gcs_parse_data(batch_timestamp=batch_timestamp,
                                   data_source_last_edit_date=
                                   data_source_last_edit_date,
                                   data_source=data_source,
                                   gcs_data=gcs_data)

    elif data_source == "aqs":
      data = format_gcs_parse_data(batch_timestamp=batch_timestamp,
                                   data_source_last_edit_date=None,
                                   data_source=data_source,
                                   gcs_data=gcs_data)

    schema = fetch_bq_table_schema(bq_table_name=bq_table_name)
    source_columns = []
    for itr in data:
      source_columns.extend([*itr])

    source_columns = [each_string.lower() for each_string in source_columns]

    col_diff = list(set(list(set(source_columns))) - set(schema))
    if len(col_diff) >= 1:
      ingestion_timestamp = constants.CURRENT_UTC_DATETIME
      col_diff_data = [[data_source, layer_name, str(col_diff), layer_url,
                        batch_timestamp, ingestion_timestamp]]
      col_diff_data = pd.DataFrame(col_diff_data,
                                   columns=
                                   fetch_bq_table_schema
                                   (new_column_audit_table))

      bq_utils.ingest_dataframe_to_bq(data=col_diff_data,
                                      bq_table_name=new_column_audit_table,
                                      ingestion_layer="audit_logs")

    clean_data = []
    for itr in data:
      for diff in col_diff:
        if diff in itr:
          itr.pop(diff)
        else:
          pass
      clean_data.append(itr)
    bq_utils.ingest_dataframe_to_bq(data=pd.DataFrame(clean_data),
                                    bq_table_name=bq_table_name,
                                    ingestion_layer=ingestion_layer)

  except Exception as exception:
    logging.error("An exception occurred in "
                  "dag_name=%s, task_name=%s"
                  "[read_data_from_gcs_and_ingest_to_bq]",
                  str(dag_id), str(task_ids))
    logging.error("Exception occurred due to %s", str(exception))
    raise exception
  return "Success"


def bq_insert_job_audit_rows(bq_table_name, data_source,
                             layer_name, task_name,
                             layer_url, task_id_name, query, **kwargs):
  """
     This function will ingest the job audit logs
     of bq raw ingestion layer into BigQuerry.
     :param bq_table_name: BigQuery table name where
     the data will be ingested.
     :param data_source: Type of the api e.g (arcgis_apis/socrata/aqs)
     :param layer_name: Data layer name.
     :param layer_url: Webservice/Api endpoint.
     :param task_id_name: task_id required to get xcom values
     :param task_name: Name of the task.
     :param query:sql query to fetch the data from BigQuery.
     :return: bq raw ingestion layer audit logs
     insertion in job audit table
  """

  data_source_last_edit_date = None
  dag_id = None
  task_ids = None

  try:
    task_ids = str(kwargs["task"]).split(":")[1].strip(">")
    dag_id = str(kwargs["dag"]).split(":")[1].strip(">")
    task_instance = kwargs["task_instance"]
    batch_timestamp = get_xcom_values(
      task_instance, task_id_name, "batch_timestamp_key")

    batch_timestamp = \
      datetime.strptime(batch_timestamp, constants.TIME_FORMAT)

    count = bq_utils.read_data_from_bq(query)["COUNT"].tolist()
    logging.info("count is %s", str(count))

    job_metad_query = bq_utils.read_data_from_bq(
      constants.JOB_AUDIT_INFO.format(batch_timestamp,
                                      data_source,
                                      layer_name))

    if data_source == "socrata":
      layer_url = layer_url.split(".json")[0]
      data_source_last_edit_date = datetime.strptime((
        job_metad_query["data_source_last_edit_date"].to_dict()
        [0]).strftime(constants.TIME_FORMAT_SECONDS)
         ,constants.TIME_FORMAT_SECONDS)
    elif data_source == "aqs":
      layer_url = job_metad_query["source_query_url"].to_dict()[0]
      data_source_last_edit_date = datetime.strptime(
        (job_metad_query[
        "data_source_last_edit_date"].to_dict()[0]).strftime(
        constants.TIME_FORMAT_SECONDS),
        constants.TIME_FORMAT_SECONDS)
    elif data_source == "arcgis_apis":
      data_source_last_edit_date = datetime.strptime(
        (job_metad_query[
        "data_source_last_edit_date"].to_dict()[0]).strftime(
        constants.TIME_FORMAT),
        constants.TIME_FORMAT)

    elif data_source == "FTP":
      data_source_last_edit_date = None

    job_audit_utils.get_insert_audit_rows(data_source=data_source,
                                          data_source_last_edit_date=
                                          data_source_last_edit_date,
                                          layer_name=layer_name,
                                          source_query_url=layer_url,
                                          task_name=task_name,
                                          destination=bq_table_name,
                                          count=count[0],
                                          status="SUCCESS",
                                          batch_timestamp=batch_timestamp,
                                          message=None,
                                          )
  except Exception as exception:
    logging.error("An exception occurred in "
                  "dag_name=%s, task_name=%s"
                  "[bq_raw_insert_job_audit_rows]"
                  , str(dag_id), str(task_ids))
    logging.error("Exception occurred due to %s", str(exception))
    raise exception


def read_data_from_source_bq_and_ingest_destination_bq(
        source_table_name, data_source,
        ingestion_layer,
        destination_table_name, **kwargs):
  """
  This function will read the data from source table from BigQuery
  and ingest destination table in BigQuery.
  :param source_table_name: BigQuery table
  name where the data will be ingested.
  :param data_source: Type of the api e.g (arcgis_apis/socrata/aqs)
  :param ingestion_layer: Ingestion layer where the data will ingest.
  :param destination_table_name: destination_table_name
  :return: file/data residing on the GCS bucket
  """

  dag_id = None
  task_ids = None

  try:
    task_ids = str(kwargs["task"]).split(":")[1].strip(">")
    dag_id = str(kwargs["dag"]).split(":")[1].strip(">")
    task_instance = kwargs["task_instance"]
    batch_timestamp = get_xcom_values(
      task_instance, "RAW_GCS_INGESTION_STARTS", "batch_timestamp_key"
    )
    batch_timestamp = \
      datetime.strptime(batch_timestamp, constants.TIME_FORMAT)

    if data_source == "arcgis_apis":
      data = bq_utils.read_data_from_bq(source_table_name)
      bq_utils.ingest_dataframe_to_bq(data=pd.DataFrame(data),
                                      bq_table_name=destination_table_name,
                                      ingestion_layer=ingestion_layer)
    elif data_source == "socrata":
      data = bq_utils.read_data_from_bq(source_table_name)
      bq_utils.ingest_dataframe_to_bq(data=pd.DataFrame(data),
                                      bq_table_name=destination_table_name,
                                      ingestion_layer=ingestion_layer)
    elif data_source == "aqs":
      if ingestion_layer == "bq_warehouse":
        data = bq_utils.read_data_from_bq(source_table_name)
        bq_utils.ingest_dataframe_to_bq(data=pd.DataFrame(data),
                                        bq_table_name=destination_table_name,
                                        ingestion_layer=ingestion_layer)
      elif ingestion_layer == "aqs_bq_reporting":

        source_table_name = source_table_name.format(
          batch_timestamp)
        data = bq_utils.ingest_dataframe_to_bq(data=None,
                                               bq_table_name=
                                               source_table_name,
                                               ingestion_layer=
                                               ingestion_layer)

  except Exception as exception:
    logging.error("An exception occurred in "
                  "dag_name=%s, task_name=%s"
                  "[read_data_from_source_bq_and_ingest_destination_bq]"
                  , str(dag_id), str(task_ids))
    logging.error("Exception occurred due to %s", str(exception))
    raise exception


def get_xcoms_from_tasks(xcom_tasks_key_list,
                         upstream_tasks_list, step_name, **context):
  """
  This function will return only those tasks for
  aqs apis which needs to skip after raw gcs layer
  :param xcom_tasks_key_list : this list will
  contain the xcoms values which needs to be skip
  :param upstream_tasks_list : this list contain
  the tasks name from the upstream layer
  :param step_name: layer name

  return list of comma separated tasks needs to be skipped

  """
  task_instance = context["task_instance"]
  xcom_list = []

  for itr in xcom_tasks_key_list:
    xcoms = get_xcom_values(
      task_instance=task_instance, task_id=itr.strip(" "),
      key_name=itr.lower().strip(" ") + "_key"
    )

    if xcoms is not None:
      xcom_list.append(xcoms + "_" + step_name)

  if len(xcom_list) > 0:
    info("intersection %s "
         , str(list(set(upstream_tasks_list) - set(xcom_list))))
    return list(set(upstream_tasks_list) - set(xcom_list))
  else:
    return upstream_tasks_list


def check_files_in_uploads():
  """
    This method will check the if files are
    present in bucket or not.
    :param return: If files is present in uploads
    it will return "TRUNCATE_RAW_TABLE"
    else return "NO_FILES_FROM_FTP."
  """
  try:
    bucket = \
      storage_util.get_storage_bucket(
        constants.PROJECT_ID, constants.FTP_BUCKET_NAME)
    files = bucket.list_blobs(delimiter="/")
    filelist = [file.name for file in files]
    filelist = list(filter(lambda x: ".NY1" in x, filelist))
    if len(filelist) > 0:
      return "TRUNCATE_RAW_TABLE"
    else:
      return "NO_FILES_FROM_FTP"

  except Exception as exception:
    logging.error("An exception occurred in "
                  "[check_files_in_uploads]")
    logging.error("Exception occurred due to %s", str(exception))
    raise exception


def moving_files_from_gcs(query_string,
                          task_id_name, cmd, status, **kwargs):
  """
      This function will move the files from
      once gcs folder to another
      based on status,data_source and batch_timestamp
      from job audit table.
      Based on above 3 parameters the query has been
      executed to filter the data
      If the status of record is SUCCESS then
      that particular file will be moved to processed similary
      for FAILED status record that file
      will be moved to failed folder in GCS.
      :param query_string: query to filter data from job audit table.
      :param task_id_name: task_id required to get xcom values
      :param cmd: gsutil command to move
      the files from one folder to another
      :param status: processed/failed.
      :return: file/data moved to one gcs folder to another
  """

  dag_id = None
  task_ids = None
  try:
    task_ids = str(kwargs["task"]).split(":")[1].strip(">")
    info("task_ids is %s", str(task_ids))
    dag_id = str(kwargs["dag"]).split(":")[1].strip(">")
    task_instance = kwargs["task_instance"]
    batch_timestamp = get_xcom_values(
      task_instance, task_id_name, "batch_timestamp_key"
    )
    batch_timestamp = \
      datetime.strptime(batch_timestamp, constants.TIME_FORMAT)

    query_string = query_string.format(batch_timestamp)
    df = bq_utils.read_data_from_bq(query_string)
    filelist = df["layer_name"].tolist()
    info(filelist)
    for file in filelist:
      info("file %s is %s hence moving to %s folder.",
           str(file), str(status), str(status))
      with subprocess.Popen(cmd.format(file), shell=True) as p:
        p.wait()
      info("File moved successfully.")

  except Exception as exception:
    logging.error("An exception occurred in "
                  "dag_name=%s, task_name=%s"
                  "[moving_files_from_gcs]"
                  , str(dag_id), str(task_ids))
    logging.error("Exception occurred due to %s", str(exception))
    raise exception
