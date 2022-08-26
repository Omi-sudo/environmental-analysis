"""
bq_util_test.py
Test file for bq_util.py
"""
import unittest
import datetime
from common.utils import bq_utils
from common.constant import E2E_DATASET, PROJECT_ID

rows_to_insert = [{"data_source": "socrata",
                   "data_source_last_edit_date": datetime.datetime.now(),
                   "layer_name": "adult_care_facility",
                   "source_query_url": "https://data.cityofnewyork.us"
                                       "/resource/f7b6-v6v3",
                   "step_name": "raw_ingestion",
                   "destination": "warehouse",
                   "count": 1,
                   "batch_timestamp": datetime.datetime.now(),
                   "ingestion_timestamp": datetime.datetime.now(),
                   "status": "SUCCESS",
                   "message": None}]
execute_query = f"SELECT * FROM `{PROJECT_ID}.{E2E_DATASET}.job_audit` LIMIT 1"


class TestIngestDataframeToBq(unittest.TestCase):
  """
 this function will ingest a row in e2e_testing.audit_log
 table

  """

  def test_ingest_dataframe_to_bq(self):
    bq_utils.ingest_dataframe_to_bq(data=rows_to_insert,
                                    bq_table_name=
                                    f"{E2E_DATASET}.job_audit_test_cov")


class TestExecuteQuery(unittest.TestCase):
  """
  Test which will fetch the BQ table schema

  """

  def test_execute_query(self):
    self.assertIsNotNone(bq_utils.execute_query(
      query=execute_query,
      table_name="job_audit"))
    self.assertIsInstance(bq_utils.execute_query(
      query=execute_query,
      table_name="job_audit"), dict)


class TestFetchBqTableSchema(unittest.TestCase):
  """
  Test which will fetch the BQ table schema

  """

  def test_fetch_bq_table_schema(self):
    self.assertIsNotNone(bq_utils.fetch_bq_table_schema(
      bq_table_name=E2E_DATASET + "." + "job_audit"))
    self.assertIsInstance(bq_utils.fetch_bq_table_schema(
      bq_table_name=E2E_DATASET + "." + "job_audit"), list)


class TestGetBqClient(unittest.TestCase):
  """
  Test which will check if the bq_client is None or not
  """

  def test_get_bq_client(self):
    self.assertIsNotNone(bq_utils.get_bq_client())


if __name__ == "__main__":
  unittest.main()
