"""
main_test.py module
Unit test cases for the main.py
"""

import unittest
from datetime import datetime

from ftp import main
from ftp import sample_test_data
from common import constant
from common.utils import bq_utils


def delete_records_from_bq(bq_table_name, project_id):
  """
  This method will delete the records in
  BigQuery table based on query
  """

  if "job_audit" in bq_table_name:
    client = bq_utils.get_bq_client()
    query_string = f"""
    DELETE {project_id}.{bq_table_name} WHERE destination="e2e_testing.airnow_i_e2e"
    """
  else:
    client = bq_utils.get_bq_client()
    query_string = f"""
        TRUNCATE TABLE {project_id}.{bq_table_name}
        """
  print(query_string)
  client.query(query_string).result()


class TestFetchFileListFromBucket(unittest.TestCase):
  """
        This function will check the return type of
        split_and_format_data_layer_name is list or not,
        also checks the value in small
        letters or not as well as value is not empty.
  """

  def test_fetch_filelist_from_bucket(self):
    self.assertIsInstance(main.fetch_filelist_from_bucket(
      bucket_name=constant.E2E_BUCKET), list)


class TestReadCsvAndIngestIntoBq(unittest.TestCase):
  """
        This function will check the return type of
        split_and_format_data_layer_name is list or not,
        also checks the value in small
        letters or not as well as value is not empty.
  """

  def test_read_csv_and_ingest_into_bq(self):
    self.assertIsInstance(
      main.read_csv_and_ingest_into_bq(data=sample_test_data.data,
                                       table_name=sample_test_data.table_name,
                                       file=sample_test_data.file_name,
                                       schema=sample_test_data.schema,
                                       batch_timestamp=datetime.now(),
                                       record_date=datetime.now().date()), str)

    delete_records_from_bq(project_id=constant.PROJECT_ID,
                           bq_table_name=constant.BQ_METADATA_DATASET
                                         +"."+constant.JOB_LOGGING_TABLE)

    delete_records_from_bq(project_id=constant.PROJECT_ID,
                           bq_table_name=sample_test_data.table_name)
