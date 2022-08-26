"""
constant_test.py
Test file for constant.py
"""
import unittest

from common.constant import PORT, PROJECT_ID


class TestCheckConstantFile(unittest.TestCase):
  """
  Test which will check if the gcs_bucket name,
  project_id and port values are empty or not
  """

  def test_check_constant_file(self):
    self.assertIsNotNone(PROJECT_ID, msg=None)
    self.assertIsNotNone(PORT, msg=None)


if __name__ == "__main__":
  unittest.main()
