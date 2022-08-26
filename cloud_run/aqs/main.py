"""
main.py module
This Module is the main python module which will be triggered by Cloud Run,
this module is responsible to fetch data from various AQS apis and write the
data into the specified GCS locations.
"""
import sys
from datetime import datetime, date
from dateutil.relativedelta import relativedelta
import calendar
import requests
import json
import logging
from flask import Flask, request

from common.utils import job_audit_utils,bq_utils
from common import config, constant
from common.utils.storage_util import \
  upload_data_on_gcs_bucket, read_data_from_storage

from common.utils.bq_utils import execute_query

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)


def upload_data(
        layer_url_endpoint, table_data,
        gcs_file_uri, layer_last_edit_info,
        pipeline_batch_time, feature_layer_name,
        source, gcs_bucket_name, record_count, task_name
):
  """
  This function will upload the raw data on specified gcs location
  and after the successful upload to GCS will make an entry to
  audit log table.

  :param layer_url_endpoint: GIS data layer url
  :param table_data: raw data
  :param gcs_file_uri: gcs file path where complete data (raw) will be
                             uploaded
  :param layer_last_edit_info: last edit information of data layer
  :param pipeline_batch_time: timestamp when execution of pipeline started
  :param feature_layer_name: arcgis_apis feature layer name
  :param source: data source name e.g. Arcgis api, Soda api, etc..
  :param gcs_bucket_name: GCS Bucket name
  :param record_count: Number records
  :param task_name: gcs_raw or parse ingestion
  """

  try:

    logging.info(
      "[upload_data] - Uploading data At gs://%s/"
      "%s", gcs_bucket_name, gcs_file_uri)

    upload_data_on_gcs_bucket(
      data=table_data,
      gcs_file_path=gcs_file_uri,
      project_name=constant.PROJECT_ID,
      gcs_bucket_name=gcs_bucket_name,
    )

    job_audit_utils.get_insert_audit_rows(
      data_source=source,
      data_source_last_edit_date=layer_last_edit_info,
      task_name=task_name,
      source_query_url=layer_url_endpoint,
      batch_timestamp=pipeline_batch_time,
      layer_name=feature_layer_name,
      destination=
      "gs://" + gcs_bucket_name + "/" + gcs_file_uri,
      count=record_count,
      status="SUCCESS")

  except Exception as exception:
    logging.error("An exception occurred in [upload_data]")
    logging.error("Exception occurred due to %s", str(exception))
    sys.exc_info()
    raise exception


def fetch_aqs_api_last_edit_date(data):
  """
      This function will fetch the last edit
      date from the AQS apis
      :param data: data fetched from aqs apis
      :return: list contains last edit date & last edit datetime
  """
  try:
    last_edit_date = []
    for rows in data:
      date_from_data = \
        datetime.strptime(rows["date_of_last_change"], constant.DATE_FORMAT)
      last_edit_date.append(date_from_data)
    last_edit_date.sort(reverse=True)
    latest_edit_date = \
      last_edit_date[0].strftime(constant.DATE_FORMAT)

    latest_date = \
      datetime.strptime(latest_edit_date, constant.DATE_FORMAT)

  except Exception as exception:
    logging.error("An exception occurred in"
                  " [fetch_aqs_api_last_edit_date]")
    logging.error("Exception occurred due to %s", str(exception))
    sys.exc_info()
    raise exception

  return [latest_date, latest_date.date()]


def fetch_data_from_aqs_api(layer_url, data_date_ranges):
  """
      This function will iterate through the
      config.aqs_api_data_layer_and_gcp_mapping to
      fetch data from different AQS apis and will
      write the data in parsed folder.
      :param layer_url: aqs api url
      :param data_date_ranges: dictionary object contains bdate and edate

      :return: data
  """
  data = []
  urls = []
  try:
    for dates in data_date_ranges:
      formatter_layer_url = layer_url.format(dates["bdate"], dates["edate"])
      urls.append(formatter_layer_url)
      logging.info("[fetch_data_from_aqs_api] - "
                   "fetching data from %s", str(formatter_layer_url))
      # the timeout 2400 seconds is for python code not for
      # cloud run
      result = requests.get(formatter_layer_url, timeout=2400)
      request_resp = json.loads(result.content.decode("utf-8"))
      response = (request_resp["Header"][0])
      if response["status"].lower() == "success":
        data.extend(request_resp["Data"])
      elif response["rows"] == 0:
        logging.info(response["status"].lower() +
                     " for the url " + formatter_layer_url)
      elif response["status"].lower() == "failed":
        raise ValueError(
          f"the request to AQS end point {formatter_layer_url} "
          f"failed due to {request_resp['Header'][0]['error'][0]}")

  except Exception as exception:
    logging.error("An exception occurred in"
                  " [fetch_data_from_aqs_api]")
    logging.error("Exception occurred due "
                  "to %s", str(fetch_data_from_aqs_api))
    sys.exc_info()
    raise exception

  return [data, urls]


def get_first_last_date(year, month):
  """
  this function will create the fist and last date from the provided
  month and year, in the format of yyyymmdd.

  :param year : year for which the first and last date needs to derived
  :param month : for month the first and last date needs to derived

  return dictionary object having two keys bdate & edate
  """
  try:
    first_date = str(year) + "-" + str(month) + "-0" + str(1)
    first_date = datetime.strptime(first_date, "%Y-%m-%d").date()
    late_date = calendar.monthrange(first_date.year, first_date.month)[1]
    bdate = str(year) + str(f"{month}") + "01"
    edate = str(year) + str(f"{month}") + str(late_date)
    dates = {"bdate": bdate, "edate": edate}
    return dates
  except Exception as exception:
    logging.error("An exception occurred in"
                  " [get_first_last_date]")
    logging.error("Exception occurred due "
                  "to %s", str(exception))
    sys.exc_info()
    raise exception


def prep_bdate_edate(year, month, lookup_month):
  """
  this function will create the fist and last date from the provided
  month and year, in the format of yyyymmdd.

  :param year : year for which the first and last date needs to derived
  :param month : for month the first and last date needs to derived
  :param lookup_month :
  number months for which data needs to fetched in case of current year

  return list object having one more dicts containing two keys bdate & edate

  """
  try:
    todays_date = date.today()
    dates = []

    if year is None or year == "None" or year == "" or len(year) != 4:
      raise TypeError(f"Incorrect value-{year}. The year should"
                      f"be in yyyy format")
    elif int(year) < todays_date.year:
      if month is None or month == "None" or month == "" or month == str("0") \
              or int(month) not in range(1, 13, 1):
        raise TypeError(f"Incorrect value-{month}. "
                        f"The month should"
                        f"be in from 01 to 12")
      else:
        ranges = get_first_last_date(year=year, month=month)
        dates.append(ranges)

    elif int(year) == todays_date.year:
      base_date = todays_date - relativedelta(months=2)
      if base_date.month < 10:
        base_date_month = "0" + str(base_date.month)
      else:
        base_date_month = base_date.month
      base_date_interval = \
        get_first_last_date(year=base_date.year, month=base_date_month)
      dates = [base_date_interval]
      if lookup_month is None or lookup_month == "None" or lookup_month == "":
        logging.info("Incorrect lookup month %s "
                     "Resetting it to default 4"
                     , str(lookup_month))
        lookup_month = 4
      for itr in range(1, int(lookup_month), 1):
        delta_dates = base_date - relativedelta(months=itr)
        if delta_dates.month < 10:
          delta_dates_month = "0" + str(delta_dates.month)
        else:
          delta_dates_month = delta_dates.month
        date_range = \
          get_first_last_date(year=delta_dates.year,
                              month=delta_dates_month)
        dates.append(date_range)
    else:
      if int(year) > todays_date.year:
        logging.info("The provided year: %s is "
                     "greater than the current year.", str(year))
        return ["The provided year: %s is greater "
                "than the current year.", str(year)]

    return dates
  except Exception as exception:
    logging.error("An exception occurred in"
                  " [prep_bdate_edate]")
    logging.error("Exception occurred due "
                  "to %s", str(exception))
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
  data_layer_name = data_layer_name.split(",")
  data_layer_name = list(map(lambda x: x.lower(), data_layer_name))
  return data_layer_name


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
            and batch_unix_timestamp is not None \
            and data_processing_type == "raw":
      data_layer_name = split_and_format_data_layer_name(data_layer_name)
      for layer_details in data_layer_name:
        logging.info("[fetch_config_info] - "
                     "Processing data for %s", layer_details)
        layer_info = config.aqs_api_data_layer_and_gcp_mapping[layer_details]
        config_dict["data_source"] = layer_info["data_source"]
        config_dict["layer_name"] = layer_info["layer_name"]
        config_dict["raw_gcs_file_uri"] = \
          layer_info["raw_gcs_file_uri"].format(batch_unix_timestamp)
        config_dict["layer_url"] = layer_info["layer_url"]


    elif data_layer_name is not None \
            and raw_gcs_ingestion_date is not None \
            and batch_unix_timestamp is not None \
            and data_processing_type == "parse":
      data_layer_name = split_and_format_data_layer_name(data_layer_name)
      for layer_name in data_layer_name:
        logging.info(
          "Processing and parsing raw data for %s", layer_name)
        layer_info = config.aqs_api_data_layer_and_gcp_mapping[layer_name]
        config_dict["data_source"] = layer_info["data_source"]
        config_dict["layer_name"] = layer_info["layer_name"]
        config_dict["raw_gcs_file_uri"] = \
          layer_info["raw_gcs_file_uri"].format(batch_unix_timestamp)
        config_dict["parsed_gcs_file_uri"] = \
          layer_info["parsed_gcs_file_uri"].format(batch_unix_timestamp)
        config_dict["layer_url_endpoint"] = layer_info["layer_url"]

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


@app.route("/process_raw_layer", methods=["GET"])
def process_raw_layer():
  """
      This function will iterate through the
      config.aqs_api_data_layer_and_gcp_mapping
      to fetch data from different AQS apis and
      will write the data in raw folder.
  """

  data = []
  batch_timestamp = None
  data_source = None
  data_layer_name = None
  config_info = {}
  layer_url_endpoint = None

  try:
    year = request.args.get("year")
    data_layer_name = request.args.get("layer_name")
    batch_timestamp = request.args.get("batch_timestamp")
    batch_unix_timestamp = request.args.get("batch_unix_timestamp")
    bucket = request.args.get("bucket")
    month = request.args.get("month")
    lookup_month = request.args.get("lookup_month")

    batch_timestamp = bq_utils.format_batch_timestamp(
      batch_timestamp=batch_timestamp)

    data_date_ranges = \
      prep_bdate_edate(year=year, month=month,
                       lookup_month=lookup_month)
    if isinstance(data_date_ranges, list) \
            and len(data_date_ranges) == 1 \
            and isinstance(data_date_ranges[0], str):
      return f"Raw Success, the provided year {year} " \
             f"is greater than the current year," \
             f" number records -> {data_layer_name} : {len(data)} "

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
        f" {bucket}",
      )

    elif data_layer_name is None \
            or data_layer_name == "":

      logging.info("[process_raw_layer] - No "
                   "pollutant has specified in query param "
                   "hence processing for all pollutants "
                   "for the year %s", str(year))

      for layer_name in config.aqs_api_data_layer_and_gcp_mapping:
        config_info = fetch_config_info(data_layer_name=layer_name,
                                        batch_unix_timestamp=
                                        batch_unix_timestamp,
                                        data_processing_type="raw",
                                        raw_gcs_ingestion_date=None)
        data_source = config_info["data_source"]
        data_layer_name = config_info["layer_name"]

        data = fetch_data_from_aqs_api(layer_url=config_info["layer_url"],
                                       data_date_ranges=data_date_ranges)
        layer_url_endpoint = (str(data[1])[1:-1])[1:-1]
        if len(data[0]) == 0:
          pass
        else:

          last_edit_date_info = fetch_aqs_api_last_edit_date(data[0])

          formatted_data = json.dumps(data[0], indent=3)
          upload_data(layer_url_endpoint=(str(data[1])[1:-1])[1:-1],
                      table_data=formatted_data,
                      gcs_file_uri=config_info["raw_gcs_file_uri"],
                      layer_last_edit_info=last_edit_date_info[0],
                      pipeline_batch_time=batch_timestamp,
                      feature_layer_name=layer_name,
                      source=config_info["data_source"],
                      gcs_bucket_name=bucket,
                      record_count=len(data[0]),
                      task_name="gcs_raw_data_ingestion"
                      )

    else:
      config_info = fetch_config_info(data_layer_name=data_layer_name,
                                      batch_unix_timestamp=batch_unix_timestamp,
                                      data_processing_type="raw",
                                      raw_gcs_ingestion_date=None)
      data_source = config_info["data_source"]
      data_layer_name = config_info["layer_name"]
      data = fetch_data_from_aqs_api(layer_url=config_info["layer_url"],
                                     data_date_ranges=data_date_ranges)
      layer_url_endpoint = (str(data[1]))
      if len(data[0]) == 0:
        return f"Raw Success,  number of " \
               f"records -> {data_layer_name} : {len(data[0])} "
      else:

        last_edit_date_info = fetch_aqs_api_last_edit_date(data[0])
        formatted_data = json.dumps(data[0], indent=3)
        upload_data(layer_url_endpoint=layer_url_endpoint,
                    table_data=formatted_data,
                    gcs_file_uri=config_info["raw_gcs_file_uri"],
                    layer_last_edit_info=last_edit_date_info[0],
                    pipeline_batch_time=batch_timestamp,
                    feature_layer_name=data_layer_name.lower(),
                    source=config_info["data_source"],
                    gcs_bucket_name=bucket,
                    record_count=len(data[0]),
                    task_name="gcs_raw_data_ingestion"
                    )

  except Exception as exception:
    logging.error(
      "An exception occurred in [process_raw_layer]"
    )

    logging.error("Exception occurred due to %s", str(exception))
    logging.error("Exception occurred inserting logs into job audit table")
    job_audit_utils.get_insert_audit_rows(
      data_source=data_source,
      task_name="gcs_raw_data_ingestion",
      source_query_url=layer_url_endpoint,
      batch_timestamp=batch_timestamp,
      layer_name=data_layer_name,
      message=(f"Exception occurred due to {str(exception)}" + " " + str(
        sys.exc_info())),
      status="FAILED")
    raise exception

  return f"Raw Success, number of records -> " \
         f"{data_layer_name} : {len(data[0])} "


@app.route("/process_parse_layer", methods=["GET"])
def process_parse_layer():
  """
      This function will iterate through the
      config.aqs_api_data_layer_and_gcp_mapping
      to fetch data from different AQS apis
      and will write the data in parsed folder.
  """

  config_info = {}
  batch_timestamp = None
  job_audit_metad = {}

  try:
    data_layer_name = request.args.get("layer_name")
    raw_gcs_ingestion_date = request.args.get("raw_gcs_ingestion_date")
    batch_timestamp = request.args.get("batch_timestamp")
    batch_unix_timestamp = request.args.get("batch_unix_timestamp")
    bucket = request.args.get("bucket")

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
        "the supplied values of query parameters "
        "is not well formatted or none,"
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

    batch_timestamp = bq_utils.format_batch_timestamp(
      batch_timestamp=batch_timestamp)

    config_info = fetch_config_info(batch_unix_timestamp=batch_unix_timestamp,
                                    data_layer_name=data_layer_name,
                                    data_processing_type="parse",
                                    raw_gcs_ingestion_date=
                                    raw_gcs_ingestion_date)

    parsed_data = \
      read_data_from_storage(config_info["raw_gcs_file_uri"],
                             bucket)

    job_audit_metad = execute_query(
      query=f"SELECT * FROM `{constant.BQ_METADATA_DATASET}."
            f"{constant.JOB_LOGGING_TABLE}` "
            f"where batch_timestamp = "
            f"'{batch_timestamp}' and layer_name="
            f"'{config_info['layer_name']}' "
            f"and step_name = 'gcs_raw_data_ingestion' "
            f"and status = 'SUCCESS' limit 1",
      table_name=constant.JOB_LOGGING_TABLE)

    upload_data(layer_url_endpoint=job_audit_metad["source_query_url"],
                table_data=json.dumps(parsed_data, indent=4),
                gcs_file_uri=config_info["parsed_gcs_file_uri"],
                layer_last_edit_info=
                job_audit_metad["data_source_last_edit_date"],
                pipeline_batch_time=batch_timestamp,
                feature_layer_name=config_info["layer_name"],
                source=config_info["data_source"],
                gcs_bucket_name=bucket,
                record_count=len(parsed_data),
                task_name="gcs_parsed_data_ingestion"
                )

  except Exception as exception:
    logging.error(
      "An exception occurred in [process_parsed_data_layer]"
    )

    logging.error("Exception occurred due to %s", str(exception))
    logging.error("Execution occurred inserting logs into job audit table")
    job_audit_utils.get_insert_audit_rows(
      data_source=config_info["data_source"],
      task_name="gcs_parsed_data_ingestion",
      source_query_url=job_audit_metad["source_query_url"],
      batch_timestamp=batch_timestamp,
      layer_name=config_info["layer_name"],
      message=(f"Exception occurred due to {str(exception)}" + " " + str(
        sys.exc_info())),
      status="FAILED")
    raise exception

  return "Success"


if __name__ == "__main__":
  app.run(debug=True, host="0.0.0.0", port=constant.PORT)
