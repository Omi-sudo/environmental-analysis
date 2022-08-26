"""last_edit_date_utils.py module
This module returns last_edit_date of the dataset
of the respective data layer
"""

import json
import logging
import requests
from datetime import datetime

import constants
import storage_util


def fetch_arcgis_api_last_edit_date(feature_layer_url):
  """
  This function will fetch the last edit date from the
  arcgis_api feature layer.
  :param feature_layer_url: feature layer url
  :return: last edit date
  """
  try:
    url = requests.get(feature_layer_url + "?f=pjson")
    req_resp = \
      json.loads(url.content.decode("utf-8"))["editingInfo"][
        "lastEditDate"]

    last_edit_datetime = datetime.strptime(
      datetime.utcfromtimestamp(req_resp / 1000).strftime(
        constants.TIME_FORMAT),
      constants.TIME_FORMAT)

    last_edit_date = last_edit_datetime.date()

  except Exception as exception:
    logging.error("An exception occurred in "
                  "[fetch_arcgis_api_last_edit_date]")
    logging.error("Exception occurred due to %s", str(exception))
    raise exception

  return [last_edit_datetime, last_edit_date]


def fetch_socrata_api_last_edit_date(url):
  """

  This function will fetch the last edit date from the socrata_apis.
  :param url: data source endpoint url.
  :return: last modified date of the data source
  """
  try:
    req = requests.get(url.replace("count(*)", ":updated_at"))
    response = json.loads(req.content.decode("utf-8"))

    date_list = [dates[":updated_at"] for dates in response]
    date_list.sort(reverse=True)
    last_updated_datetime = datetime.strptime(date_list[0].rsplit(".")[0],
                                              "%Y-%m-%dT%H:%M:%S")
    last_updated_date = last_updated_datetime.date()

  except Exception as exception:
    logging.error("An exception occurred in "
                  "[fetch_socrata_api_last_edit_date]")
    logging.error("Exception occurred due to %s", str(exception))
    raise exception

  return [last_updated_datetime, last_updated_date]


def fetch_aqs_api_last_edit_date(parsed_gcs_file_uri):
  """
    This function will fetch the last edit date from the aqs_apis.
    :param parsed_gcs_file_uri: path of parsed gcs file.
    :return: last modified date of the data source
    """

  try:
    parsed_data = \
      json.loads(json.dumps(storage_util.read_data_from_storage(
        parsed_gcs_file_uri, constants.
            GCS_BUCKET_MAPPING[constants.ENVIRONMENT]
        ["AQS_GCS_BUCKET_NAME"])))

    last_edit_date = []
    for data in parsed_data:
      date_from_data = \
        datetime.strptime(data["date_of_last_change"], constants.DATE_FORMAT)
      last_edit_date.append(date_from_data)
    last_edit_date.sort(reverse=True)
    latest_edit_date = last_edit_date[0].strftime(constants.DATE_FORMAT)
    latest_date = datetime.strptime(latest_edit_date, constants.DATE_FORMAT)

    logging.info("latest_date: %s ", str(latest_date))
    logging.info("latest_date.date() : %s ", str(latest_date.date()))

  except Exception as exception:
    logging.error("An exception occurred in "
                  "[fetch_socrata_api_last_edit_date]")
    logging.error("Exception occurred due to %s", str(exception))
    raise exception

  return [latest_date, latest_date.date()]
