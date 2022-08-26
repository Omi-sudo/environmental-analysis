"""
main_test.py module
Unit test cases for the main.py
"""

import unittest
from datetime import datetime, date
import json

from arcgis_apis import main
from common.utils import arcgis_parsing_sample_data_test

DATA_LAYER_URL = "https://services6.arcgis.com/DZHaqZm9cxOD4CWM" \
                 "/ArcGIS/rest/services/Major_Oil_Storage_Facility" \
                 "/FeatureServer/0"


class TestSplitAndFormatDataLayerName(unittest.TestCase):
  """
        This function will check the return type of
        split_and_format_data_layer_name is list or not,
        also checks the value in small
        letters or not as well as value is not empty.
  """

  def test_split_and_format_data_layer_name(self):
    self.assertIsInstance(
      main.split_and_format_data_layer_name("nursing_homes"), list)

    self.assertEqual(
      any(itr.islower() for itr in main.split_and_format_data_layer_name
      ("nursing_homes")), True)

    self.assertGreater(
      len(main.split_and_format_data_layer_name("nursing_homes")), 0)


class TestAddRecordDateInParsedData(unittest.TestCase):
  """
    This function will check the return type of
    add_record_date_in_parsed_data is list or not,
    also checks the record_date is present or not.
  """

  def test_add_record_date_in_parsed_data(self):
    self.assertIsInstance(
      main.add_record_date_in_parsed_data(
        parsed_data=json.dumps(arcgis_parsing_sample_data_test.parsed_data),
        layer_last_edit_info=
        main.fetch_feature_layer_last_edit_date(DATA_LAYER_URL)), list)

    self.assertEqual(
      all(isinstance(itr, dict)
          for itr in
          main.add_record_date_in_parsed_data(
            parsed_data=json.dumps(arcgis_parsing_sample_data_test.parsed_data),
            layer_last_edit_info=
            main.fetch_feature_layer_last_edit_date(DATA_LAYER_URL))),
      True)

    self.assertEqual(
      any("record_date" in itr for itr in
          main.add_record_date_in_parsed_data(
            parsed_data=
            json.dumps(arcgis_parsing_sample_data_test.parsed_data),
            layer_last_edit_info=
            main.fetch_feature_layer_last_edit_date(DATA_LAYER_URL))),
      True)


class TestPrepareParseData(unittest.TestCase):
  """
  This function will check the return type of
  prepare_parse_data is string or not
  for each parsing type.
  """

  def test_prepare_parse_data(self):
    self.assertIsInstance(
      main.prepare_parse_data(
        data=json.dumps(arcgis_parsing_sample_data_test.geometry_data),
        parsing_type="geometry_data"), str)

    self.assertIsInstance(
      main.prepare_parse_data(
        data=json.dumps(arcgis_parsing_sample_data_test.geometry_rings_data),
        parsing_type="geometry_rings_data"), str)

    self.assertIsInstance(
      main.prepare_parse_data(
        data=json.dumps(arcgis_parsing_sample_data_test.geometry_data),
        parsing_type="no_parsing"), str)


class TestFetchRawDataConfigInfo(unittest.TestCase):
  """
  This function will check the return type of
  fetch_config_info is dictionary or not
  and checks length of the return data = 5
  """

  def test_fetch_config_info(self):
    self.assertIsInstance(
      main.fetch_config_info(batch_unix_timestamp=1654856052,
                             data_layer_name="nursing_homes",
                             data_processing_type="raw",
                             raw_gcs_ingestion_date=None), dict)

    self.assertEqual(len(main.fetch_config_info(batch_unix_timestamp=1654856052,
                                                data_layer_name="nursing_homes",
                                                data_processing_type="raw",
                                                raw_gcs_ingestion_date
                                                =None)), 5)

    self.assertIsInstance(main.fetch_config_info
                          (batch_unix_timestamp=1654856052,
                           data_layer_name="nursing_homes",
                           data_processing_type="parse",
                           raw_gcs_ingestion_date="2022-05-01"), dict)

    self.assertEqual(
      len(main.fetch_config_info(batch_unix_timestamp=1654856052,
                                 data_layer_name="nursing_homes",
                                 data_processing_type="parse",
                                 raw_gcs_ingestion_date="2022-05-01")), 8)


class TestFetchDataFromSource(unittest.TestCase):
  """
    This function will check the return type of
    fetch_data_from_source
    is string or not.
    also checks the data type of function is
    list of not after performing json.loads
  """

  def test_fetch_data_from_source(self):
    self.assertIsInstance(
      main.fetch_data_from_source(layer_url_endpoint=DATA_LAYER_URL,
                                  layer_last_edit_info=
                                  main.fetch_feature_layer_last_edit_date
                                  (DATA_LAYER_URL)), str)

    self.assertIsInstance(json.loads(
      main.fetch_data_from_source(layer_url_endpoint=DATA_LAYER_URL,
                                  layer_last_edit_info=
                                  main.fetch_feature_layer_last_edit_date
                                  (DATA_LAYER_URL))), dict)

    self.assertIsInstance(
      json.loads(main.fetch_data_from_source(
        layer_url_endpoint=DATA_LAYER_URL,
        layer_last_edit_info=main.fetch_feature_layer_last_edit_date
                                             (DATA_LAYER_URL)))
      ["features"], list)


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
      main.fetch_feature_layer_last_edit_date(DATA_LAYER_URL), list
    )

    self.assertEqual(
      len(main.fetch_feature_layer_last_edit_date(DATA_LAYER_URL)), 2
    )

    self.assertIsInstance(
      main.fetch_feature_layer_last_edit_date(DATA_LAYER_URL)[0], datetime
    )

    self.assertIsInstance(
      main.fetch_feature_layer_last_edit_date(DATA_LAYER_URL)[1], date
    )
