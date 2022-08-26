"""
bq_utils.py Module
This module contains all the functions needs to interact with BigQuery
"""
import logging
from datetime import datetime
from google.cloud import bigquery
import pandas as pd

from common import constant

logging.basicConfig(level=logging.INFO)

def format_batch_timestamp(batch_timestamp):
  """
  this method will format the string object of timestamp
  into datetime object
  param: batch_timestamp - string object of
  batch_timestamp

  return datetime object of batch_timestamp
  """
  try:
    batch_timestamp = datetime.strptime(
      batch_timestamp, constant.TIME_FORMAT,
    )
  except ValueError as value_error:
    raise ValueError(
      "value of batch_timestamp "
      f"is not in the format of {constant.TIME_FORMAT}") \
      from value_error

  return batch_timestamp

def get_bq_client():
  """
    This method will create a BigQuery client
    :return: This function will return the client for the BigQuery
    """
  bq_client = None
  try:
    bq_client = bigquery.Client(project=constant.PROJECT_ID)
  except Exception as exception:
    logging.error("An exception occurred in [get_bq_client]")
    logging.error("Exception occurred due to %s",str(exception))
    raise exception

  return bq_client


def ingest_dataframe_to_bq(data, bq_table_name):
  """
    This method will ingest the input dataframe
    into the specified BigQuery table
    :param data: input data rows to be ingested
    :param bq_table_name: BQ table name where data needs to be ingested
  """
  try:
    client = get_bq_client()
    table_ref = client.get_table(bq_table_name)
    job_config = bigquery.LoadJobConfig()
    job_config.autodetect = True

    insert_data = client.load_table_from_dataframe(
      dataframe=pd.DataFrame(data), destination=table_ref, job_config=job_config
    )

    insert_data.result()

  except Exception as exception:
    logging.error("An exception occurred in [ingest_dataframe_to_bq]")
    logging.error("Exception occurred due to %s",str(exception))
    raise exception



def execute_query(query, table_name):
  row_val = {}
  client = get_bq_client()
  logging.info("Executing Query : %s", str(query))
  query_job = client.query(query)
  if table_name == "job_audit":
    result = query_job.result()
    for rows in result:
      row_val["source_query_url"] = rows["source_query_url"]
      row_val["data_source_last_edit_date"] = rows["data_source_last_edit_date"]

  return row_val

def fetch_bq_table_schema(bq_table_name):
  """
    This method will fetch the table schema
    from specified BigQuery table
    :param bq_table_name: BigQuery table name
    :param return: List of column names of provided table
  """
  try:
    logging.info("Fetching %s's schema", str(bq_table_name))
    # establishing a bigquery client connection to fetch column of bq table
    client = get_bq_client()
    table_ref = client.get_table(bq_table_name)
    result = [f"{schema.name.lower()}" for schema in table_ref.schema]
    return result
  except Exception as exception:
    logging.error("An exception occurred while fetching schema!!!")
    logging.error("Failed to fetch schema due to %s", str(exception))
    raise exception

