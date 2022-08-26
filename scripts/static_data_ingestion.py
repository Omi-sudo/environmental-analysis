import logging
from google.cloud import bigquery
# import google.auth
import static_data_ingestion_config as config

logging.basicConfig(level=logging.INFO)

DEST_PROJECT_ID = "dec-cam-p-warehouse-d356"
SOURCE_PROJECT_ID = "gcp-environmental-analysis"


def get_bq_client():
  """
  This method will create a BigQuery client
  :return: This function will returns the client for the BigQuery
  """
  bq_client = None
  try:
    bq_client = bigquery.Client()
    print(bq_client)

  except Exception as exception:
    logging.error("An exception occurred in [get_bq_client]")
    logging.error("Exception occurred due to %s", str(exception))
    raise exception

  return bq_client


def execute_query(query):
  """
    This method will read data from a BigQuery.
    :return: This function will return the data in form of
    dataframe
    """
  try:
    client = get_bq_client()
    logging.info(f"Query String {query}")
    query = client.query(query)
    query.result()
    logging.info("data inserted successfully")

  except Exception as exception:
    logging.error("An exception occurred in "
                  "[read_data_from_bq]")
    logging.error("Exception occurred due to %s", str(exception))
    raise exception


def load_data_into_bq_tables():
  """
  This method will execute insert queries in ingestion & reporting dataset
  :return:
  """
  try:
    for tables in config.BQ_RAW_INGESTION_MAPPING:
      table_name = config.BQ_RAW_INGESTION_MAPPING[tables]["table_name"]
      query_string = f"TRUNCATE TABLE `{DEST_PROJECT_ID}.ingestion.{table_name}`"
      logging.info(f"TRUNACTE Data in `{DEST_PROJECT_ID}.ingestion.{table_name}`")
      execute_query(query=query_string)

    for tables in config.BQ_RAW_INGESTION_MAPPING:
      table_name = config.BQ_RAW_INGESTION_MAPPING[tables]["table_name"]
      query_string = config.BQ_RAW_INGESTION_MAPPING[tables]["query"]
      logging.info(f"Inserting Data in ingestion.{table_name}")
      execute_query(query=query_string)

    for tables in config.BQ_REPORTING_INGESTION_MAPPING:
      table_name = config.BQ_REPORTING_INGESTION_MAPPING[tables]["table_name"]
      query_string = f"TRUNCATE TABLE `{DEST_PROJECT_ID}.reporting.{table_name}`"
      logging.info(f"TRUNACTE Data in `{DEST_PROJECT_ID}.reporting.{table_name}`")
      execute_query(query=query_string)

    for tables in config.BQ_REPORTING_INGESTION_MAPPING:
      table_name = config.BQ_REPORTING_INGESTION_MAPPING[tables]["table_name"]
      query_string = config.BQ_REPORTING_INGESTION_MAPPING[tables]["query"]
      logging.info(f"Inserting Data in reporting.{table_name}")
      execute_query(query=query_string)

    for tables in config.AQS_MAPPING:
      table_name = config.AQS_MAPPING[tables]["table_name"]
      query_string = f"TRUNCATE TABLE `{DEST_PROJECT_ID}.reporting.{table_name}`"
      logging.info(f"TRUNACTE Data in `{DEST_PROJECT_ID}.reporting.{table_name}`")
      execute_query(query=query_string)

    for tables in config.AQS_MAPPING:
      table_name = config.AQS_MAPPING[tables]["table_name"]
      query_string = config.AQS_MAPPING[tables]["query"]
      logging.info(f"Inserting Data in reporting.{table_name}")
      execute_query(query=query_string)

  except Exception as exception:
    logging.error("An exception occurred in "
                  "[load_data_into_bq_tables]")
    logging.error("Exception occurred due to %s", str(exception))
    raise exception


if __name__ == '__main__':
  load_data_into_bq_tables()
