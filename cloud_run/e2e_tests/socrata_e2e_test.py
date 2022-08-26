"""
socrata_e2e_test.py
Python module for SOCRATA e2e test
"""

import requests as request
import subprocess
import logging
from datetime import datetime

import google.auth
import google.auth.transport.requests
import google.oauth2.id_token
from google.cloud import bigquery

from common.utils import storage_util, bq_utils
from common import constant


logging.basicConfig(level=logging.INFO)


GCS_FILE_PATH = f"parsed/adult_care_facility_map/" \
                f"{constant.CURRENT_DATE}/" \
                f"adult_care_facility_map_1654856052.json"
BQ_TABLE_NAME = f"{constant.E2E_DATASET}." \
                f"socrata_adult_care_facility_map_e2e"
table_name = constant.BQ_METADATA_DATASET + "." + constant.JOB_LOGGING_TABLE


def delete_gcs_object():
  """
  This method deletes the files from gcs bucket
  """

  logging.info("Deleting object raw folder in GCS bucket")
  with subprocess.Popen(f"gsutil rm gs://{constant.E2E_BUCKET}/"
                        f"raw/"
                        f"adult_care_facility_map/"
                        f"{constant.CURRENT_DATE}/"
                        "adult_care_facility_map_1654856052.json",
                        shell=True) as process:
    process.wait()
  logging.info("return code is %s", str(process.returncode))
  if process.returncode != 0:
    raise ValueError(
      f"Request failed due to "
      f"the response code {process.returncode}"
    )
  logging.info("Object deleted successfully from "
               "raw folder in GCS bucket")

  logging.info("Deleting object from parsed "
               "folder in GCS bucket ")

  with subprocess.Popen(f"gsutil rm gs://{constant.E2E_BUCKET}/"
                        f"parsed/"
                        f"adult_care_facility_map/"
                        f"{constant.CURRENT_DATE}/"
                        "adult_care_facility_map_1654856052.json",
                        shell=True) as process:
    process.wait()
  logging.info("return code is %s", str(process.returncode))
  if process.returncode != 0:
    raise ValueError(
      f"Request failed due to "
      f"the response code {process.returncode}"
    )
  logging.info("Object deleted successfully from "
               "parsed folder in GCS bucket")


def authenticate_and_trigger_cloud_run(url_info):
  """
  This method will authenticate into
  the cloud run and trigger it.
  :param url_info: cloud run service url.
  :return: Trigger the respective cloud run service.
  """
  logging.info("Printing url_info :%s", url_info)
  auth_req = google.auth.transport.requests.Request()
  logging.info("url: %s", str(url_info[0]))
  raw_cloud_run_url = url_info[0] + "/process_raw_layer?" \
                                    "layer_name=" \
                                    "adult_care_facility_map&" \
                                    "batch_timestamp=" \
                                    "2021-06-10 10:14:12.700268&" \
                                    "batch_unix_timestamp=" \
                                    "1654856052&" \
                                    f"bucket={constant.E2E_BUCKET}"

  parsed_cloud_run_url = url_info[0] + "/process_parse_layer?layer_name=" \
                                       "adult_care_facility_map&" \
                                       f"raw_gcs_ingestion_date=" \
                                       f"{constant.CURRENT_DATE}&" \
                                       "batch_timestamp=" \
                                       "2021-06-10 10:14:12.700268&" \
                                       "batch_unix_timestamp=1654856052&" \
                                       f"bucket={constant.E2E_BUCKET}"

  url_list = [raw_cloud_run_url, parsed_cloud_run_url]


  for url in url_list:
    logging.info("service_endpoint: %s", str(url))
    id_token = google.oauth2.id_token.fetch_id_token(auth_req, url)

    headers = {
      "Authorization": "Bearer " + id_token,
      "Content-Type": "application/json; charset=utf-8",
    }


    response = request.get(
      url,
      headers=headers,
    )
    logging.info(response.content.decode("UTF-8"))
    logging.info("status code: %s", str(response.status_code))
    if response.status_code != 200:
      raise ValueError(
        f"Request failed due to "
        f"the response code {response.status_code}"
      )


def fetch_cloud_run_endpoint():
  """
  "This method fetch the cloud run url and service endpoint
  :param url_info: cloud run service url.
  :return: List of cloud run url and service endpoint"
  """

  output = \
    subprocess.check_output("gcloud run services list", shell=True)

  data = str(output.decode("utf-8")).split(" ")
  for itr in data:
    if "https://socrata-e2e-testing" in itr:
      return [itr.rstrip("LAST").strip(), itr.rstrip(
        "LAST").strip()]


def get_bq_client():
  """
    This method will create a BigQuery client.
    :return: This function will returns the client for the BigQuery
    """
  bq_client = None
  try:
    bq_client = bigquery.Client(constant.PROJECT_ID)
  except Exception as exception:
    logging.error("An exception occurred in [get_bq_client]")
    logging.error("Exception occurred due to %s", str(exception))
    raise exception

  return bq_client


def delete_records_from_bq(bq_table_name, project_id):
  """
  This method will delete the records in
  BigQuery table based on query
  """

  client = get_bq_client()
  if "job_audit" in bq_table_name:
    query_string = f"""
    DELETE {project_id}.{bq_table_name} WHERE batch_timestamp=
    "2021-06-11 10:14:12.700268"
    """
  else:
  # Download query results.
    query_string = f"""
    TRUNCATE TABLE {project_id}.{bq_table_name}
        """
  logging.info("Query string %s", str(query_string))
  client.query(query_string).result()

def delete_cloud_run_service():

  "This method deletes the created cloud run service"
  with subprocess.Popen("gcloud run services delete "
                        "socrata-e2e-testing "
                        "--region=us-east4 --quiet",
                        shell=True) as process:
    process.wait()
  logging.info("return code is %s", str(process.returncode))
  if process.returncode != 0:
    raise ValueError(
      f"Request failed due to "
      f"the response code {process.returncode}"
    )
  logging.info("Cloud run deleted successfully.")


def delete_image_from_artifact():

  "This method deletes the image from artifact regesitry."
  with subprocess.Popen("gcloud artifacts docker images delete "
                        f"us-east4-docker.pkg.dev/"
                        f"{constant.PROJECT_ID}"
                        f"/{constant.E2E_REPO_NAME}/"
                        f"e2e_socrata",
                        shell=True) as process:
    process.wait()
  logging.info("return code is %s", str(process.returncode))
  if process.returncode != 0:
    raise ValueError(
      f"Request failed due to "
      f"the response code {process.returncode}"
    )
  logging.info("Image deleted.")


def read_data_from_storage_and_ingest_to_bq():
  "This method will read the data from GCS and to BigQuery"

  logging.info("Reading file from GCS")
  data = storage_util.read_data_from_storage(
    gcs_file_path=GCS_FILE_PATH,
    gcs_bucket_name=constant.E2E_BUCKET)

  gcs_data = [
    dict(
      rows,
      **{
        "ingestion_timestamp":
          datetime.strptime("2021-06-11 10:14:12.700268",
                            constant.TIME_FORMAT),
        "record_date":
          datetime.strptime(str("2021-06-10"),
                            constant.DATE_FORMAT)
      }
    )
    for rows in data
  ]

  logging.info("File Read Successfully")
  logging.info("Inserting data to BQ")
  bq_utils.ingest_dataframe_to_bq(data=gcs_data,
                                  bq_table_name=BQ_TABLE_NAME)
  logging.info("Data inserted to BQ")



if __name__ == "__main__":
  authenticate_and_trigger_cloud_run(
    url_info=fetch_cloud_run_endpoint())
  read_data_from_storage_and_ingest_to_bq()
  delete_records_from_bq(bq_table_name=table_name,
                         project_id=constant.PROJECT_ID)
  delete_records_from_bq(bq_table_name=BQ_TABLE_NAME,
                         project_id=constant.PROJECT_ID)
  delete_gcs_object()
  delete_cloud_run_service()
  delete_image_from_artifact()

