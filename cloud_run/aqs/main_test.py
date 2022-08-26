"""
main_test.py module
Unit test cases for the main.py
"""
import unittest
from datetime import datetime, date

from aqs.main import fetch_data_from_aqs_api, \
  fetch_aqs_api_last_edit_date, split_and_format_data_layer_name, \
  fetch_config_info, get_first_last_date, prep_bdate_edate

from aqs import sample_test_data
from common import constant

DATA_LAYER_URL = "https://aqs.epa.gov/data/api/sampleData/byState?email=" \
                 + constant.AQS_EMAIL \
                 + "&key=" + constant.AQS_KEY + \
                 "&param=42101&bdate={}&edate={}&state=36"


class TestPrepBdateEdate(unittest.TestCase):
  """
    This function will test prep_bdate_edate
  """

  def test_prep_bdate_edate(self):
    self.assertIsInstance(
      prep_bdate_edate(year="2021",
                       month="11",
                       lookup_month="5"),
      list)

    self.assertEqual(
      len(prep_bdate_edate(year="2021",
                           month="11",
                           lookup_month="5")),
      1)

    self.assertEqual(
      len(prep_bdate_edate(year="2021",
                           month="11",
                           lookup_month="5")[0]),
      2)

    self.assertIsInstance(
      prep_bdate_edate(year=str(date.today().year),
                       month="11",
                       lookup_month="5"),
      list)

    self.assertEqual(
      len(prep_bdate_edate(year=str(date.today().year),
                           month="11",
                           lookup_month="5")),
      5)

    self.assertEqual(
      len(prep_bdate_edate(year=str(date.today().year), month="11"
                           , lookup_month="5")[0]),
      2)


class TestGetFirstLastDate(unittest.TestCase):
  """
    This function will test get_first_last_date
  """

  def test_get_first_last_date(self):
    self.assertIsInstance(
      get_first_last_date(year="2021", month="11"), dict)

    self.assertEqual(
      len(get_first_last_date(year="2021",
                              month="11")), 2)

    self.assertIsInstance(
      get_first_last_date(year="2021", month="11")["bdate"]
      , str)

    self.assertEqual(
      len(get_first_last_date(year="2021", month="11")["bdate"])
      , 8)

    self.assertIsInstance(
      get_first_last_date(year="2021", month="11")["edate"]
      , str)

    self.assertEqual(
      len(get_first_last_date(year="2021", month="11")["edate"])
      , 8)


class TestSplitAndFormatDataLayerName(unittest.TestCase):
  """
    This function will check test split_and_format_data_layer_name
  """

  def test_split_and_format_data_layer_name(self):
    self.assertIsInstance(
      split_and_format_data_layer_name("carbon_monoxide"), list)

    self.assertEqual(
      any(itr.islower() for itr in split_and_format_data_layer_name(
        "carbon_monoxide")), True)

    self.assertGreater(
      len(split_and_format_data_layer_name(
        "carbon_monoxide")), 0)


class TestFetchDataFromAqsApi(unittest.TestCase):
  """
  This function will test fetch_data_from_aqs_api
  """

  def test_fetch_data_from_aqs_api(self):
    self.assertIsInstance(
      fetch_data_from_aqs_api(
        layer_url=DATA_LAYER_URL,
        data_date_ranges=[{"bdate": "20210515",
                           "edate": "20210515"}]), list)

    self.assertEqual(
      all(isinstance(itr, dict)
          for itr in
          fetch_data_from_aqs_api(
            layer_url=DATA_LAYER_URL,
            data_date_ranges=[{"bdate": "20210515", "edate": "20210515"}])),
      False)


class TestFetchFeatureLayerLastEditDate(unittest.TestCase):
  """
    This function will check the return type of element
    in returned list in fetch_aqs_api_last_edit_date function
    is datetime  date object or not,
    checks the length of return data = 2,
    also checks the returned type of
    the data is list or not.
  """

  def test_fetch_aqs_api_last_edit_date(self):
    self.assertIsInstance(
      fetch_aqs_api_last_edit_date(
        data=sample_test_data.data)[0], datetime)

    self.assertIsInstance(
      fetch_aqs_api_last_edit_date(
        data=sample_test_data.data)[1], date)

    self.assertIsInstance(
      fetch_aqs_api_last_edit_date(
        data=sample_test_data.data), list)

    self.assertEqual(
      len(fetch_aqs_api_last_edit_date(
        data=sample_test_data.data)), 2)


class TestFetchRawDataConfigInfo(unittest.TestCase):
  """
    This function will check the return type of
    test_fetch_config_info is dictionary or not
    and checks length of the return data.
  """

  def test_fetch_config_info(self):
    self.assertIsInstance(
      fetch_config_info(batch_unix_timestamp=1654856052,
                        data_layer_name="carbon_monoxide",
                        data_processing_type="raw",
                        raw_gcs_ingestion_date=None), dict)

    self.assertEqual(len(fetch_config_info(batch_unix_timestamp=1654856052,
                                           data_layer_name="carbon_monoxide",
                                           data_processing_type="raw",
                                           raw_gcs_ingestion_date=None)), 4)

    self.assertIsInstance(fetch_config_info
                          (batch_unix_timestamp=1654856052,
                           data_layer_name="carbon_monoxide",
                           data_processing_type="parse",
                           raw_gcs_ingestion_date="2022-05-01"), dict)

    self.assertEqual(
      len(fetch_config_info(batch_unix_timestamp=1654856052,
                            data_layer_name="carbon_monoxide",
                            data_processing_type="parse",
                            raw_gcs_ingestion_date="2022-05-01")), 5)
