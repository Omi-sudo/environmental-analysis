"""
constant.py module
This module contains all the common values/variables which are being used
in the different functions of this pipeline
"""
from datetime import datetime, date

import google.auth
from airflow import models

import secrets_util

# ARCGIS_CLOUD_RUN_SERVICE_ENDPOINT = \
#   models.Variable.get("arcgis_cloud_run_service_endpoint")
# SOCRATA_CLOUD_RUN_SERVICE_ENDPOINT = \
#   models.Variable.get("socrata_cloud_run_service_endpoint")
# AQS_CLOUD_RUN_SERVICE_ENDPOINT = \
#   models.Variable.get("aqs_cloud_run_service_endpoint")
FTP_CLOUD_RUN_SERVICE_ENDPOINT = \
  models.Variable.get("ftp_cloud_run_service_endpoint")
FTP_BUCKET_NAME = \
  models.Variable.get("ftp_bucket_name")
FTP_FILES_TO_PROCESS = \
  models.Variable.get("ftp_files_to_process")

# AQS_API_YEAR = [date.today().year if models.Variable.get("aqs_api_year")
#                                      is None or ("" ,
#                                       len(models.Variable.get(
#                                         "aqs_api_year"))) != 4
#                 else models.Variable.get("aqs_api_year")]

# AQS_API_MONTH = models.Variable.get("aqs_api_month")
# AQS_BUCKET_NAME = models.Variable.get("aqs_bucket_name")
# AQS_API_LOOKUP_MONTH = models.Variable.get("aqs_api_lookup_month")
# ARCGIS_BUCKET_NAME = models.Variable.get("arcgis_bucket_name")
# SOCRATA_BUCKET_NAME = models.Variable.get("socrata_bucket_name")

# GCP Project Info
PROJECT_INFO = google.auth.default()
PROJECT_ID = PROJECT_INFO[1]

DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S.000001"

# Time Format
TIME_FORMAT = "%Y-%m-%d %H:%M:%S.%f"

TIME_FORMAT_SECONDS = "%Y-%m-%dT%H:%M:%S"

# Date Format
DATE_FORMAT = "%Y-%m-%d"

# Current Date
CURRENT_DATE = datetime.today().strftime(DATE_FORMAT)
# Current formatted UTC datetime in string object
CURRENT_DATETIME = datetime.utcnow().strftime(TIME_FORMAT)
# Current formatted UTC datetime in datetime object
CURRENT_FORMATTED_DATETIME = \
  datetime.strptime(CURRENT_DATETIME, TIME_FORMAT)
# Current UTC Timestamp
CURRENT_UTC_DATETIME = datetime.utcnow()

# BQ Tables & Datasets
BQ_METADATA_DATASET = "job_metadata"
JOB_LOGGING_TABLE = "job_audit"
REPORTING_VIEWS = "reporting_views"

ARCGIS_RAW_DATASET = "ingestion_arcgis"
SOCRATA_RAW_DATASET = "ingestion_socrata"
AQS_RAW_DATASET = "ingestion_aqs"
FTP_RAW_DATASET = "ingestion_ftp"

BQ_WH_DATASET = "warehouse"
BQ_REPORTING_DATASET = "reporting"

JOB_AUDIT_INFO = "SELECT * FROM " + BQ_METADATA_DATASET + \
                 "." + JOB_LOGGING_TABLE + \
                 " WHERE batch_timestamp = '{}' and data_source = '{}' and " \
                 "step_name = 'gcs_raw_data_ingestion' and layer_name = '{}' " \
                 "and status = 'SUCCESS' limit 1"

# GCP SECRET MANAGER INFO

# AQS_EMAIL = secrets_util.access_secrets(
#   secret_names=f"projects/{PROJECT_ID}/secrets/aqs_email/versions/latest")
# AQS_KEY = secrets_util.access_secrets(
#   secret_names=f"projects/{PROJECT_ID}/secrets/aqs_key/versions/latest")
