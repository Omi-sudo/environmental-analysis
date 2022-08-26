"""
Test file for the socrata_socrata_parsing_util.py
"""

import unittest
from common.utils import socrata_parsing_sample_data_test
from common.utils import socrata_parsing_util


class TestCheckParseHumanAddressDataReturnType(unittest.TestCase):
  """
      Test which will check if the return type of parsed object is of string or
      not.
  """
  def test_check_parse_human_address_data_return_type_is_string(self):
    self.assertIsInstance(socrata_parsing_util.parse_human_address_data(
      socrata_parsing_sample_data_test.human_address_data),
      str)


class TestCheckParseMutlipolygonDataReturnType(unittest.TestCase):
  """
      Test which will check if the retrun type of parsed object is of string or
      not.
  """
  def test_check_parse_mutlipolygon_data_return_type_is_string(self):
    self.assertIsInstance\
        (socrata_parsing_util.parse_geometry_coordinates_mutlipolygon_data
      (
      socrata_parsing_sample_data_test.multipolygon_data),
      str)


class TestCheckParsePointDataReturnType(unittest.TestCase):
  """
      Test which will check if the retrun type of parsed object is of string or
      not.
  """
  def test_check_parse_point_data_return_type_is_string(self):
    self.assertIsInstance(
      socrata_parsing_util.parse_geometry_coordinates_point_data
      (socrata_parsing_sample_data_test.point_data), str)


if __name__ == "__main__":
  unittest.main()
