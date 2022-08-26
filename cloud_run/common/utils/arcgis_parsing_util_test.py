"""
socrata_arcgis_parsing_util_test.py
Test file for arcgis_apis api
"""
import unittest
from common.utils import arcgis_parsing_util
from common.utils import arcgis_parsing_sample_data_test


class TestCheckGeometryDataParsingReturnType(unittest.TestCase):
  """
  Test which will check if the return type of
  parsed object is of string or not.
  """
  def test_check_geometry_data_parsing_return_type_is_string(self):
    self.assertIsInstance(arcgis_parsing_util.parse_geometry_data
                          (arcgis_parsing_sample_data_test.geometry_data), str)


class TestCheckGeometryRingsDataParsingReturnType(unittest.TestCase):
  def test_check_geometry_rings_data_parsing_return_type_is_string(self):
    """
    Test which will check if the return type of
    parsed object is of string
    or not.
    """

    self.assertIsInstance(
      arcgis_parsing_util.parse_geometry_rings_data(
        arcgis_parsing_sample_data_test.geometry_rings_data), str
    )


if __name__ == "__main__":
  unittest.main()
