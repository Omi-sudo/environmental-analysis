"""
main.py module
This Module is the main python module which will be triggered by Cloud Run,
this module is responsible to fetch data from various web services and write the
data into the specified GCS locations.
"""
import sys
import logging
import json
import requests
from flask import Flask, request
from datetime import datetime

from sodapy import Socrata

from common.utils.socrata_parsing_util import \
  parse_geometry_coordinates_mutlipolygon_data, \
  parse_geometry_coordinates_point_data, parse_human_address_data, \
  prefix_check
from common.utils import job_audit_utils, bq_utils
from common import config, constant
from common.utils.storage_util import upload_data_on_gcs_bucket, \
  read_data_from_storage

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)


def fetch_data_layer_last_edit_date(url):
  """
  This function will fetch the last edit date from the SOCRATA apis
  :param url: data source endpoint url.
  :return: last modified date of the data source
  """
  try:
    logging.info("[fetch_data_layer_last_edit_date]"
                 "Fetching last edit date for url %s", url)
    req = requests.get(url.replace("count(*)", ":updated_at"))
    response = json.loads(req.content.decode("utf-8"))

    date_list = [dates[":updated_at"] for dates in response]
    date_list.sort(reverse=True)
    last_updated_datetime = datetime.strptime(date_list[0].rsplit(".")[0],
                                              "%Y-%m-%dT%H:%M:%S")
    last_updated_date = last_updated_datetime.date().strftime(
      constant.DATE_FORMAT)

    return [last_updated_datetime, last_updated_date]

  except Exception as exception:
    logging.error("An exception occurred in "
                  "[fetch_data_layer_last_edit_date]")
    logging.error("Exception occurred due to %s", str(exception))
    sys.exc_info()
    raise exception


def fetch_data_from_source(url, domain_name, dataset_name):
  """
    This function will fetch the data from source url,
    store into variable and return it.
    :param layer_url_endpoint: Feature Layer URL
    :param layer_last_edit_info:
    Feature layer last edit date information
    """
  try:
    logging.info("[fetch_data_from_source] "
                 "Fetching_data_from_source for url %s", url)
    count_request = requests.get(url)
    count = json.loads(count_request.content.decode("utf-8"))[0]["count"]
    client = Socrata(domain_name, None)
    results = client.get(dataset_name, limit=count)

    raw_table_data = json.dumps(results, indent=3)

    return raw_table_data

  except Exception as exception:
    logging.error("An exception occurred in [fetch_data_from_source]")
    logging.error("Exception occurred oue to %s", str(exception))
    sys.exc_info()
    raise exception


def split_and_format_data_layer_name(data_layer_name):
  """
  This function will split the comma separated data layer name
  and convert it into lower cases.

  :param data_layer_name comma separated data layer names e.g
                    Input -> ADult_care_FACility_map,adult_CARE_facility
                    Output -> [adult_care_facility_map,adult_care_facility]
  """
  try:
    logging.info("[split_and_format_data_layer_name] "
                 "split and format for data layer name %s",
                 data_layer_name)
    data_layer_name = data_layer_name.split(",")
    data_layer_name = list(map(lambda x: x.lower(), data_layer_name))
    return data_layer_name

  except Exception as exception:
    logging.error("An exception occurred in "
                  "[split_and_format_data_layer_name]")
    logging.error("Exception occurred oue to %s", str(exception))
    sys.exc_info()
    raise exception


def fetch_config_info(batch_unix_timestamp, data_layer_name,
                      data_processing_type, raw_gcs_ingestion_date):
  """
   This function will fetch the required config values from the give
   data_layer_name's configuration mapping.

   :param batch_unix_timestamp: unix representation of batch_timestamp.
   :param data_layer_name:
   data layer for which config details fetched from mapping
   :param data_processing_type: raw / parsing
   :param raw_gcs_ingestion_date: date on which raw data was ingested in GCS

   """
  try:
    config_dict = {}

    if data_layer_name is not None \
            and raw_gcs_ingestion_date is None \
            and data_processing_type == "raw":
      data_layer_name = split_and_format_data_layer_name(data_layer_name)
      for layer_details in data_layer_name:
        logging.info("[read_data_from_source_and_ingest_to_gcs_raw] - "
                     "Processing data for %s", layer_details)
        layer_info = config.socrata_data_layer_and_gcp_mapping[layer_details]
        config_dict["layer_url"] = layer_info["url"]
        config_dict["raw_gcs_file_path"] = \
          layer_info["raw_gcs_file_uri"].format(batch_unix_timestamp)
        config_dict["domain_name"] = layer_info["domain_name"]
        config_dict["dataset_name"] = layer_info["dataset_name"]
        config_dict["data_source"] = layer_info["data_source"]

        config_dict["layer_last_modified_info"] = \
          fetch_data_layer_last_edit_date(config_dict["layer_url"])
        config_dict["layer_name"] = layer_info["layer_name"]

    elif data_layer_name is not None \
            and raw_gcs_ingestion_date is not None \
            and batch_unix_timestamp is not None \
            and data_processing_type == "parse":
      data_layer_name = split_and_format_data_layer_name(data_layer_name)
      for layer_details in data_layer_name:
        logging.info(
          "Processing and parsing raw data for %s", layer_details)
        layer_info = config.socrata_data_layer_and_gcp_mapping[layer_details]

        config_dict["raw_gcs_file_uri"] = \
          layer_info["raw_gcs_file_uri"].format(batch_unix_timestamp)
        config_dict["data_layer_name"] = layer_info["layer_name"]
        config_dict["parsing_type"] = layer_info["parsing_type"]
        config_dict["layer_url_endpoint"] = layer_info["url"]
        config_dict["parsed_gcs_file_uri"] = \
          layer_info["parsed_gcs_file_uri"].format(batch_unix_timestamp)
        config_dict["data_source"] = layer_info["data_source"]

        config_dict["layer_last_edit_info"] = \
          fetch_data_layer_last_edit_date(config_dict["layer_url_endpoint"])

        raw_gcs_file_uri = config_dict["raw_gcs_file_uri"].rsplit("/", 2)
        raw_gcs_file_uri[1] = raw_gcs_ingestion_date
        config_dict["raw_gcs_file_uri"] = \
          "/".join(raw_gcs_file_uri).format(batch_unix_timestamp)

    return config_dict

  except Exception as exception:
    logging.error("An exception occurred in [fetch_config_info]")
    logging.error("Exception occurred oue to %s", str(exception))
    sys.exc_info()
    raise exception


def upload_data(source_data_url, gcs_file_uri, table_data,
                pipeline_batch_time, layer_last_modified_info,
                data_layer_name, source,
                gcs_bucket_name, task_name, record_count):
  """
  This function will fetch the data from soda api and results will be send
  to two different locations i.e raw and parsed.
  :param source_data_url: SODA api endpoint url
  :param gcs_file_uri: gcs file path where complete data (raw)
    will be uploaded.
  :param pipeline_batch_time: timestamp when execution of pipeline started
  :param layer_last_modified_info: date on which dataset was last modified
  :param data_layer_name: Soda api data layer name e.g Health Facilities.
  :param source: data source name e.g. Arcgis api, soda api etc..
  :param table_data: data needs to be uploaded.
  :param gcs_bucket_name: gcs bucket where data needs to be uploaded.
  :param task_name: Name of teh task.
  :param record_count: Count of inserted records in GCP.
  :return:
  """

  try:

    logging.info(
      "[upload_data] -"
      " Uploading data at gs://%s/%s", gcs_bucket_name,
      gcs_file_uri
    )

    upload_data_on_gcs_bucket(
      data=table_data,
      gcs_file_path=gcs_file_uri,
      project_name=constant.PROJECT_ID,
      gcs_bucket_name=gcs_bucket_name,
    )

    job_audit_utils.get_insert_audit_rows(
      data_source=source,
      data_source_last_edit_date=layer_last_modified_info[0],
      task_name=task_name,
      source_query_url=source_data_url.split(".json")[0],
      batch_timestamp=pipeline_batch_time,
      layer_name=data_layer_name,
      destination=
      "gs://" + gcs_bucket_name + "/" + gcs_file_uri,
      count=record_count,
      status="SUCCESS")

  except Exception as exception:
    logging.error("An exception occurred  in [upload_data]")
    logging.error("Exception occurred oue to %s", str(exception))
    sys.exc_info()
    raise exception



@app.route("/process_raw_layer", methods=["GET"])
def read_data_from_source_and_ingest_to_gcs_raw():
  """
    This function will iterate through the
    config.socrata_data_layer_and_gcp_mapping
    to fetch the raw data from different socrata_api url and will write it
    to Cloud Storage.
  """
  batch_timestamp = None
  config_info = {}
  rec_count = 0
  data_source = None
  layer_url = None
  layer_name = None
  try:

    data_layer_name = request.args.get("layer_name")
    batch_timestamp = request.args.get("batch_timestamp")
    batch_unix_timestamp = request.args.get("batch_unix_timestamp")
    bucket = request.args.get("bucket")
    batch_timestamp = bq_utils.format_batch_timestamp(batch_timestamp)

    if batch_timestamp is None \
            or batch_timestamp == "None" \
            or batch_timestamp == "" \
            or batch_unix_timestamp is None \
            or batch_unix_timestamp == "None" \
            or batch_unix_timestamp == "" \
            or bucket is None \
            or bucket == "None" \
            or bucket == "":
      raise ValueError(
        "the supplied values of query parameters is not well formatted or none,"
        "the received value of "
        f", batch_timestamp is {batch_timestamp}"
        f"batch_unix_timestamp is {batch_unix_timestamp}, bucket is"
        f" {bucket}"
      )

    elif data_layer_name is None or data_layer_name == "":

      logging.info(
        "[read_data_from_source_and_ingest_to_gcs_raw] - No data layer has "
        "specified processing all data layers")
      for layer_details in config.socrata_data_layer_and_gcp_mapping:
        config_info = fetch_config_info(data_layer_name=layer_details,
                                        batch_unix_timestamp=
                                        batch_unix_timestamp,
                                        data_processing_type="raw",
                                        raw_gcs_ingestion_date=None)
        data_source = config_info["data_source"]
        layer_url = config_info["layer_url"].split(".json")[0]
        layer_name = config_info["layer_name"]

        raw_data = \
          fetch_data_from_source(url=config_info["layer_url"],
                                 domain_name=config_info["domain_name"],
                                 dataset_name=config_info["dataset_name"])
        if len(json.loads(raw_data)) == 0:
          pass
        else:
          upload_data(source_data_url=config_info["layer_url"],
                      table_data=raw_data,
                      gcs_file_uri=config_info["raw_gcs_file_path"],
                      layer_last_modified_info=
                      config_info["layer_last_modified_info"],
                      pipeline_batch_time=batch_timestamp,
                      data_layer_name=config_info["layer_name"],
                      source=config_info["data_source"],
                      gcs_bucket_name=bucket,
                      record_count=len(json.loads(raw_data)),
                      task_name="gcs_raw_data_ingestion"
                      )

    else:
      config_info = fetch_config_info(data_layer_name=data_layer_name,
                                      batch_unix_timestamp=batch_unix_timestamp,
                                      data_processing_type="raw",
                                      raw_gcs_ingestion_date=None)

      data_source = config_info["data_source"]
      layer_url = config_info["layer_url"].split(".json")[0]
      layer_name = config_info["layer_name"]
      raw_data = \
        fetch_data_from_source(url=config_info["layer_url"],
                               domain_name=config_info["domain_name"],
                               dataset_name=config_info["dataset_name"])
      rec_count = len(json.loads(raw_data))
      if len(json.loads(raw_data)) == 0:
        return f"Raw Success, number of " \
               f"records -> {data_layer_name} : {len(json.loads(raw_data))}"

      upload_data(source_data_url=config_info["layer_url"],
                  table_data=raw_data,
                  gcs_file_uri=config_info["raw_gcs_file_path"],
                  layer_last_modified_info=
                  config_info["layer_last_modified_info"],
                  pipeline_batch_time=batch_timestamp,
                  data_layer_name=config_info["layer_name"],
                  source=config_info["data_source"],
                  gcs_bucket_name=bucket,
                  record_count=len(json.loads(raw_data)),
                  task_name="gcs_raw_data_ingestion"
                  )

  except Exception as exception:
    logging.error(
      "An exception occurred  in "
      "[read_data_from_source_and_ingest_to_gcs_raw]"
    )
    logging.error("Exception occurred due to %s", str(exception))
    logging.error("Execution occurred inserting logs into job audit table")
    job_audit_utils.get_insert_audit_rows(
      data_source=data_source,
      task_name="gcs_raw_data_ingestion",
      source_query_url=layer_url,
      batch_timestamp=batch_timestamp,
      layer_name=layer_name,
      message=(f"Exception occurred due to {str(exception)}" + " " + str(
        sys.exc_info())),
      status="FAILED")
    raise exception

  return f"Raw Success, number " \
         f"records -> {data_layer_name} : {rec_count} "


def prepare_parse_data(data, parsing_type):
  parsed_table_data = None

  try:
    logging.info(
      "[prepare_parse_data] - Parsing type is %s", parsing_type
    )
    if parsing_type == "multipolygon_data":
      parsed_table_data = \
        parse_geometry_coordinates_mutlipolygon_data(json.loads(data))
    elif parsing_type == "point_data":
      parsed_table_data = \
        parse_geometry_coordinates_point_data(json.loads(data))
    elif parsing_type == "human_address_data":
      parsed_table_data = parse_human_address_data(json.loads(data))
    elif parsing_type == "no_parsing":
      parsed_table_data = prefix_check(json.loads(data))

    return parsed_table_data

  except Exception as exception:
    logging.error("An exception occurred  in [prepare_parse_data]")
    logging.error("Exception occurred due to %s", str(exception))
    sys.exc_info()
    raise exception


def add_record_date_in_parsed_data(parsed_data, layer_last_modified_info):
  """
  This function will add a new key record_date having value to describe when
  the data layer was last edited/updated.

  parsed_data: parsed data
  layer_last_edit_info:
  layer_last_modified_info: Feature layer last edit date information

  """
  try:

    data = [
      dict(rows,
           **{"record_date"
              : layer_last_modified_info[1]})
      for rows in json.loads(parsed_data)
    ]

    return data

  except Exception as exception:
    logging.error("An exception occurred  in [add_record_date_in_parsed_data]")
    logging.error("Exception occurred due to %s", str(exception))
    sys.exc_info()
    raise exception


@app.route("/process_parse_layer", methods=["GET"])
def read_gcs_raw_data_ingest_to_gcs_parse():
  """
  This method will read the raw data stored in the GCS Bucket.
  This endpoint/functions expects a data layer name for which data parsing &
  processing is required and the date on which its corresponding raw data was
  uploaded in the GCS bucket, the data can be found from the GCS bucket itself,
  and the date should be in format of YYYY-MM-DD or otherwise the code will
  throw and exception.
  """
  batch_timestamp = None
  config_info = {}
  data_source = None
  layer_url = None
  data_layer_name = None
  try:
    data_layer_name = request.args.get("layer_name")
    raw_gcs_ingestion_date = request.args.get("raw_gcs_ingestion_date")
    batch_timestamp = request.args.get("batch_timestamp")
    batch_unix_timestamp = request.args.get("batch_unix_timestamp")
    bucket = request.args.get("bucket")
    batch_timestamp = bq_utils.format_batch_timestamp(batch_timestamp)

    if data_layer_name is None or data_layer_name == "None" \
            or data_layer_name == "" \
            or batch_timestamp is None \
            or batch_timestamp == "None" \
            or batch_timestamp == "" \
            or batch_unix_timestamp is None \
            or batch_unix_timestamp == "None" \
            or batch_unix_timestamp == "" \
            or bucket is None \
            or bucket == "None" \
            or bucket == "" \
            or raw_gcs_ingestion_date is None \
            or raw_gcs_ingestion_date == "None" \
            or raw_gcs_ingestion_date == "":
      raise ValueError(
        "the supplied values of query parameters is not well formatted or none,"
        "the received value of data_layer_name "
        f"is {data_layer_name}, batch_timestamp is {batch_timestamp}"
        f"batch_unix_timestamp is {batch_unix_timestamp}, bucket is"
        f" {bucket}, raw_gcs_ingestion_date is "
        f"{raw_gcs_ingestion_date}"
      )

    try:
      datetime.strptime(raw_gcs_ingestion_date, constant.DATE_FORMAT)
    except ValueError as value_error:
      raise ValueError(
        "value of raw_gcs_ingestion_date "
        f"is not in the format of {constant.DATE_FORMAT}"
      ) from value_error

    config_info = fetch_config_info(batch_unix_timestamp=batch_unix_timestamp,
                                    data_layer_name=data_layer_name,
                                    data_processing_type="parse",
                                    raw_gcs_ingestion_date=
                                    raw_gcs_ingestion_date)
    data_source = config_info["data_source"]
    layer_url = config_info["layer_url_endpoint"].split(".json")[0]
    data_layer_name = config_info["data_layer_name"]

    raw_data = json.dumps(
      read_data_from_storage(
        config_info["raw_gcs_file_uri"],
        bucket))

    parsed_data = \
      prepare_parse_data(data=raw_data,
                         parsing_type=config_info["parsing_type"])

    formatted_parsed_data = \
      add_record_date_in_parsed_data(parsed_data=parsed_data,
                                     layer_last_modified_info=
                                     config_info["layer_last_edit_info"])

    upload_data(source_data_url=config_info["layer_url_endpoint"],
                table_data=json.dumps(formatted_parsed_data, indent=4),
                gcs_file_uri=config_info["parsed_gcs_file_uri"],
                layer_last_modified_info=config_info["layer_last_edit_info"],
                pipeline_batch_time=batch_timestamp,
                data_layer_name=config_info["data_layer_name"],
                source=config_info["data_source"],
                gcs_bucket_name=bucket,
                record_count=len(formatted_parsed_data),
                task_name="gcs_parsed_data_ingestion"
                )

  except Exception as exception:
    logging.error(
      "An exception occurred  in [read_gcs_raw_data_ingest_to_gcs_parse]")
    logging.error("Exception occurred due to %s", str(exception))
    logging.error("Execution occurred inserting logs into job audit table")
    job_audit_utils.get_insert_audit_rows(
      data_source=data_source,
      task_name="gcs_parsed_data_ingestion",
      source_query_url=layer_url,
      batch_timestamp=batch_timestamp,
      layer_name=data_layer_name,
      message=(f"Exception occurred due to {str(exception)}" + " " + str(
        sys.exc_info())),
      status="FAILED")
    raise exception

  return "Success"


if __name__ == "__main__":
  app.run(debug=True, host="0.0.0.0", port=constant.PORT)
