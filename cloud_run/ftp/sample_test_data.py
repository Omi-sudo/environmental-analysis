"""
sample_data_test.py Module
This module contains sample data required to execute unit test cases
"""
from common.constant import E2E_DATASET
data = "840360310003,0,0,20220621T0000-0500,88502" \
       ",60,,9.0,105,0,2,44.393136,-73.858953,NAD27,,236,,,,"

schema = ["site", "data_status", "action_code", "datetime",
          "parameter", "duration", "frequency", "value", "unit",
          "qc", "poc", "latitude", "longitude", "gisdatum",
          "elev", "method_code", "mpc", "mpc_value", "uncertainty",
          "qualifiers", "file_name", "record_date", "ingestion_timestamp"]

file_name = "202206100330_840.NY1"
table_name = f"{E2E_DATASET}.ftp_airnow_i_e2e"
