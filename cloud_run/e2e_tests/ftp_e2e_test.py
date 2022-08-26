"""
ftp_e2e_test.py
Python module for FTP e2e test
"""

import requests as request
import subprocess
import logging

import google.auth
import google.auth.transport.requests
import google.oauth2.id_token
from google.cloud import bigquery
from common import constant

logging.basicConfig(level=logging.INFO)

GCS_FILE_PATH = "gs://e2e-stage/202106100690_840.NY1"
BQ_TABLE_NAME = f"{constant.E2E_DATASET}.ftp_airnow_i_e2e"
table_name = constant.BQ_METADATA_DATASET + "." + constant.JOB_LOGGING_TABLE

def delete_gcs_object():
  """
  This method deletes the files from gcs bucket
  """

  logging.info("deleting object raw folder in GCS bucket")
  with subprocess.Popen(f"gsutil rm gs://{constant.E2E_BUCKET}/raw/"
                        f"adult_care_facility_map/{constant.CURRENT_DATE}/"
                        "adult_care_facility_map_1654856052.json",
                        shell=True) as process:
    process.wait()
  logging.info("return code is %s", str(process.returncode))
  if process.returncode != 0:
    raise ValueError(
      f"Request failed due to "
      f"the response code {process.returncode}"
    )
  logging.info("object deleted successfully from "
               "raw folder in GCS bucket")

  logging.info("deleting object from parsed folder in GCS bucket ")

  with subprocess.Popen(f"gsutil rm gs://{constant.E2E_BUCKET}/parsed/"
                        f"adult_care_facility_map/{constant.CURRENT_DATE}/"
                        "adult_care_facility_map_1654856052.json",
                        shell=True) as process:
    process.wait()
  logging.info("return code is %s", str(process.returncode))
  if process.returncode != 0:
    raise ValueError(
      f"Request failed due to "
      f"the response code {process.returncode}"
    )
  logging.info("object deleted successfully from "
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
  raw_cloud_run_url = url_info[0] + "/gcs_to_bq?" \
                                    "bucket_name=e2e-stage&" \
                                    f"table_name={BQ_TABLE_NAME}&" \
                                    f"ftp_files_to_process=1&" \
                                    f"batch_timestamp" \
                                    f"=2021-06-14 10:14:12.700268"

  url_list = [raw_cloud_run_url]

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
    if "https://ftp-e2e-testing" in itr:
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
    DELETE {project_id}.{bq_table_name} WHERE 
    batch_timestamp="2021-06-14 10:14:12.700268"
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
                        "ftp-e2e-testing "
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
                        f"e2e_ftp",
                        shell=True) as process:
    process.wait()
  logging.info("return code is %s", str(process.returncode))
  if process.returncode != 0:
    raise ValueError(
      f"Request failed due to "
      f"the response code {process.returncode}"
    )
  logging.info("Image deleted.")


if __name__ == "__main__":
  authenticate_and_trigger_cloud_run(url_info=fetch_cloud_run_endpoint())
  delete_records_from_bq(bq_table_name=table_name,
                         project_id=constant.PROJECT_ID)
  delete_records_from_bq(bq_table_name=BQ_TABLE_NAME,
                         project_id=constant.PROJECT_ID)
  delete_cloud_run_service()
  delete_image_from_artifact()
