"""
config.py module.
This module has all the mapping configurations info like web service url,
GCS locations,Big Query table names,ingestion layer task name data source etc
required to trigger the cloud run and store data to Big Query
"""

import constants

FTP_TASKS_CONFIG = [
  # FTP RAW BQ MAIN TASKS.
  {
    "task_name": "ftp_aqs_raw_ingestion",
    "data_source": "ftp_aqs",
    "ingestion_layer": "bq_raw",
    "ingestion_table_name":
      f"{constants.FTP_RAW_DATASET}."
      f"airnow_i",
    "service_endpoint": constants.FTP_CLOUD_RUN_SERVICE_ENDPOINT +
                        f"/gcs_to_bq?bucket_name={constants.FTP_BUCKET_NAME}&"
                        f"table_name="
                        f"{constants.FTP_RAW_DATASET}.airnow_i"
                        f"&ftp_files_to_process="
                        f"{constants.FTP_FILES_TO_PROCESS}"
                        "&batch_timestamp={}",
    "processed_query": "SELECT layer_name "
                       f"FROM {constants.BQ_METADATA_DATASET}."
                       f"{constants.JOB_LOGGING_TABLE} WHERE "
                       "data_source = 'FTP' AND "
                       "batch_timestamp='{}' "
                       "AND status='SUCCESS' limit 1",
    "failed_query": "SELECT layer_name "
                    f"FROM {constants.BQ_METADATA_DATASET}."
                    f"{constants.JOB_LOGGING_TABLE} WHERE "
                    "data_source = 'FTP' AND "
                    "batch_timestamp='{}' "
                    "AND status='FAILED' limit 1",
    "gsutil_processed_cmd":
      f"gsutil mv gs://{constants.FTP_BUCKET_NAME}/"
      "{} "
      f"gs://{constants.FTP_BUCKET_NAME}/processed/",
    "gsutil_failed_cmd":
      f"gsutil mv gs://{constants.FTP_BUCKET_NAME}/"
      "{} "
      f"gs://{constants.FTP_BUCKET_NAME}/failed/",
    "wh_bq_table_name": f"{constants.BQ_WH_DATASET}.ftp_airnow_i",
    "warehouse_query": f"INSERT INTO "
                       f"{constants.BQ_WH_DATASET}.ftp_airnow_i "
                       f"SELECT * FROM "
                       f"{constants.FTP_RAW_DATASET}.airnow_i",
    "audit_wh_query": f" SELECT COUNT(*) AS COUNT "
                      f"FROM {constants.BQ_WH_DATASET}."
                      f"ftp_airnow_i where ingestion_timestamp = ",
    "reporting_bq_table_name":
      f"{constants.BQ_REPORTING_DATASET}.ftp_airnow_i",
    "reporting_query": f"INSERT INTO "
                       f"{constants.BQ_REPORTING_DATASET}.ftp_airnow_i "
                       f"SELECT * FROM "
                       f"{constants.REPORTING_VIEWS}.vw_ftp_airnow_i "
                       f"where ingestion_timestamp = ",
    "audit_reporting_query": f"SELECT COUNT(*) AS COUNT "
                             f"FROM {constants.BQ_REPORTING_DATASET}."
                             "ftp_airnow_i where ingestion_timestamp = ",

  },

]
