"""
ftp_to_gcp.py Module
This is the main module to process data
ftp data in gcs bucket to BigQuery.
This module will trigger the respective
cloud run service and proceed data to gcp in ingestion
"""

from datetime import timedelta, datetime
import logging
import pendulum

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.python import BranchPythonOperator
from airflow.providers.google.cloud.operators.bigquery import BigQueryInsertJobOperator

import utils
import config
import bq_utils
import constants

# DAG STARTS HERE
try:
  local_tz = pendulum.timezone("America/New_York")

  dag_default_args ={"owner": "airflow",
                     "depends_on_past": False,
                     "start_date": datetime(2020, 5, 7, tzinfo=local_tz),
                     "email_on_failure": False,
                     "email_on_retry": False,
                     "retries": 1,
                     "retry_delay": timedelta(minutes=2),
                     "execution_timeout": timedelta(minutes=20),
    }
  with DAG("FTP_TO_GCP",
           default_args=dag_default_args,
           description="DAG TO ORCHESTRATE FTP DATA TO GCP PIPELINE",
           max_active_runs=3,
           concurrency=30,
           schedule_interval="*/30 * * * *",
           catchup=False,) as dag:

    start = PythonOperator(
        task_id="START",
        python_callable=utils.set_batch_timestamp,
        provide_context=True,
        dag=dag,
    )

    checking_files_in_uploads = BranchPythonOperator(
        task_id="CHECKING_FILES_IN_UPLOADS",
        python_callable=utils.check_files_in_uploads,
        do_xcom_push=False,
        dag=dag,
    )

    no_files_from_ftp = PythonOperator(
        task_id="NO_FILES_FROM_FTP",
        python_callable=lambda: print("NO_FILES_FROM_FTP"),
        dag=dag,
    )

    end = PythonOperator(
        task_id="END",
        trigger_rule="none_failed_or_skipped",
        python_callable=lambda: print("ENDS"),
        dag=dag,
    )
    for task_details in config.FTP_TASKS_CONFIG:
      if task_details["data_source"] == "ftp_aqs":
        truncate_raw_table = PythonOperator(
            task_id="TRUNCATE_RAW_TABLE",
            python_callable=bq_utils.truncate_table_data,
            op_kwargs={
                "bq_table_name": task_details["ingestion_table_name"]
            },
            dag=dag,
        )

        bq_raw_ingestion = PythonOperator(
            task_id="BQ_RAW_INGESTION",
            python_callable=utils.authenticate_and_trigger_cloud_run,
            op_kwargs={
                "url": constants.FTP_CLOUD_RUN_SERVICE_ENDPOINT,
                "service_endpoint": task_details["service_endpoint"],
                "task_id_name": "START",
            },
            dag=dag,
        )

        mv_uploads_to_processed =\
            PythonOperator(
                task_id="MV_UPLOADS_TO_PROCESSED",
                python_callable=utils.moving_files_from_gcs,
                op_kwargs={
                    "query_string": task_details["processed_query"],
                    "task_id_name": "START",
                    "cmd": task_details["gsutil_processed_cmd"],
                    "status": "processed"
                },
                dag=dag,
        )

        mv_uploads_to_failed = \
            PythonOperator(
                task_id="MV_UPLOADS_TO_FAILED",
                python_callable=utils.moving_files_from_gcs,
                op_kwargs={
                    "query_string": task_details["failed_query"],
                    "task_id_name": "START",
                    "cmd": task_details["gsutil_failed_cmd"],
                    "status": "failed"
                },
                dag=dag,
            )

        aqs_ftp_wh_bq_ingestion = \
            BigQueryInsertJobOperator(
                task_id="AQS_FTP_WH_BQ_INGESTION",
                configuration={
                    "query": {
                        "query": task_details["warehouse_query"],
                        "useLegacySql": False,
                    },
                },
                location="us-east4",
                dag=dag,
            )

        aqs_ftp_wh_job_audit = \
            PythonOperator(
                task_id="AQS_FTP_WH_JOB_AUDIT",
                python_callable=utils.bq_insert_job_audit_rows,
                op_kwargs={
                    "parsed_gcs_file_path": None,
                    "bq_table_name": task_details["wh_bq_table_name"],
                    "data_source": "FTP",
                    "layer_name": "ftp_files",
                    "task_name": "aqs_ftp_warehouse_ingestion",
                    "task_id_name": "START",
                    "layer_url": None,
                    "query": task_details["audit_wh_query"] +
                        "'{{ti.xcom_pull(task_ids='START', "
                        "key='batch_timestamp_key')}}'",
                },
                dag=dag,
            )

        aqs_ftp_reporting_bq_ingestion = \
            BigQueryInsertJobOperator(
                task_id="AQS_FTP_REPORTING_BQ_INGESTION",
                configuration={
                    "query": {
                        "query": task_details["reporting_query"] +
                        "'{{ti.xcom_pull(task_ids='START', "
                        "key='batch_timestamp_key')}}'",
                        "useLegacySql": False,
                    },
                },
                location="us-east4",
                dag=dag,
            )

        aqs_ftp_reporting_job_audit = \
            PythonOperator(
                task_id="AQS_FTP_REPORTING_JOB_AUDIT",
                python_callable=utils.bq_insert_job_audit_rows,
                op_kwargs={
                    "parsed_gcs_file_path": None,
                    "bq_table_name":
                        task_details["reporting_bq_table_name"],
                    "data_source": "FTP",
                    "layer_name": "ftp_files",
                    "task_name": "aqs_ftp_reporting_ingestion",
                    "task_id_name": "START",
                    "layer_url": None,
                    "query": task_details["audit_reporting_query"] +
                        "'{{ti.xcom_pull(task_ids='START', "
                        "key='batch_timestamp_key')}}'",
                },
                dag=dag,
            )

    # CHECKING FILES IN UPLOADS
    start.set_downstream(
        checking_files_in_uploads
    )

    # DELETING EXISTING DATA FROM RAW BQ TABLE
    checking_files_in_uploads.set_downstream(
        [truncate_raw_table, no_files_from_ftp])

    # RAW BQ INGESTION
    bq_raw_ingestion.set_upstream(truncate_raw_table)

    # MOVING FILES PROCESSED AND FAILED FOLDER
    bq_raw_ingestion.set_downstream(
        mv_uploads_to_processed)

    bq_raw_ingestion.set_downstream(
        mv_uploads_to_failed)

    # WAREHOUSE BQ INGESTION
    mv_uploads_to_processed.set_downstream(aqs_ftp_wh_bq_ingestion)

    mv_uploads_to_failed.set_downstream(aqs_ftp_wh_bq_ingestion)

    aqs_ftp_wh_bq_ingestion.set_downstream(aqs_ftp_wh_job_audit)

    aqs_ftp_wh_job_audit.set_downstream(aqs_ftp_reporting_bq_ingestion)

    # REPORTING BQ INGESTION
    aqs_ftp_reporting_bq_ingestion.set_downstream(aqs_ftp_reporting_job_audit)

    aqs_ftp_reporting_job_audit.set_downstream(end)

    no_files_from_ftp.set_downstream(end)


except IndexError as ex:
  logging.error("Error while running dag %s", str(ex))
# DAG ENDS HERE
