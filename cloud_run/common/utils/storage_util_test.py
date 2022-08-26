"""
storage_util_test.py
Test file for storage_util.py
"""
import unittest
from common.utils import storage_util

from common.constant import PROJECT_ID, E2E_BUCKET


class TestUploadDataOnGcsBucket(unittest.TestCase):
  """
  Test Function which will upload a dummy file on GCS
  """

  def test_upload_data_on_gcs_bucket(self):
    """
    Test Function which will check if the
    gcs_bucket is NONE or not
    """

    storage_util.upload_data_on_gcs_bucket(
      project_name=PROJECT_ID, gcs_bucket_name=E2E_BUCKET,
      gcs_file_path="storage_utils/test_cases_dummy.json",
      data="{'DUMMY_KEY':'DUMMY_VALUE'}")


class TestReadDataFromStorage(unittest.TestCase):
  """
  Test Function which will check if the function
  is able to read data from GCS bucket
  """

  def test_read_data_from_storage(self):
    """
    Test Function which will check if the
    gcs_bucket is NONE or not
    """

    self.assertIsNotNone(
      storage_util.read_data_from_storage(gcs_file_path="storage_utils/"
                                                        "gcp-environmental"
                                                        "-analysis."
                                                        "ingestion_"
                                                        "arcgis.major_"
                                                        "oil_storage_"
                                                        "facilities.json",
                                          gcs_bucket_name=E2E_BUCKET,
                                          file_type="json"))
    self.assertIsNotNone(
      storage_util.read_data_from_storage(gcs_file_path="storage_utils/"
                                                        "gcp-environmental"
                                                        "-analysis."
                                                        "ingestion_"
                                                        "arcgis.major_"
                                                        "oil_storage_"
                                                        "facilities.csv",
                                          gcs_bucket_name=E2E_BUCKET,
                                          file_type="CSV"))


class TestGetStorageBucket(unittest.TestCase):
  """
  Test Function which will check if the
  gcs_bucket client and bucket is NONE or not
  """

  def test_get_storage_bucket(self):
    """
    Test Function which will check if the
    gcs_bucket is NONE or not
    """

    self.assertIsNotNone(
      storage_util.get_storage_bucket(
        project_name=PROJECT_ID, bucket_name=E2E_BUCKET))


class TestGetStorageClient(unittest.TestCase):
  """
  Test Function which will check if the
  gcs_bucket client NONE or not
  """

  def test_get_storage_client(self):
    self.assertIsNotNone(
      storage_util.get_storage_client(
        project_name=PROJECT_ID))


if __name__ == "__main__":
  unittest.main()
