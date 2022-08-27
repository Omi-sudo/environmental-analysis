"""
constant.py module
This module contains all the common values/variables which are being used
in the different functions of this pipeline
"""

from datetime import datetime
import google.auth
import os
from common.utils import secrets_util

# GCP Project Info
PROJECT_INFO = google.auth.default()
PROJECT_ID = PROJECT_INFO[1]

# Port number
PORT = int(os.environ.get("PORT", 8080))

# Time Format
TIME_FORMAT = "%Y-%m-%d %H:%M:%S.%f"

# Date Format
DATE_FORMAT = "%Y-%m-%d"

# YEAR
YEAR = 2019

# Current Date
CURRENT_DATE = datetime.today().strftime(DATE_FORMAT)
# Current formatted UTC datetime in string object
CURRENT_DATETIME = datetime.utcnow().strftime(TIME_FORMAT)
# Current formatted UTC datetime in datetime object
CURRENT_FORMATTED_DATETIME = datetime.strptime(CURRENT_DATETIME, TIME_FORMAT)
# Current UTC Timestamp
CURRENT_UTC_DATETIME = datetime.utcnow()

# BQ Tables & Datasets
BQ_METADATA_DATASET = "job_metadata"
JOB_LOGGING_TABLE = "job_audit"

# Components used for e2e testing & unittest coverage
E2E_BUCKET = "e2e-stage"
E2E_DATASET = "e2e_testing"

# Artifact Registry
# This repo is being used for e2e testing
E2E_REPO_NAME = "dec"

# # GCP SECRET MANAGER INFO
#
# AQS_EMAIL = secrets_util.access_secrets(
#   secret_names=f"projects/{PROJECT_ID}/secrets/aqs_email/versions/latest")
# AQS_KEY = secrets_util.access_secrets(
#   secret_names=f"projects/{PROJECT_ID}/secrets/aqs_key/versions/latest")
