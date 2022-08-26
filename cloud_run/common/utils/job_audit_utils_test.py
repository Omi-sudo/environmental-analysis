"""
job_audit_utils_test.py
Test file for job_audit_utils_test.py
"""
import datetime
import unittest
from common.utils import job_audit_utils
from common.constant import E2E_DATASET, PROJECT_ID

execute_query = f"SELECT * FROM `{PROJECT_ID}.{E2E_DATASET}.job_audit` LIMIT 1"


class TestGetBqClient(unittest.TestCase):
  """
  Test which will check if the bq_client is None or not
  """

  def test_get_bq_client(self):
    job_audit_utils.get_insert_audit_rows(data_source="socrata",
                                          data_source_last_edit_date=
                                          datetime.datetime.now(),
                                          layer_name=
                                          "adult_care_facility",
                                          source_query_url=
                                          "https://data.cityofnewyork.us"
                                          "/resource/f7b6-v6v3",
                                          task_name=
                                          "raw_ingestion",
                                          destination=
                                          "warehouse",
                                          count=1,
                                          status="SUCCESS",
                                          bq_table_name=
                                           f"{E2E_DATASET}."
                                           "job_audit_test_cov")


if __name__ == "__main__":
  unittest.main()
