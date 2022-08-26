"""
aqs_to_gcp.py Module
This is the main module for aqs apis.
This module will trigger the respective
cloud run service and proceed parsed data to gcp in ingestion,
warehouse and reporting datasets
"""

from datetime import timedelta, datetime
import logging
import pendulum

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.python import BranchPythonOperator

import utils
import constants
import config

# DAG STARTS HERE

aqs_raw_ingestion_list = []
aqs_raw_ingestion_tasks_name_list = []
aqs_parse_ingestion_list = []
aqs_parse_ingestion_tasks_name_list = []
aqs_raw_bq_ingestion_list = []
aqs_raw_bq_ingestion_tasks_name_list = []
aqs_raw_bq_job_audit_list = []
aqs_raw_bq_job_audit_tasks_name_list = []
aqs_wh_bq_ingestion_list = []
aqs_wh_bq_ingestion_tasks_name_list = []
aqs_wh_bq_job_audit_list = []
aqs_wh_bq_job_audit_tasks_name_list = []
aqs_reporting_bq_ingestion_list = []
aqs_reporting_bq_ingestion_tasks_name_list = []
aqs_reporting_bq_job_audit_list = []
aqs_reporting_bq_job_audit_tasks_name_list = []

try:
  local_tz = pendulum.timezone("America/New_York")

  dag_default_args = {"owner": "airflow",
                      "depends_on_past": False,
                      "start_date": datetime(2020, 5, 7, tzinfo=local_tz),
                      "email_on_failure": False,
                      "email_on_retry": False,
                      "retries": 1,
                      "retry_delay": timedelta(minutes=2),
                      "execution_timeout": timedelta(minutes=30),
                      }
  with DAG("AQS_TO_GCP",
           default_args=dag_default_args,
           description="DAG TO ORCHESTRATE AQS API DATA TO GCP PIPELINE",
           max_active_runs=3,
           concurrency=30,
           schedule_interval="0 8 15 * *",
           catchup=False) as dag:

    raw_gcs_ingestion_starts = PythonOperator(
      task_id="RAW_GCS_INGESTION_STARTS",
      python_callable=utils.set_batch_timestamp,
      provide_context=True,
      dag=dag,
    )

    raw_gcs_ingestion_ends = PythonOperator(
      task_id="RAW_GCS_INGESTION_ENDS",
      python_callable=lambda: print("Raw GCS Ingestion Ends"),
      dag=dag,
    )

    parse_gcs_ingestion_starts = BranchPythonOperator(
      task_id="PARSE_GCS_INGESTION_STARTS",
      python_callable=utils.get_xcoms_from_tasks,
      op_kwargs={"xcom_tasks_key_list": aqs_raw_ingestion_tasks_name_list,
                 "upstream_tasks_list": aqs_parse_ingestion_tasks_name_list,
                 "step_name": "parse_ingestion"},
      provide_context=True,
      dag=dag,
    )

    parse_gcs_ingestion_ends = PythonOperator(
      task_id="PARSE_GCS_INGESTION_ENDS",
      python_callable=lambda: print("Parse GCS Ingestion Ends"),
      trigger_rule="none_failed",
      dag=dag,
    )

    bq_raw_ingestion_starts = BranchPythonOperator(
      task_id="BQ_RAW_INGESTION_STARTS",
      python_callable=utils.get_xcoms_from_tasks,
      op_kwargs={"xcom_tasks_key_list": aqs_raw_ingestion_tasks_name_list,
                 "upstream_tasks_list": aqs_raw_bq_ingestion_tasks_name_list,
                 "step_name": "bq_raw_ingestion"},
      provide_context=True,
      dag=dag,
    )

    bq_raw_ingestion_ends = PythonOperator(
      task_id="BQ_RAW_INGESTION_ENDS",
      python_callable=lambda: print("BQ Raw Ingestion Ends"),
      trigger_rule="none_failed",
      dag=dag,
    )

    bq_raw_job_audit_ingestion_starts = BranchPythonOperator(
      task_id="BQ_RAW_JOB_AUDIT_INGESTION_STARTS",
      python_callable=utils.get_xcoms_from_tasks,
      op_kwargs={"xcom_tasks_key_list": aqs_raw_ingestion_tasks_name_list,
                 "upstream_tasks_list": aqs_raw_bq_job_audit_tasks_name_list,
                 "step_name": "bq_raw_job_audit_ingestion"},
      provide_context=True,
      dag=dag,
    )

    bq_raw_job_audit_ingestion_ends = PythonOperator(
      task_id="BQ_RAW_JOB_AUDIT_INGESTION_ENDS",
      python_callable=lambda: print("BQ Job Audit Raw Ingestion Ends"),
      trigger_rule="none_failed",
      dag=dag,
    )

    bq_wh_ingestion_starts = BranchPythonOperator(
      task_id="BQ_WAREHOUSE_INGESTION_STARTS",
      python_callable=utils.get_xcoms_from_tasks,
      op_kwargs={"xcom_tasks_key_list": aqs_raw_ingestion_tasks_name_list,
                 "upstream_tasks_list": aqs_wh_bq_ingestion_tasks_name_list,
                 "step_name": "wh_ingestion"},
      provide_context=True,
      dag=dag,
    )
    bq_wh_ingestion_ends = PythonOperator(
      task_id="BQ_WAREHOUSE_INGESTION_ENDS",
      python_callable=lambda: print("BQ Warehouse Ingestion Ends"),
      trigger_rule="none_failed",
      dag=dag,
    )

    bq_wh_job_audit_ingestion_starts = BranchPythonOperator(
      task_id="BQ_WH_JOB_AUDIT_INGESTION_STARTS",
      python_callable=utils.get_xcoms_from_tasks,
      op_kwargs={"xcom_tasks_key_list": aqs_raw_ingestion_tasks_name_list,
                 "upstream_tasks_list": aqs_wh_bq_job_audit_tasks_name_list,
                 "step_name": "bq_wh_job_audit_ingestion"},
      provide_context=True,
      dag=dag,
    )

    bq_wh_job_audit_ingestion_ends = PythonOperator(
      task_id="BQ_WH_JOB_AUDIT_INGESTION_ENDS",
      python_callable=lambda: print("BQ WH Job Audit Ingestion Ends"),
      trigger_rule="none_failed",
      dag=dag,
    )

    bq_reporting_ingestion_starts = BranchPythonOperator(
      task_id="BQ_REPORTING_INGESTION_STARTS",
      python_callable=utils.get_xcoms_from_tasks,
      op_kwargs={"xcom_tasks_key_list": aqs_raw_ingestion_tasks_name_list,
                 "upstream_tasks_list":
                   aqs_reporting_bq_ingestion_tasks_name_list,
                 "step_name": "reporting_ingestion"},
      provide_context=True,
      dag=dag,
    )

    bq_reporting_ingestion_ends = PythonOperator(
      task_id="BQ_REPORTING_INGESTION_ENDS",
      python_callable=lambda: print("BQ Reporting Ingestion Ends"),
      trigger_rule="none_failed",
      dag=dag,
    )

    bq_reporting_job_audit_ingestion_starts = BranchPythonOperator(
      task_id="BQ_REPORTING_JOB_AUDIT_INGESTION_STARTS",
      python_callable=utils.get_xcoms_from_tasks,
      op_kwargs={"xcom_tasks_key_list": aqs_raw_ingestion_tasks_name_list,
                 "upstream_tasks_list":
                   aqs_reporting_bq_job_audit_tasks_name_list,
                 "step_name": "bq_reporting_job_audit_ingestion"},
      provide_context=True,
      dag=dag,
    )

    bq_reporting_job_audit_ingestion_ends = PythonOperator(
      task_id="BQ_REPORTING_JOB_AUDIT_INGESTION_ENDS",
      python_callable=lambda: print("BQ Reporting Job Audit Ingestion Ends"),
      trigger_rule="none_failed",
      dag=dag,
    )

    for task_details in config.AQS_TASKS_CONFIG:
      if task_details["ingestion_layer"] == "gcs_raw":
        if task_details["data_source"] == "aqs":
          aqs_raw_ingestion_list.append(
            PythonOperator(
              task_id=task_details["task_name"],
              python_callable=utils.authenticate_and_trigger_cloud_run,
              op_kwargs={
                "url": constants.AQS_CLOUD_RUN_SERVICE_ENDPOINT,
                "service_endpoint": task_details["service_endpoint"],
                "task_id_name": "RAW_GCS_INGESTION_STARTS"
              },
              dag=dag,
            )
          )
          aqs_raw_ingestion_tasks_name_list.append(task_details["task_name"])

      elif task_details["ingestion_layer"] == "gcs_parse":
        if task_details["data_source"] == "aqs":
          aqs_parse_ingestion_list.append(PythonOperator(
            task_id=task_details["task_name"],
            python_callable=utils.authenticate_and_trigger_cloud_run,
            op_kwargs={
              "url": constants.AQS_CLOUD_RUN_SERVICE_ENDPOINT,
              "service_endpoint": task_details["service_endpoint"],
              "task_id_name": "RAW_GCS_INGESTION_STARTS"
            },
            dag=dag,
          )
          )
          aqs_parse_ingestion_tasks_name_list.append(task_details["task_name"])

      elif task_details["ingestion_layer"] == "bq_raw":
        if task_details["data_source"] == "aqs":
          aqs_raw_bq_ingestion_list.append(PythonOperator(
            task_id=task_details["task_name"],
            python_callable=utils.read_data_from_gcs_and_ingest_to_bq,
            op_kwargs={
              "parsed_gcs_file_path":
                task_details["parsed_gcs_file_path"],
              "gcs_bucket_name": task_details["gcs_bucket_name"],
              "bq_table_name": task_details["bq_table_name"],
              "new_column_audit_table":
                task_details["new_column_audit_table"],
              "data_source": task_details["data_source"],
              "ingestion_layer": task_details["ingestion_layer"],
              "layer_name": task_details["layer_name"],
              "task_name": task_details["task_name"],
              "layer_url": task_details["layer_url"]
            },
            dag=dag,
          )
          )
          aqs_raw_bq_ingestion_tasks_name_list.append(task_details["task_name"])

      elif task_details["ingestion_layer"] == "bq_raw_job_audit":
        if task_details["data_source"] == "aqs":
          aqs_raw_bq_job_audit_list.append(PythonOperator(
            task_id=task_details["task_name"],
            python_callable=utils.bq_insert_job_audit_rows,
            op_kwargs={
              "parsed_gcs_file_path":
                task_details["parsed_gcs_file_path"],
              "bq_table_name": task_details["bq_table_name"],
              "query": task_details["query"] +
                       "'{{ti.xcom_pull"
                       "(task_ids='RAW_GCS_INGESTION_STARTS', "
                       "key='batch_timestamp_key')}}'",
              "data_source": task_details["data_source"],
              "layer_name": task_details["layer_name"],
              "task_name": task_details["task_name"],
              "layer_url": task_details["layer_url"],
              "task_id_name": "RAW_GCS_INGESTION_STARTS"
            },
            dag=dag,
          )
          )
          aqs_raw_bq_job_audit_tasks_name_list.append(task_details["task_name"])

      elif task_details["ingestion_layer"] == "bq_warehouse":
        if task_details["data_source"] == "aqs":
          aqs_wh_bq_ingestion_list.append(PythonOperator(
            task_id=task_details["task_name"],
            python_callable=utils.
              read_data_from_source_bq_and_ingest_destination_bq,
            op_kwargs={
              "source_table_name": task_details["bq_table_name"],
              "parsed_gcs_file_path":
                task_details["parsed_gcs_file_path"],
              "data_source": task_details["data_source"],
              "ingestion_layer": task_details["ingestion_layer"],
              "destination_table_name":
                task_details["warehouse_table_name"]
            }, dag=dag,
          )
          )
          aqs_wh_bq_ingestion_tasks_name_list.append(task_details["task_name"])

      elif task_details["ingestion_layer"] == "bq_wh_job_audit":
        if task_details["data_source"] == "aqs":
          aqs_wh_bq_job_audit_list.append(PythonOperator(
            task_id=task_details["task_name"],
            python_callable=utils.bq_insert_job_audit_rows,
            op_kwargs={
              "parsed_gcs_file_path":
                task_details["parsed_gcs_file_path"],
              "bq_table_name": task_details["bq_table_name"],
              "query": task_details["query"] +
                       "'{{ti.xcom_pull"
                       "(task_ids='RAW_GCS_INGESTION_STARTS', "
                       "key='batch_timestamp_key')}}'",
              "data_source": task_details["data_source"],
              "layer_name": task_details["layer_name"],
              "task_name": task_details["task_name"],
              "layer_url": task_details["layer_url"],
              "task_id_name": "RAW_GCS_INGESTION_STARTS"
            },
            dag=dag,
          )
          )
          aqs_wh_bq_job_audit_tasks_name_list.append(task_details["task_name"])

      elif task_details["ingestion_layer"] == "aqs_bq_reporting":
        if task_details["data_source"] == "aqs":
          aqs_reporting_bq_ingestion_list.append(PythonOperator(
            task_id=task_details["task_name"],
            python_callable=utils.
              read_data_from_source_bq_and_ingest_destination_bq,
            op_kwargs={
              "source_table_name": task_details["source_table_name"],
              "parsed_gcs_file_path":
                task_details["parsed_gcs_file_path"],
              "data_source": task_details["data_source"],
              "ingestion_layer": task_details["ingestion_layer"],
              "destination_table_name":
                task_details["reporting_table_name"]
            }, dag=dag,

          )
          )
          aqs_reporting_bq_ingestion_tasks_name_list. \
            append(task_details["task_name"])

      elif task_details["ingestion_layer"] == "bq_reporting_job_audit":
        if task_details["data_source"] == "aqs":
          aqs_reporting_bq_job_audit_list.append(PythonOperator(
            task_id=task_details["task_name"],
            python_callable=utils.bq_insert_job_audit_rows,
            op_kwargs={
              "parsed_gcs_file_path":
                task_details["parsed_gcs_file_path"],
              "bq_table_name": task_details["bq_table_name"],
              "query": task_details["query"] +
                       "'{{ti.xcom_pull"
                       "(task_ids='RAW_GCS_INGESTION_STARTS', "
                       "key='batch_timestamp_key')}}'",
              "data_source": task_details["data_source"],
              "layer_name": task_details["layer_name"],
              "task_name": task_details["task_name"],
              "layer_url": task_details["layer_url"],
              "task_id_name": "RAW_GCS_INGESTION_STARTS"
            },
            dag=dag,
          )
          )
          aqs_reporting_bq_job_audit_tasks_name_list.append(
            task_details["task_name"])

        # RAW GCS TASKS STREAMS STARTS

        raw_gcs_ingestion_starts.set_downstream(
          aqs_raw_ingestion_list
        )

        raw_gcs_ingestion_ends.set_upstream(aqs_raw_ingestion_list)

        raw_gcs_ingestion_ends.set_downstream(parse_gcs_ingestion_starts)

        # PARSE GCS TASKS STREAMS STARTS

        parse_gcs_ingestion_starts.set_downstream(
          aqs_parse_ingestion_list
        )

        parse_gcs_ingestion_ends.set_upstream(aqs_parse_ingestion_list)

        parse_gcs_ingestion_ends.set_downstream(bq_raw_ingestion_starts)

        # RAW BQ INGESTION TASKS STREAMS STARTS

        bq_raw_ingestion_starts.set_downstream(
          aqs_raw_bq_ingestion_list
        )

        bq_raw_ingestion_ends.set_upstream(
          aqs_raw_bq_ingestion_list,
        )

        bq_raw_ingestion_ends.set_downstream(bq_raw_job_audit_ingestion_starts)

        # BQ RAW JOB AUDIT INGESTION TASKS STREAMS STARTS

        bq_raw_job_audit_ingestion_starts.set_downstream(
          aqs_raw_bq_job_audit_list
        )

        bq_raw_job_audit_ingestion_ends.set_upstream(
          aqs_raw_bq_job_audit_list,
        )

        bq_raw_job_audit_ingestion_ends.set_downstream(bq_wh_ingestion_starts)

        # WH BQ INGESTION TASKS STREAMS STARTS

        bq_wh_ingestion_starts.set_downstream(
          aqs_wh_bq_ingestion_list
        )

        bq_wh_ingestion_ends.set_upstream(
          aqs_wh_bq_ingestion_list,
        )

        bq_wh_ingestion_ends.set_downstream(bq_wh_job_audit_ingestion_starts)

        # BQ WH JOB AUDIT INGESTION TASKS STREAMS STARTS

        bq_wh_job_audit_ingestion_starts.set_downstream(
          aqs_wh_bq_job_audit_list
        )

        bq_wh_job_audit_ingestion_ends.set_upstream(
          aqs_wh_bq_job_audit_list,
        )

        bq_wh_job_audit_ingestion_ends.set_downstream(
          bq_reporting_ingestion_starts)

        # REPORTING BQ INGESTION TASKS STREAMS STARTS

        bq_reporting_ingestion_starts.set_downstream(
          aqs_reporting_bq_ingestion_list
        )

        bq_reporting_ingestion_ends.set_upstream(
          aqs_reporting_bq_ingestion_list,
        )

        bq_reporting_ingestion_ends.set_downstream(
          bq_reporting_job_audit_ingestion_starts)

        # BQ REPORTING JOB AUDIT INGESTION TASKS STREAMS STARTS

        bq_reporting_job_audit_ingestion_starts.set_downstream(
          aqs_reporting_bq_job_audit_list
        )

        bq_reporting_job_audit_ingestion_ends.set_upstream(
          aqs_reporting_bq_job_audit_list,
        )


except IndexError as ex:
  logging.error("Error while running dag %s", str(ex))
# DAG ENDS HERE
