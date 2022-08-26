"""
main_test.py module
Unit test cases for the main.py
"""
import unittest
from datetime import datetime
import json

from socrata.main import fetch_data_layer_last_edit_date,\
  fetch_data_from_source, fetch_config_info, prepare_parse_data, \
  add_record_date_in_parsed_data, split_and_format_data_layer_name
from common.utils import socrata_parsing_sample_data_test


DATA_LAYER_URL = \
    "https://health.data.ny.gov/resource/6wkx-ptu4.json?$select=count(*)"
DOMAIN_NAME = "health.data.ny.gov"
DATASET_NAME = "6wkx-ptu4"

class TestSplitAndFormatDataLayerName(unittest.TestCase):
  """
    This function will check the return type of
    split_and_format_data_layer_name is list or not,
    also checks the value in small
    letters or not as well as value is not empty.
  """
  def test_split_and_format_data_layer_name(self):
    self.assertIsInstance(
        split_and_format_data_layer_name(
            "adult_care_facility_map"), list)

    self.assertEqual(
        any(itr.islower() for itr in split_and_format_data_layer_name(
            "adult_care_facility_map")), True)

    self.assertGreater(
        len(split_and_format_data_layer_name(
            "adult_care_facility_map")), 0)


class TestAddRecordDateInParsedData(unittest.TestCase):
  """
    This function will check the return type of
    add_record_date_in_parsed_data is list or not,
    also checks the record_date is present or not.
  """
  def test_add_record_date_in_parsed_data(self):
    self.assertIsInstance(
        add_record_date_in_parsed_data(
            parsed_data=
            json.dumps(socrata_parsing_sample_data_test.human_address_data),
            layer_last_modified_info=
            fetch_data_layer_last_edit_date(DATA_LAYER_URL)), list)

    self.assertEqual(
      all(isinstance(itr, dict)
      for itr in
      add_record_date_in_parsed_data(
          parsed_data=
          json.dumps(socrata_parsing_sample_data_test.human_address_data),
          layer_last_modified_info=
          fetch_data_layer_last_edit_date(DATA_LAYER_URL))), True)

    self.assertEqual(
        any("record_date" in itr for itr in
          add_record_date_in_parsed_data(
              parsed_data=
              json.dumps(socrata_parsing_sample_data_test.human_address_data),
              layer_last_modified_info=
              fetch_data_layer_last_edit_date(DATA_LAYER_URL))), True)


class TestPrepareParseData(unittest.TestCase):
  """
  This function will check the return type of
  prepare_parse_data is string or not
  for each parsing type.
  """
  def test_prepare_parse_data(self):
    self.assertIsInstance(
        prepare_parse_data(
            data=
            json.dumps(socrata_parsing_sample_data_test.human_address_data),
            parsing_type="human_address_data"), str)

    self.assertIsInstance(
      prepare_parse_data(
          data=json.dumps(socrata_parsing_sample_data_test.multipolygon_data),
          parsing_type="multipolygon_data"), str)

    self.assertIsInstance(
      prepare_parse_data(
          data=json.dumps(socrata_parsing_sample_data_test.point_data),
          parsing_type="point_data"), str)


class TestFetchRawDataConfigInfo(unittest.TestCase):
  """
    This function will check the return type of
    fetch_config_info is dictionary or not
    and checks length of the return data = 7
  """
  def test_fetch_config_info(self):
    self.assertIsInstance(
        fetch_config_info(batch_unix_timestamp=1654856052,
                          data_layer_name="adult_care_facility_map",
                          data_processing_type="raw",
                          raw_gcs_ingestion_date=None), dict)


    self.assertEqual(len(fetch_config_info(
        batch_unix_timestamp=1654856052,
        data_layer_name="adult_care_facility_map",
        data_processing_type="raw",
        raw_gcs_ingestion_date=None)), 7)

    self.assertIsInstance(fetch_config_info(batch_unix_timestamp=
                                            1654856052,
                                            data_layer_name=
                                            "adult_care_facility_map",
                                            data_processing_type=
                                            "parse",
                                            raw_gcs_ingestion_date=
                                            "2022-05-01"),dict)

    self.assertEqual(
      len(fetch_config_info(batch_unix_timestamp=1654856052,
                            data_layer_name="adult_care_facility_map",
                            data_processing_type="parse",
                            raw_gcs_ingestion_date="2022-05-01")), 7)


class TestFetchDataFromSource(unittest.TestCase):
  """
  This function will check the return type of
  fetch_data_from_source
  is string or not
  also checks the data type of function is
  list of not after performing json.loads
  """

  def test_fetch_data_from_source(self):
    self.assertIsInstance(
      fetch_data_from_source(url=DATA_LAYER_URL, domain_name=DOMAIN_NAME,
                             dataset_name=DATASET_NAME), str
    )

    self.assertIsInstance(json.loads(
      fetch_data_from_source(url=DATA_LAYER_URL, domain_name=DOMAIN_NAME,
                             dataset_name=DATASET_NAME)), list
    )

    self.assertEqual(all(isinstance(itr, dict) for itr in json.loads(
      fetch_data_from_source(url=DATA_LAYER_URL, domain_name=DOMAIN_NAME,
                             dataset_name=DATASET_NAME))), True
    )


class TestFetchFeatureLayerLastEditDate(unittest.TestCase):
  """
    This function will check the return type of
    check_fetch_feature_layer_last_edit_date
    is list or not, checks length of the return
    data = 2, also check return data values are date
    and datetime object.
  """

  def test_check_fetch_feature_layer_last_edit_date(self):
    self.assertIsInstance(
      fetch_data_layer_last_edit_date(DATA_LAYER_URL), list
    )

    self.assertEqual(
      len(fetch_data_layer_last_edit_date(DATA_LAYER_URL)), 2
    )

    self.assertIsInstance(
      fetch_data_layer_last_edit_date(DATA_LAYER_URL)[0], datetime
    )

    self.assertIsInstance(
      fetch_data_layer_last_edit_date(DATA_LAYER_URL)[1], str
    )
