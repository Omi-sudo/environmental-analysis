"""
config_test.py
Test file for config.py
"""
import unittest
from common import config


class TestCheckLengthOfConfigFile(unittest.TestCase):
  """
  Test which will check whether config file is empty or not.
  """

  def test_check_length_of_config_file(self):
    self.assertGreater(
      len(config.arcgis_data_layer_and_gcp_mapping), 0)
    self.assertGreater(
      len(config.socrata_data_layer_and_gcp_mapping), 0)
    self.assertGreater(
      len(config.aqs_api_data_layer_and_gcp_mapping), 0)


class TestCheckConfigFile(unittest.TestCase):
  """
  Test which will check if the config values are empty or not
  """

  def test_check_config_file(self):

    for layer in config.arcgis_data_layer_and_gcp_mapping:
      data_source = \
        config.arcgis_data_layer_and_gcp_mapping[layer]["data_source"]
      parsing_type = \
        config.arcgis_data_layer_and_gcp_mapping[layer]["parsing_type"]
      layer_name = \
        config.arcgis_data_layer_and_gcp_mapping[layer]["layer_name"]
      layer_url = \
        config.arcgis_data_layer_and_gcp_mapping[layer]["layer_url"]
      parsed_gcs_file_path = \
        config.arcgis_data_layer_and_gcp_mapping[layer][
        "parsed_gcs_file_uri"
      ]
      raw_gcs_file_path = \
        config.arcgis_data_layer_and_gcp_mapping[layer][
        "raw_gcs_file_uri"
      ]

      self.assertIsNotNone(data_source)
      self.assertIsNotNone(parsing_type)
      self.assertIsNotNone(layer_name)
      self.assertIsNotNone(layer_url)
      self.assertIsNotNone(parsed_gcs_file_path)
      self.assertIsNotNone(raw_gcs_file_path)

    for layer in config.socrata_data_layer_and_gcp_mapping:
      data_source = \
        config.socrata_data_layer_and_gcp_mapping[layer]["data_source"]
      layer_name = \
        config.socrata_data_layer_and_gcp_mapping[layer]["layer_name"]
      url = \
        config.socrata_data_layer_and_gcp_mapping[layer]["url"]
      parsed_gcs_file_path = \
        config.socrata_data_layer_and_gcp_mapping[layer]["parsed_gcs_file_uri"]
      raw_gcs_file_path = \
        config.socrata_data_layer_and_gcp_mapping[layer][
          "raw_gcs_file_uri"
        ]
      domain_name = \
        config.socrata_data_layer_and_gcp_mapping[layer]["domain_name"]
      dataset_name = \
        config.socrata_data_layer_and_gcp_mapping[layer]["dataset_name"]

      parsing_type = \
        config.socrata_data_layer_and_gcp_mapping[layer]["parsing_type"]

      title = \
        config.socrata_data_layer_and_gcp_mapping[layer]["title"]

      self.assertIsNotNone(data_source)
      self.assertIsNotNone(layer_name)
      self.assertIsNotNone(url)
      self.assertIsNotNone(parsed_gcs_file_path)
      self.assertIsNotNone(raw_gcs_file_path)
      self.assertIsNotNone(domain_name)
      self.assertIsNotNone(dataset_name)
      self.assertIsNotNone(parsing_type)
      self.assertIsNotNone(title)

    for layer in config.aqs_api_data_layer_and_gcp_mapping:
      data_source = \
        config.aqs_api_data_layer_and_gcp_mapping[layer]["data_source"]
      param = \
        config.aqs_api_data_layer_and_gcp_mapping[layer]["param"]
      layer_name = \
        config.aqs_api_data_layer_and_gcp_mapping[layer]["layer_name"]
      layer_url = \
        config.aqs_api_data_layer_and_gcp_mapping[layer]["layer_url"]
      parsed_gcs_file_path = \
        config.aqs_api_data_layer_and_gcp_mapping[layer]["parsed_gcs_file_uri"]
      raw_gcs_file_path = \
        config.aqs_api_data_layer_and_gcp_mapping[layer][
          "raw_gcs_file_uri"
        ]

      self.assertIsNotNone(data_source)
      self.assertIsNotNone(param)
      self.assertIsNotNone(layer_name)
      self.assertIsNotNone(layer_url)
      self.assertIsNotNone(parsed_gcs_file_path)
      self.assertIsNotNone(raw_gcs_file_path)


if __name__ == "__main__":
  unittest.main()
