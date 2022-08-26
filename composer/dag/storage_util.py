"""
storage_util.py Module
"""
import sys
import json
import logging

from google.cloud import storage

import constants

logging.basicConfig(level=logging.INFO)


def get_storage_client(project_name):
  """
  Returns the client for the Google Cloud storage
  :param project_name: the name of the project
  :returns: the client object or None otherwise
  """
  client = None
  try:
    client = storage.Client(project=project_name)

  except Exception as exception:
    logging.error("An exception occurred in [get_storage_client]")
    logging.error("Exception occurred due to %s", str(exception))
    sys.exc_info()
    raise exception

  return client


def get_storage_bucket(project_name, bucket_name):
  """
  Returns the storage bucket object for a project
  name and bucket name

  :param project_name: the project name
  :param bucket_name: the name of the bucket
  :returns: the storage bucket object
  """
  bucket = None
  try:
    client = get_storage_client(project_name)
    bucket = client.get_bucket(bucket_name)

  except Exception as exception:
    logging.error("Provided project name = %s and bucket name is"
                 " = %s ", str(project_name), str(bucket_name))
    logging.error("An exception occurred in [get_storage_bucket]")
    logging.error("Exception occurred due to %s", str(exception))
    logging.info("Provided project name = %s and bucket name is"
                 " = %s ", str(project_name), str(bucket_name))
    sys.exc_info()
    raise exception

  return bucket


def upload_data_on_gcs_bucket(project_name, gcs_bucket_name, gcs_file_path,
                              data):
  """

  This function will upload the data on the specified GCS location

  :param data:  Data fetched from NYS-DEC webservices
  :param gcs_file_path : GCS location where data needs to be uploaded
  :param gcs_bucket_name: Google Cloud Storage
  bucket name where the file needs to be upload
  :param project_name: Google Cloud project_id
  """

  try:
    bucket = get_storage_bucket(
      project_name=project_name, bucket_name=gcs_bucket_name
    )
    blob = bucket.blob(gcs_file_path)
    blob.upload_from_string(data=data, content_type="application/octet-stream")
    logging.info(
      "[upload_data_on_gcs_bucket] - Data successfully uploaded at gs://%s/%s"
      , gcs_bucket_name, gcs_file_path
    )

  except Exception as exception:
    logging.error("An exception occurred in [upload_data_on_gcs_bucket]")
    logging.error("Exception occurred due to %s", str(exception))
    sys.exc_info()
    raise exception


def read_data_from_storage(gcs_file_path, gcs_bucket_name):
  """
  This Function will read the files from GCS
  :param gcs_file_path: GCS object path/location which
  needs to be ingest into BigQuery tables
  :param gcs_bucket_name: GCS bucket name.
  :return: file/data residing on the GCS bucket
  """
  try:

    bucket = get_storage_bucket(constants.PROJECT_ID, gcs_bucket_name)
    blob = bucket.get_blob(gcs_file_path)
    downloaded_blob = json.loads(blob.download_as_text())
    return downloaded_blob

  except Exception as exception:
    logging.error("An exception occurred in [read_data_from_storage]")
    logging.error("Exception occurred due to %s", str(exception))
    sys.exc_info()
    raise exception
