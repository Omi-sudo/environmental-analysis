"""
job_audit_utils.py Module
This module contains function to gather all the audit metrics of pipeline
"""

import logging
from datetime import datetime

import bq_utils
import constants
import pytz


logging.basicConfig(level=logging.INFO)


def get_insert_audit_rows(data_source=None, data_source_last_edit_date=None,
                          layer_name=None, source_query_url=None,
                          task_name=None,
                          destination=None,
                          count=None,
                          batch_timestamp=None,
                          status=None,
                          message=None):

  """
  This function will gather all the job audit metrics
  :param data_source: Source of data e.g. Arcgis api, soda api, etc
  :param data_source_last_edit_date: date on which data source was last modified
                                     or edited
  :param layer_name: Data layer name
  :param source_query_url: endpoint used to fetch data
  :param task_name: which task/operation is happening
  :param destination: destination sink for the data
  :param count: number of elements / records in data
  :param batch_timestamp: timestamp on which execution of pipeline started
  :param status: status of operation SUCCESS/FAILED
  :param message: error message if task failed
  :return:
  """
  try:
    ingestion_timestamp = datetime.strptime(
        datetime.strftime(datetime.now(pytz.timezone("America/New_York")),
                          constants.TIME_FORMAT), constants.TIME_FORMAT)

    rows_to_insert = [{"data_source": data_source,
                       "data_source_last_edit_date": data_source_last_edit_date,
                       "layer_name": layer_name,
                       "source_query_url": source_query_url,
                       "step_name": task_name,
                       "destination": destination,
                       "count": count,
                       "batch_timestamp": batch_timestamp,
                       "ingestion_timestamp": ingestion_timestamp,
                       "status": status,
                       "message": message}]

    bq_utils.ingest_dataframe_to_bq(data=rows_to_insert,
                                    bq_table_name=constants.BQ_METADATA_DATASET
                                                  + "." +
                                                  constants.JOB_LOGGING_TABLE,
                                    ingestion_layer="audit_logs")

  except Exception as exception:
    logging.error("An exception occurred in "
                  "[get_insert_audit_rows]")
    logging.error("Exception occurred due to %s", str(exception))
    raise exception



