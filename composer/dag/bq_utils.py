"""
bq_utils.py Module
This module contains all the functions needs to interact with BigQuery
"""
import logging
from google.cloud import bigquery
import pandas as pd

import constants

logging.basicConfig(level=logging.INFO)


def get_bq_client():
  """
  This method will create a BigQuery client
  :return: This function will returns the client for the BigQuery
  """
  bq_client = None
  try:
    bq_client = bigquery.Client(project=constants.PROJECT_ID)

  except Exception as exception:
    logging.error("An exception occurred in [get_bq_client]")
    logging.error("Exception occurred due to %s", str(exception))
    raise exception

  return bq_client


def read_data_from_bq(query_string):
  """
    This method will read data from a BigQuery.
    :return: This function will return the data in form of
    dataframe
    """
  try:
    client = get_bq_client()
    # Download query results.
    logging.info("Query String %s", str(query_string))
    dataframe = (
      client.query(query_string)
        .result()
        .to_dataframe(
        create_bqstorage_client=True)
    )

  except Exception as exception:
    logging.error("An exception occurred in "
                  "[read_data_from_bq]")
    logging.error("Exception occurred due to %s", str(exception))
    raise exception
  return dataframe


def ingest_dataframe_to_bq(data, bq_table_name, ingestion_layer):
  """
  This method will ingest the input dataframe
  into the specified BigQuery table
  :param data: input data rows to be ingested
  :param bq_table_name: BQ table name where data needs to be ingested
  :param ingestion_layer: ion layer nameIngest
  """

  try:
    if ingestion_layer in ("bq_raw", "bq_reporting"):
      client = get_bq_client()
      table_ref = client.get_table(bq_table_name)
      # Note:  WRITE_DISPOSITION= WRITE_TRUNCATE option in client
      # library is deleting the data along with schema
      # hence we have used TRUNCATE TABLE query to delete data only.
      truncate_query = \
        f"TRUNCATE TABLE `{bq_table_name}`"
      client.query(truncate_query).result()
      job_config = bigquery.LoadJobConfig()
      job_config.autodetect = True

      insert_data = client.load_table_from_dataframe(
        dataframe=pd.DataFrame(data), destination=table_ref,
        job_config=job_config
      )
      insert_data.result()
    elif ingestion_layer in "aqs_bq_reporting":
      client = get_bq_client()
      logging.info("Query String %s", str(bq_table_name))
      client.query(bq_table_name).result()

    elif ingestion_layer in "audit_logs":
      client = get_bq_client()
      table_ref = client.get_table(bq_table_name)
      job_config = bigquery.LoadJobConfig(write_disposition="WRITE_APPEND")
      job_config.autodetect = True

      insert_data = \
        client.load_table_from_dataframe(
          dataframe=pd.DataFrame(data), destination=table_ref)
      insert_data.result()

    else:
      client = get_bq_client()
      table_ref = client.get_table(bq_table_name)
      job_config = bigquery.LoadJobConfig(write_disposition="WRITE_APPEND")
      job_config.autodetect = True

      insert_data = \
        client.load_table_from_dataframe(
          dataframe=pd.DataFrame(data), destination=table_ref)
      insert_data.result()

  except Exception as exception:
    logging.error("An exception occurred in [ingest_dataframe_to_bq]")
    logging.error("Exception occurred due to %s", str(exception))
    raise exception

  return "Success"


def truncate_table_data(bq_table_name):
  """
    This method will truncate the records
    from the provided table name.
    :param bq_table_name: BQ table name where data needs deleted
    """
  try:
    client = get_bq_client()
    truncate_query = \
      f"TRUNCATE TABLE `{bq_table_name}`"
    client.query(truncate_query).result()
    logging.info("All records has been deleted from"
                 "%s", str(bq_table_name))
  except Exception as exception:
    logging.error("Provided table name is = %s", str(bq_table_name))
    logging.error("An exception occurred in [truncate_table_data]")
    logging.error("Exception occurred due to %s", str(exception))
    raise exception



