"""
config.py module.
This module has all the mapping configurations info like web service url,
GCS locations,Big Query table names,ingestion layer task name data source etc
required to trigger the cloud run and store data to Big Query
"""

import constants

ARCGIS_TASKS_CONFIG = [
  # ARCGIS RAW GCS INGESTION MAIN TASKS

  {
    "task_name": "nursing_homes_raw_ingestion",
    "data_source": "arcgis_apis",
    "ingestion_layer": "gcs_raw",
    "service_endpoint": constants.ARCGIS_CLOUD_RUN_SERVICE_ENDPOINT
                        + "/process_raw_layer?layer_name=nursing_homes&"
                          "batch_timestamp={}&batch_unix_timestamp={}&"
                          f"bucket={constants.ARCGIS_BUCKET_NAME}",
  },
  {
    "task_name": "remediation_sites_raw_ingestion",
    "data_source": "arcgis_apis",
    "ingestion_layer": "gcs_raw",
    "service_endpoint": constants.ARCGIS_CLOUD_RUN_SERVICE_ENDPOINT
                        + "/process_raw_layer?layer_name=remediation_sites&"
                          "batch_timestamp={}&batch_unix_timestamp={}&"
                          f"bucket={constants.ARCGIS_BUCKET_NAME}",
  },
  {
    "task_name": "remediation_boundaries_raw_ingestion",
    "data_source": "arcgis_apis",
    "ingestion_layer": "gcs_raw",
    "service_endpoint": constants.ARCGIS_CLOUD_RUN_SERVICE_ENDPOINT
                        + "/process_raw_layer?"
                          "layer_name=remediation_boundaries&"
                          "batch_timestamp={}&batch_unix_timestamp={}&"
                          f"bucket={constants.ARCGIS_BUCKET_NAME}",
  },
  {
    "task_name": "air_title_v_raw_ingestion",
    "data_source": "arcgis_apis",
    "ingestion_layer": "gcs_raw",
    "service_endpoint": constants.ARCGIS_CLOUD_RUN_SERVICE_ENDPOINT
                        + "/process_raw_layer?layer_name=air_title_v&"
                          "batch_timestamp={}&batch_unix_timestamp={}&"
                          f"bucket={constants.ARCGIS_BUCKET_NAME}",
  },
  {
    "task_name": "air_facilities_system_raw_ingestion",
    "data_source": "arcgis_apis",
    "ingestion_layer": "gcs_raw",
    "service_endpoint": constants.ARCGIS_CLOUD_RUN_SERVICE_ENDPOINT
                        + "/process_raw_layer?"
                          "layer_name=air_facilities_system&"
                          "batch_timestamp={}&batch_unix_timestamp={}&"
                          f"bucket={constants.ARCGIS_BUCKET_NAME}",
  },
  {
    "task_name": "air_facility_registration_raw_ingestion",
    "data_source": "arcgis_apis",
    "ingestion_layer": "gcs_raw",
    "service_endpoint": constants.ARCGIS_CLOUD_RUN_SERVICE_ENDPOINT
                        + "/process_raw_layer?"
                          "layer_name=air_facility_registration&"
                          "batch_timestamp={}&batch_unix_timestamp={}&"
                          f"bucket={constants.ARCGIS_BUCKET_NAME}",
  },
  {
    "task_name": "major_oil_storage_facilities_raw_ingestion",
    "data_source": "arcgis_apis",
    "ingestion_layer": "gcs_raw",
    "service_endpoint": constants.ARCGIS_CLOUD_RUN_SERVICE_ENDPOINT
                        + "/process_raw_layer?"
                          "layer_name=major_oil_storage_facilities&"
                          "batch_timestamp={}&batch_unix_timestamp={}&"
                          f"bucket={constants.ARCGIS_BUCKET_NAME}",
  },

  # ARCGIS PARSE GCS INGESTION MAIN TASKS

  {
    "task_name": "nursing_homes_parse_ingestion",
    "data_source": "arcgis_apis",
    "ingestion_layer": "gcs_parse",
    "service_endpoint":
      f"{constants.ARCGIS_CLOUD_RUN_SERVICE_ENDPOINT}"
      f"/process_parse_layer?layer_name="
      f"nursing_homes&raw_gcs_ingestion_date={constants.CURRENT_DATE}"
      "&batch_timestamp={}&batch_unix_timestamp={}"
      f"&bucket={constants.ARCGIS_BUCKET_NAME}",
  },
  {
    "task_name": "remediation_sites_parse_ingestion",
    "data_source": "arcgis_apis",
    "ingestion_layer": "gcs_parse",
    "service_endpoint":
      f"{constants.ARCGIS_CLOUD_RUN_SERVICE_ENDPOINT}"
      f"/process_parse_layer?layer_name="
      f"remediation_sites&raw_gcs_ingestion_date="
      f"{constants.CURRENT_DATE}"
      "&batch_timestamp={}&batch_unix_timestamp={}"
      f"&bucket={constants.ARCGIS_BUCKET_NAME}",
  },
  {
    "task_name": "remediation_boundaries_parse_ingestion",
    "data_source": "arcgis_apis",
    "ingestion_layer": "gcs_parse",
    "service_endpoint":
      f"{constants.ARCGIS_CLOUD_RUN_SERVICE_ENDPOINT}"
      f"/process_parse_layer?layer_name="
      f"remediation_boundaries&raw_gcs_ingestion_date="
      f"{constants.CURRENT_DATE}"
      "&batch_timestamp={}&batch_unix_timestamp={}"
      f"&bucket={constants.ARCGIS_BUCKET_NAME}",
  },
  {
    "task_name": "air_title_v_parse_ingestion",
    "data_source": "arcgis_apis",
    "ingestion_layer": "gcs_parse",
    "service_endpoint":
      f"{constants.ARCGIS_CLOUD_RUN_SERVICE_ENDPOINT}"
      f"/process_parse_layer?layer_name="
      f"air_title_v&raw_gcs_ingestion_date="
      f"{constants.CURRENT_DATE}"
      "&batch_timestamp={}&batch_unix_timestamp={}"
      f"&bucket={constants.ARCGIS_BUCKET_NAME}",
  },
  {
    "task_name": "air_facilities_system_parse_ingestion",
    "data_source": "arcgis_apis",
    "ingestion_layer": "gcs_parse",
    "service_endpoint":
      f"{constants.ARCGIS_CLOUD_RUN_SERVICE_ENDPOINT}"
      f"/process_parse_layer?layer_name="
      f"air_facilities_system&raw_gcs_ingestion_date="
      f"{constants.CURRENT_DATE}"
      "&batch_timestamp={}&batch_unix_timestamp={}"
      f"&bucket={constants.ARCGIS_BUCKET_NAME}",
  },
  {
    "task_name": "air_facility_registration_parse_ingestion",
    "data_source": "arcgis_apis",
    "ingestion_layer": "gcs_parse",
    "service_endpoint":
      f"{constants.ARCGIS_CLOUD_RUN_SERVICE_ENDPOINT}"
      f"/process_parse_layer?layer_name="
      f"air_facility_registration&raw_gcs_ingestion_date="
      f"{constants.CURRENT_DATE}"
      "&batch_timestamp={}&batch_unix_timestamp={}"
      f"&bucket={constants.ARCGIS_BUCKET_NAME}",
  },
  {
    "task_name": "major_oil_storage_facilities_parse_ingestion",
    "data_source": "arcgis_apis",
    "ingestion_layer": "gcs_parse",
    "service_endpoint":
      f"{constants.ARCGIS_CLOUD_RUN_SERVICE_ENDPOINT}"
      f"/process_parse_layer?layer_name="
      f"major_oil_storage_facilities&raw_gcs_ingestion_date="
      f"{constants.CURRENT_DATE}"
      "&batch_timestamp={}&batch_unix_timestamp={}"
      f"&bucket={constants.ARCGIS_BUCKET_NAME}",
  },
  # ARCGIS RAW BQ INGESTION
  {
    "task_name": "nursing_homes_bq_raw_ingestion",
    "bq_table_name": f"{constants.ARCGIS_RAW_DATASET}.nursing_homes",
    "new_column_audit_table":
      f"{constants.BQ_METADATA_DATASET}.new_column_audit",
    "gcs_bucket_name": constants.ARCGIS_BUCKET_NAME,
    "parsed_gcs_file_path": f"parsed/nursing_homes/"
                            f"{constants.CURRENT_DATE}/"
                            "nursing_homes_{}.json",
    "data_source": "arcgis_apis",
    "ingestion_layer": "bq_raw",
    "layer_name": "nursing_homes",
    "layer_url": "https://services1.arcgis.com/Hp6G80Pky0om7QvQ/"
                 "ArcGIS/rest/services/NursingHomes/FeatureServer/0"
  },
  {
    "task_name": "remediation_sites_bq_raw_ingestion",
    "bq_table_name":
      f"{constants.ARCGIS_RAW_DATASET}.remediation_sites",
    "new_column_audit_table":
      f"{constants.BQ_METADATA_DATASET}.new_column_audit",
    "gcs_bucket_name": constants.ARCGIS_BUCKET_NAME,
    "parsed_gcs_file_path": f"parsed/remediation_sites/"
                            f"{constants.CURRENT_DATE}/"
                            "remediation_sites_{}.json",
    "data_source": "arcgis_apis",
    "ingestion_layer": "bq_raw",
    "layer_name": "remediation_sites",
    "layer_url": "https://services6.arcgis.com/DZHaqZm9cxOD4CWM/"
                 "ArcGIS/rest/services/Remediation_Sites/FeatureServer/0"
  },
  {
    "task_name": "remediation_boundaries_bq_raw_ingestion",
    "bq_table_name":
      f"{constants.ARCGIS_RAW_DATASET}.remediation_boundaries",
    "new_column_audit_table":
      f"{constants.BQ_METADATA_DATASET}.new_column_audit",
    "gcs_bucket_name": constants.ARCGIS_BUCKET_NAME,
    "parsed_gcs_file_path": f"parsed/remediation_boundaries/"
                            f"{constants.CURRENT_DATE}/"
                            "remediation_boundaries_{}.json",
    "data_source": "arcgis_apis",
    "ingestion_layer": "bq_raw",
    "layer_name": "remediation_boundaries",
    "layer_url": "https://services6.arcgis.com/DZHaqZm9cxOD4CWM/ArcGIS/"
                 "rest/services/Remediation_Boundaries/FeatureServer/0",
  },
  {
    "task_name": "air_title_v_bq_raw_ingestion",
    "bq_table_name":
      f"{constants.ARCGIS_RAW_DATASET}."
      f"atv_total_emissions_submitted",
    "new_column_audit_table":
      f"{constants.BQ_METADATA_DATASET}.new_column_audit",
    "gcs_bucket_name": constants.ARCGIS_BUCKET_NAME,
    "parsed_gcs_file_path": f"parsed/air_title_v/"
                            f"{constants.CURRENT_DATE}/"
                            "air_title_v_{}.json",
    "data_source": "arcgis_apis",
    "ingestion_layer": "bq_raw",
    "layer_name": "air_title_v",
    "layer_url": "https://services6.arcgis.com/DZHaqZm9cxOD4CWM/ArcGIS/"
                 "rest/services/CLCPA_ATV/FeatureServer/0"
  },
  {
    "task_name": "air_facilities_system_bq_raw_ingestion",
    "bq_table_name":
      f"{constants.ARCGIS_RAW_DATASET}.air_facilities_system",
    "new_column_audit_table":
      f"{constants.BQ_METADATA_DATASET}.new_column_audit",
    "gcs_bucket_name": constants.ARCGIS_BUCKET_NAME,
    "parsed_gcs_file_path": f"parsed/air_facilities_system/"
                            f"{constants.CURRENT_DATE}/"
                            "air_facilities_system_{}.json",
    "data_source": "arcgis_apis",
    "ingestion_layer": "bq_raw",
    "layer_name": "air_facilities_system",
    "layer_url": "https://services6.arcgis.com/DZHaqZm9cxOD4CWM/ArcGIS/"
                 "rest/services/CLCPA_ASF/FeatureServer/0",
  },
  {
    "task_name": "air_facility_registration_bq_raw_ingestion",
    "bq_table_name":
      f"{constants.ARCGIS_RAW_DATASET}.air_facility_registration",
    "new_column_audit_table":
      f"{constants.BQ_METADATA_DATASET}.new_column_audit",
    "gcs_bucket_name": constants.ARCGIS_BUCKET_NAME,
    "parsed_gcs_file_path": f"parsed/air_facility_registration/"
                            f"{constants.CURRENT_DATE}/"
                            "air_facility_registration_{}.json",
    "data_source": "arcgis_apis",
    "ingestion_layer": "bq_raw",
    "layer_name": "air_facility_registration",
    "layer_url": "https://services6.arcgis.com/DZHaqZm9cxOD4CWM/ArcGIS/"
                 "rest/services/CLCPA_AFR/FeatureServer/0",
  },
  {
    "task_name": "major_oil_storage_facilities_bq_raw_ingestion",
    "bq_table_name":
      f"{constants.ARCGIS_RAW_DATASET}.major_oil_storage_facilities",
    "new_column_audit_table":
      f"{constants.BQ_METADATA_DATASET}.new_column_audit",
    "gcs_bucket_name": constants.ARCGIS_BUCKET_NAME,
    "parsed_gcs_file_path": f"parsed/major_oil_storage_facilities/"
                            f"{constants.CURRENT_DATE}/"
                            "major_oil_storage_facilities_{}.json",
    "data_source": "arcgis_apis",
    "ingestion_layer": "bq_raw",
    "layer_name": "major_oil_storage_facilities",
    "layer_url": "https://services6.arcgis.com/DZHaqZm9cxOD4CWM/ArcGIS"
                 "/rest/services/Major_Oil_Storage_Facility/FeatureServer/0",
  },
  # ARCGIS JOB_AUDIT RAW BQ INGESTION
  {
    "task_name": "nursing_homes_bq_raw_job_audit_ingestion",
    "bq_table_name": f"{constants.ARCGIS_RAW_DATASET}.nursing_homes",
    "query": f" SELECT COUNT(*) AS COUNT FROM {constants.ARCGIS_RAW_DATASET}."
             f"nursing_homes WHERE ingestion_timestamp = ",
    "gcs_bucket_name": constants.ARCGIS_BUCKET_NAME,
    "parsed_gcs_file_path": f"parsed/nursing_homes/"
                            f"{constants.CURRENT_DATE}/nursing_homes.json",
    "data_source": "arcgis_apis",
    "ingestion_layer": "bq_raw_job_audit",
    "layer_name": "nursing_homes",
    "layer_url": "https://services1.arcgis.com/Hp6G80Pky0om7QvQ/"
                 "ArcGIS/rest/services/NursingHomes/FeatureServer/0"
  },
  {
    "task_name": "remediation_sites_bq_raw_job_audit_ingestion",
    "query":
      f" SELECT COUNT(*) AS COUNT FROM "
      f"{constants.ARCGIS_RAW_DATASET}.remediation_sites"
      f" WHERE ingestion_timestamp = ",
    "bq_table_name": f"{constants.ARCGIS_RAW_DATASET}.remediation_sites",
    "gcs_bucket_name": constants.ARCGIS_BUCKET_NAME,
    "parsed_gcs_file_path": f"parsed/remediation_sites/"
                            f"{constants.CURRENT_DATE}/"
                            f"remediation_sites.json",
    "data_source": "arcgis_apis",
    "ingestion_layer": "bq_raw_job_audit",
    "layer_name": "remediation_sites",
    "layer_url": "https://services6.arcgis.com/DZHaqZm9cxOD4CWM/"
                 "ArcGIS/rest/services/Remediation_Sites/FeatureServer/0"
  },
  {
    "task_name": "remediation_boundaries_bq_raw_job_audit_ingestion",
    "query":
      f" SELECT COUNT(*) AS COUNT FROM "
      f"{constants.ARCGIS_RAW_DATASET}.remediation_boundaries "
      f"WHERE ingestion_timestamp = ",
    "bq_table_name": f"{constants.ARCGIS_RAW_DATASET}.remediation_boundaries",
    "gcs_bucket_name": constants.ARCGIS_BUCKET_NAME,
    "parsed_gcs_file_path": f"parsed/remediation_boundaries/"
                            f"{constants.CURRENT_DATE}/"
                            f"remediation_boundaries.json",
    "data_source": "arcgis_apis",
    "ingestion_layer": "bq_raw_job_audit",
    "layer_name": "remediation_boundaries",
    "layer_url": "https://services6.arcgis.com/DZHaqZm9cxOD4CWM/ArcGIS/"
                 "rest/services/Remediation_Boundaries/FeatureServer/0",
  },
  {
    "task_name": "air_title_v_bq_raw_job_audit_ingestion",
    "query":
      f" SELECT COUNT(*) AS COUNT FROM {constants.ARCGIS_RAW_DATASET}."
      f"atv_total_emissions_submitted WHERE ingestion_timestamp = ",
    "bq_table_name": f"{constants.ARCGIS_RAW_DATASET}."
                     f"atv_total_emissions_submitted",
    "gcs_bucket_name": constants.ARCGIS_BUCKET_NAME,
    "parsed_gcs_file_path": f"parsed/air_title_v/"
                            f"{constants.CURRENT_DATE}/air_title_v.json",
    "data_source": "arcgis_apis",
    "ingestion_layer": "bq_raw_job_audit",
    "layer_name": "air_title_v",
    "layer_url": "https://services6.arcgis.com/DZHaqZm9cxOD4CWM/ArcGIS/"
                 "rest/services/CLCPA_ATV/FeatureServer/0"
  },
  {
    "task_name": "air_facilities_system_bq_raw_job_audit_ingestion",
    "query":
      f" SELECT COUNT(*) AS COUNT FROM "
      f"{constants.ARCGIS_RAW_DATASET}.air_facilities_system"
      f" WHERE ingestion_timestamp = ",
    "bq_table_name": f"{constants.ARCGIS_RAW_DATASET}.air_facilities_system",
    "gcs_bucket_name": constants.ARCGIS_BUCKET_NAME,
    "parsed_gcs_file_path": f"parsed/air_facilities_system/"
                            f"{constants.CURRENT_DATE}/"
                            f"air_facilities_system.json",
    "data_source": "arcgis_apis",
    "ingestion_layer": "bq_raw_job_audit",
    "layer_name": "air_facilities_system",
    "layer_url": "https://services6.arcgis.com/DZHaqZm9cxOD4CWM/ArcGIS/"
                 "rest/services/CLCPA_ASF/FeatureServer/0",
  },
  {
    "task_name":
      "air_facility_registration_bq_raw_job_audit_ingestion",
    "query":
      f" SELECT COUNT(*) AS COUNT FROM "
      f"{constants.ARCGIS_RAW_DATASET}.air_facility_registration"
      f" WHERE ingestion_timestamp = ",
    "bq_table_name":
      f"{constants.ARCGIS_RAW_DATASET}.air_facility_registration",
    "gcs_bucket_name": constants.ARCGIS_BUCKET_NAME,
    "parsed_gcs_file_path": f"parsed/air_facility_registration/"
                            f"{constants.CURRENT_DATE}/"
                            f"air_facility_registration.json",
    "data_source": "arcgis_apis",
    "ingestion_layer": "bq_raw_job_audit",
    "layer_name": "air_facility_registration",
    "layer_url": "https://services6.arcgis.com/DZHaqZm9cxOD4CWM/ArcGIS/"
                 "rest/services/CLCPA_AFR/FeatureServer/0",
  },
  {
    "task_name":
      "major_oil_storage_facilities_bq_raw_job_audit_ingestion",
    "query":
      f" SELECT COUNT(*) AS COUNT FROM "
      f"{constants.ARCGIS_RAW_DATASET}.major_oil_storage_facilities"
      f" WHERE ingestion_timestamp = ",
    "bq_table_name":
      f"{constants.ARCGIS_RAW_DATASET}.major_oil_storage_facilities",
    "gcs_bucket_name": constants.ARCGIS_BUCKET_NAME,
    "parsed_gcs_file_path": f"parsed/major_oil_storage_facilities/"
                            f"{constants.CURRENT_DATE}/"
                            f"major_oil_storage_facilities.json",
    "data_source": "arcgis_apis",
    "ingestion_layer": "bq_raw_job_audit",
    "layer_name": "major_oil_storage_facilities",
    "layer_url": "https://services6.arcgis.com/DZHaqZm9cxOD4CWM/ArcGIS"
                 "/rest/services/Major_Oil_Storage_Facility/FeatureServer/0",
  },
  # ARCGIS WH BQ INGESTION
  {
    "task_name": "nursing_homes_wh_ingestion",
    "bq_table_name": f" SELECT * FROM "
                     f"{constants.ARCGIS_RAW_DATASET}.nursing_homes",
    "data_source": "arcgis_apis",
    "ingestion_layer": "bq_warehouse",
    "layer_name": "nursing_homes",
    "warehouse_table_name":
      f"{constants.BQ_WH_DATASET}.arcgis_nursing_homes",
    "layer_url": "https://services1.arcgis.com/Hp6G80Pky0om7QvQ/"
                 "ArcGIS/rest/services/NursingHomes/FeatureServer/0"

  },
  {
    "task_name": "remediation_sites_wh_ingestion",
    "bq_table_name": f" SELECT * FROM "
                     f"{constants.ARCGIS_RAW_DATASET}.remediation_sites",
    "data_source": "arcgis_apis",
    "ingestion_layer": "bq_warehouse",
    "layer_name": "remediation_sites",
    "warehouse_table_name":
      f"{constants.BQ_WH_DATASET}.arcgis_remediation_sites",
    "layer_url": "https://services6.arcgis.com/DZHaqZm9cxOD4CWM/"
                 "ArcGIS/rest/services/Remediation_Sites/FeatureServer/0"

  },
  {
    "task_name": "remediation_boundaries_wh_ingestion",
    "bq_table_name":
      f" SELECT * FROM {constants.ARCGIS_RAW_DATASET}.remediation_boundaries",
    "data_source": "arcgis_apis",
    "ingestion_layer": "bq_warehouse",
    "layer_name": "remediation_boundaries",
    "warehouse_table_name":
      f"{constants.BQ_WH_DATASET}.arcgis_remediation_boundaries",
    "layer_url": "https://services6.arcgis.com/DZHaqZm9cxOD4CWM/ArcGIS/"
                 "rest/services/Remediation_Boundaries/FeatureServer/0",

  },
  {
    "task_name": "air_title_v_wh_ingestion",
    "bq_table_name":
      f" SELECT * FROM {constants.ARCGIS_RAW_DATASET}."
      f"atv_total_emissions_submitted",
    "data_source": "arcgis_apis",
    "ingestion_layer": "bq_warehouse",
    "layer_name": "air_title_v",
    "warehouse_table_name":
      f"{constants.BQ_WH_DATASET}.arcgis_atv_total_emissions_submitted",
    "layer_url": "https://services6.arcgis.com/DZHaqZm9cxOD4CWM/ArcGIS/"
                 "rest/services/CLCPA_ATV/FeatureServer/0"

  },
  {
    "task_name": "air_facilities_system_wh_ingestion",
    "bq_table_name":
      f" SELECT * FROM {constants.ARCGIS_RAW_DATASET}.air_facilities_system",
    "data_source": "arcgis_apis",
    "ingestion_layer": "bq_warehouse",
    "layer_name": "air_facilities_system",
    "layer_url": "https://services6.arcgis.com/DZHaqZm9cxOD4CWM/ArcGIS/"
                 "rest/services/CLCPA_ASF/FeatureServer/0",
    "warehouse_table_name":
      f"{constants.BQ_WH_DATASET}.arcgis_air_facilities_system",

  },
  {
    "task_name": "air_facility_registration_wh_ingestion",
    "bq_table_name":
      f" SELECT * FROM {constants.ARCGIS_RAW_DATASET}."
      f"air_facility_registration",
    "data_source": "arcgis_apis",
    "ingestion_layer": "bq_warehouse",
    "layer_name": "air_facility_registration",
    "warehouse_table_name":
      f"{constants.BQ_WH_DATASET}.arcgis_air_facility_registration",
    "layer_url": "https://services6.arcgis.com/DZHaqZm9cxOD4CWM/ArcGIS/"
                 "rest/services/CLCPA_AFR/FeatureServer/0",

  },
  {
    "task_name": "major_oil_storage_facilities_wh_ingestion",
    "bq_table_name":
      f" SELECT * FROM {constants.ARCGIS_RAW_DATASET}."
      f"major_oil_storage_facilities",
    "data_source": "arcgis_apis",
    "ingestion_layer": "bq_warehouse",
    "layer_name": "major_oil_storage_facilities",
    "warehouse_table_name":
      f"{constants.BQ_WH_DATASET}.arcgis_major_oil_storage_facilities",
    "layer_url": "https://services6.arcgis.com/DZHaqZm9cxOD4CWM/ArcGIS"
                 "/rest/services/Major_Oil_Storage_Facility/FeatureServer/0",

  },
  # ARCGIS JOB_AUDIT WH BQ INGESTION
  {
    "task_name": "nursing_homes_bq_wh_job_audit_ingestion",
    "bq_table_name": f"{constants.BQ_WH_DATASET}.arcgis_nursing_homes",
    "query": f" SELECT COUNT(*) AS COUNT FROM {constants.BQ_WH_DATASET}."
             f"arcgis_nursing_homes WHERE ingestion_timestamp = ",
    "gcs_bucket_name": constants.ARCGIS_BUCKET_NAME,
    "parsed_gcs_file_path": f"parsed/nursing_homes/"
                            f"{constants.CURRENT_DATE}/nursing_homes.json",
    "data_source": "arcgis_apis",
    "ingestion_layer": "bq_wh_job_audit",
    "layer_name": "nursing_homes",
    "layer_url": "https://services1.arcgis.com/Hp6G80Pky0om7QvQ/"
                 "ArcGIS/rest/services/NursingHomes/FeatureServer/0"
  },
  {
    "task_name": "remediation_sites_bq_wh_job_audit_ingestion",
    "query":
      f" SELECT COUNT(*) AS COUNT FROM "
      f"{constants.BQ_WH_DATASET}.arcgis_remediation_sites "
      f"WHERE ingestion_timestamp = ",
    "bq_table_name": f"{constants.BQ_WH_DATASET}.arcgis_remediation_sites",
    "gcs_bucket_name": constants.ARCGIS_BUCKET_NAME,
    "parsed_gcs_file_path": f"parsed/remediation_sites/"
                            f"{constants.CURRENT_DATE}/"
                            f"remediation_sites.json",
    "data_source": "arcgis_apis",
    "ingestion_layer": "bq_wh_job_audit",
    "layer_name": "remediation_sites",
    "layer_url": "https://services6.arcgis.com/DZHaqZm9cxOD4CWM/"
                 "ArcGIS/rest/services/Remediation_Sites/FeatureServer/0"
  },
  {
    "task_name": "remediation_boundaries_bq_wh_job_audit_ingestion",
    "query":
      f" SELECT COUNT(*) AS COUNT FROM "
      f"{constants.BQ_WH_DATASET}.arcgis_remediation_boundaries"
      f" WHERE ingestion_timestamp = ",
    "bq_table_name": f"{constants.BQ_WH_DATASET}.argics_remediation_boundaries",
    "gcs_bucket_name": constants.ARCGIS_BUCKET_NAME,
    "parsed_gcs_file_path": f"parsed/remediation_boundaries/"
                            f"{constants.CURRENT_DATE}/"
                            f"remediation_boundaries.json",
    "data_source": "arcgis_apis",
    "ingestion_layer": "bq_wh_job_audit",
    "layer_name": "remediation_boundaries",
    "layer_url": "https://services6.arcgis.com/DZHaqZm9cxOD4CWM/ArcGIS/"
                 "rest/services/Remediation_Boundaries/FeatureServer/0",
  },
  {
    "task_name": "air_title_v_bq_wh_job_audit_ingestion",
    "query":
      f" SELECT COUNT(*) AS COUNT FROM {constants.BQ_WH_DATASET}."
      f"arcgis_atv_total_emissions_submitted "
      f"WHERE ingestion_timestamp = ",
    "bq_table_name": f"{constants.BQ_WH_DATASET}."
                     f"arcgis_atv_total_emissions_submitted",
    "gcs_bucket_name": constants.ARCGIS_BUCKET_NAME,
    "parsed_gcs_file_path": f"parsed/air_title_v/"
                            f"{constants.CURRENT_DATE}/air_title_v.json",
    "data_source": "arcgis_apis",
    "ingestion_layer": "bq_wh_job_audit",
    "layer_name": "air_title_v",
    "layer_url": "https://services6.arcgis.com/DZHaqZm9cxOD4CWM/ArcGIS/"
                 "rest/services/CLCPA_ATV/FeatureServer/0"
  },
  {
    "task_name": "air_facilities_system_bq_wh_job_audit_ingestion",
    "query":
      f" SELECT COUNT(*) AS COUNT FROM "
      f"{constants.BQ_WH_DATASET}.arcgis_air_facilities_system "
      f"WHERE ingestion_timestamp = ",
    "bq_table_name": f"{constants.BQ_WH_DATASET}.arcgis_air_facilities_system",
    "gcs_bucket_name": constants.ARCGIS_BUCKET_NAME,
    "parsed_gcs_file_path": f"parsed/air_facilities_system/"
                            f"{constants.CURRENT_DATE}/"
                            f"air_facilities_system.json",
    "data_source": "arcgis_apis",
    "ingestion_layer": "bq_wh_job_audit",
    "layer_name": "air_facilities_system",
    "layer_url": "https://services6.arcgis.com/DZHaqZm9cxOD4CWM/ArcGIS/"
                 "rest/services/CLCPA_ASF/FeatureServer/0",
  },
  {
    "task_name":
      "air_facility_registration_bq_wh_job_audit_ingestion",
    "query":
      f" SELECT COUNT(*) AS COUNT FROM "
      f"{constants.BQ_WH_DATASET}.arcgis_air_facility_registration"
      f" WHERE ingestion_timestamp = ",
    "bq_table_name":
      f"{constants.BQ_WH_DATASET}.arcgis_air_facility_registration",
    "gcs_bucket_name": constants.ARCGIS_BUCKET_NAME,
    "parsed_gcs_file_path": f"parsed/air_facility_registration/"
                            f"{constants.CURRENT_DATE}/"
                            f"air_facility_registration.json",
    "data_source": "arcgis_apis",
    "ingestion_layer": "bq_wh_job_audit",
    "layer_name": "air_facility_registration",
    "layer_url": "https://services6.arcgis.com/DZHaqZm9cxOD4CWM/ArcGIS/"
                 "rest/services/CLCPA_AFR/FeatureServer/0",
  },
  {
    "task_name":
      "major_oil_storage_facilities_bq_wh_job_audit_ingestion",
    "query":
      f" SELECT COUNT(*) AS COUNT FROM "
      f"{constants.BQ_WH_DATASET}.arcgis_major_oil_storage_facilities "
      f"WHERE ingestion_timestamp = ",
    "bq_table_name":
      f"{constants.BQ_WH_DATASET}.arcgis_major_oil_storage_facilities",
    "gcs_bucket_name": constants.ARCGIS_BUCKET_NAME,
    "parsed_gcs_file_path": f"parsed/major_oil_storage_facilities/"
                            f"{constants.CURRENT_DATE}/"
                            f"major_oil_storage_facilities.json",
    "data_source": "arcgis_apis",
    "ingestion_layer": "bq_wh_job_audit",
    "layer_name": "major_oil_storage_facilities",
    "layer_url": "https://services6.arcgis.com/DZHaqZm9cxOD4CWM/ArcGIS"
                 "/rest/services/Major_Oil_Storage_Facility/FeatureServer/0",
  },

  # REPORTING ARCGIS BQ INGESTION
  {
    "task_name": "nursing_homes_reporting_ingestion",
    "data_source": "arcgis_apis",
    "ingestion_layer": "bq_reporting",
    "source_table_name":
      f" SELECT * FROM {constants.REPORTING_VIEWS}."
      f"vw_arcgis_nursing_homes where ingestion_timestamp = ",
    "reporting_table_name":
      f"{constants.BQ_REPORTING_DATASET}.arcgis_nursing_homes",
    "layer_name": "nursing_homes",
    "layer_url": "https://services1.arcgis.com/Hp6G80Pky0om7QvQ/"
                 "ArcGIS/rest/services/NursingHomes/FeatureServer/0"

  },
  {
    "task_name": "remediation_sites_reporting_ingestion",
    "data_source": "arcgis_apis",
    "ingestion_layer": "bq_reporting",
    "source_table_name": f" SELECT * FROM {constants.REPORTING_VIEWS}."
                         f"vw_arcgis_remediation_sites "
                         f"where ingestion_timestamp = ",
    "reporting_table_name":
      f"{constants.BQ_REPORTING_DATASET}.arcgis_remediation_sites",
    "layer_name": "remediation_sites",
    "layer_url": "https://services6.arcgis.com/DZHaqZm9cxOD4CWM/"
                 "ArcGIS/rest/services/Remediation_Sites/FeatureServer/0"

  },
  {
    "task_name": "remediation_boundaries_reporting_ingestion",
    "data_source": "arcgis_apis",
    "ingestion_layer": "bq_reporting",
    "source_table_name": f" SELECT * FROM {constants.REPORTING_VIEWS}."
                         f"vw_arcgis_remediation_boundaries "
                         f"where ingestion_timestamp = ",
    "reporting_table_name":
      f"{constants.BQ_REPORTING_DATASET}.arcgis_remediation_"
      f"boundaries",
    "layer_name": "remediation_boundaries",
    "layer_url": "https://services6.arcgis.com/DZHaqZm9cxOD4CWM/ArcGIS/"
                 "rest/services/Remediation_Boundaries/FeatureServer/0",
  },
  {
    "task_name": "air_title_v_reporting_ingestion",
    "data_source": "arcgis_apis",
    "ingestion_layer": "bq_reporting",
    "source_table_name": f" SELECT * FROM {constants.REPORTING_VIEWS}."
                         f"vw_arcgis_atv_total_emissions_submitted "
                         f"where ingestion_timestamp = ",
    "reporting_table_name":
      f"{constants.BQ_REPORTING_DATASET}."
      f"arcgis_atv_total_emissions_submitted",

    "layer_name": "air_title_v",
    "layer_url": "https://services6.arcgis.com/DZHaqZm9cxOD4CWM/ArcGIS/"
                 "rest/services/CLCPA_ATV/FeatureServer/0"
  },
  {
    "task_name": "air_facilities_system_reporting_ingestion",
    "data_source": "arcgis_apis",
    "ingestion_layer": "bq_reporting",
    "source_table_name": f" SELECT * FROM {constants.REPORTING_VIEWS}."
                         f"vw_arcgis_air_facilities_system "
                         f"where ingestion_timestamp = ",
    "reporting_table_name":
      f"{constants.BQ_REPORTING_DATASET}."
      f"arcgis_air_facilities_system",
    "layer_name": "air_facilities_system",
    "layer_url": "https://services6.arcgis.com/DZHaqZm9cxOD4CWM/ArcGIS/"
                 "rest/services/CLCPA_ASF/FeatureServer/0",

  },
  {
    "task_name": "air_facility_registration_reporting_ingestion",
    "data_source": "arcgis_apis",
    "ingestion_layer": "bq_reporting",
    "source_table_name": f" SELECT * FROM {constants.REPORTING_VIEWS}."
                         f"vw_arcgis_air_facility_registration "
                         f"where ingestion_timestamp = ",
    "reporting_table_name":
      f"{constants.BQ_REPORTING_DATASET}."
      f"arcgis_air_facility_registration",
    "layer_name": "air_facility_registration",
    "layer_url": "https://services6.arcgis.com/DZHaqZm9cxOD4CWM/ArcGIS/"
                 "rest/services/CLCPA_AFR/FeatureServer/0",

  },
  {
    "task_name": "major_oil_storage_facilities_reporting_ingestion",
    "data_source": "arcgis_apis",
    "ingestion_layer": "bq_reporting",
    "source_table_name": f" SELECT * FROM {constants.REPORTING_VIEWS}."
                         f"vw_arcgis_major_oil_storage_facilities "
                         f"where ingestion_timestamp = ",
    "reporting_table_name":
      f"{constants.BQ_REPORTING_DATASET}."
      f"arcgis_major_oil_storage_facilities",
    "layer_name": "major_oil_storage_facilities",
    "layer_url": "https://services6.arcgis.com/DZHaqZm9cxOD4CWM/ArcGIS"
                 "/rest/services/Major_Oil_Storage_Facility/FeatureServer/0",

  },

  # ARCGIS JOB_AUDIT REPORTING BQ INGESTION
  {
    "task_name": "nursing_homes_bq_reporting_job_audit_ingestion",
    "bq_table_name": f"{constants.BQ_REPORTING_DATASET}.arcgis_nursing_homes",
    "query": f" SELECT COUNT(*) AS COUNT FROM "
             f"{constants.BQ_REPORTING_DATASET}."
             f"arcgis_nursing_homes WHERE ingestion_timestamp = ",
    "gcs_bucket_name": constants.ARCGIS_BUCKET_NAME,
    "parsed_gcs_file_path": f"parsed/nursing_homes/"
                            f"{constants.CURRENT_DATE}/nursing_homes.json",
    "data_source": "arcgis_apis",
    "ingestion_layer": "bq_reporting_job_audit",
    "layer_name": "nursing_homes",
    "layer_url": "https://services1.arcgis.com/Hp6G80Pky0om7QvQ/"
                 "ArcGIS/rest/services/NursingHomes/FeatureServer/0"
  },
  {
    "task_name": "remediation_sites_bq_reporting_job_audit_ingestion",
    "query":
      f" SELECT COUNT(*) AS COUNT FROM "
      f"{constants.BQ_REPORTING_DATASET}.arcgis_remediation_sites "
      f"WHERE ingestion_timestamp = ",
    "bq_table_name": f"{constants.BQ_REPORTING_DATASET}"
                     f".arcgis_remediation_sites",
    "gcs_bucket_name": constants.ARCGIS_BUCKET_NAME,
    "parsed_gcs_file_path": f"parsed/remediation_sites/"
                            f"{constants.CURRENT_DATE}/"
                            f"remediation_sites.json",
    "data_source": "arcgis_apis",
    "ingestion_layer": "bq_reporting_job_audit",
    "layer_name": "remediation_sites",
    "layer_url": "https://services6.arcgis.com/DZHaqZm9cxOD4CWM/"
                 "ArcGIS/rest/services/Remediation_Sites/FeatureServer/0"
  },
  {
    "task_name": "remediation_boundaries_bq_reporting_job_audit_ingestion",
    "query":
      f" SELECT COUNT(*) AS COUNT FROM "
      f"{constants.BQ_REPORTING_DATASET}.arcgis_remediation_boundaries"
      f" WHERE ingestion_timestamp = ",
    "bq_table_name": f"{constants.BQ_REPORTING_DATASET}"
                     f".argics_remediation_boundaries",
    "gcs_bucket_name": constants.ARCGIS_BUCKET_NAME,
    "parsed_gcs_file_path": f"parsed/remediation_boundaries/"
                            f"{constants.CURRENT_DATE}/"
                            f"remediation_boundaries.json",
    "data_source": "arcgis_apis",
    "ingestion_layer": "bq_reporting_job_audit",
    "layer_name": "remediation_boundaries",
    "layer_url": "https://services6.arcgis.com/DZHaqZm9cxOD4CWM/ArcGIS/"
                 "rest/services/Remediation_Boundaries/FeatureServer/0",
  },
  {
    "task_name": "air_title_v_bq_reporting_job_audit_ingestion",
    "query":
      f" SELECT COUNT(*) AS COUNT FROM "
      f"{constants.BQ_REPORTING_DATASET}."
      f"arcgis_atv_total_emissions_submitted "
      f"WHERE ingestion_timestamp = ",
    "bq_table_name": f"{constants.BQ_REPORTING_DATASET}."
                     f"arcgis_atv_total_emissions_submitted",
    "gcs_bucket_name": constants.ARCGIS_BUCKET_NAME,
    "parsed_gcs_file_path": f"parsed/air_title_v/"
                            f"{constants.CURRENT_DATE}/air_title_v.json",
    "data_source": "arcgis_apis",
    "ingestion_layer": "bq_reporting_job_audit",
    "layer_name": "air_title_v",
    "layer_url": "https://services6.arcgis.com/DZHaqZm9cxOD4CWM/ArcGIS/"
                 "rest/services/CLCPA_ATV/FeatureServer/0"
  },
  {
    "task_name": "air_facilities_system_bq_reporting_job_audit_ingestion",
    "query":
      f" SELECT COUNT(*) AS COUNT FROM "
      f"{constants.BQ_REPORTING_DATASET}."
      f"arcgis_air_facilities_system "
      f"WHERE ingestion_timestamp = ",
    "bq_table_name": f"{constants.BQ_REPORTING_DATASET}"
                     f".arcgis_air_facilities_system",
    "gcs_bucket_name": constants.ARCGIS_BUCKET_NAME,
    "parsed_gcs_file_path": f"parsed/air_facilities_system/"
                            f"{constants.CURRENT_DATE}/"
                            f"air_facilities_system.json",
    "data_source": "arcgis_apis",
    "ingestion_layer": "bq_reporting_job_audit",
    "layer_name": "air_facilities_system",
    "layer_url": "https://services6.arcgis.com/DZHaqZm9cxOD4CWM/ArcGIS/"
                 "rest/services/CLCPA_ASF/FeatureServer/0",
  },
  {
    "task_name":
      "air_facility_registration_bq_reporting_job_audit_ingestion",
    "query":
      f" SELECT COUNT(*) AS COUNT FROM "
      f"{constants.BQ_REPORTING_DATASET}."
      f"arcgis_air_facility_registration"
      f" WHERE ingestion_timestamp = ",
    "bq_table_name":
      f"{constants.BQ_REPORTING_DATASET}.arcgis_air_facility_registration",
    "gcs_bucket_name": constants.ARCGIS_BUCKET_NAME,
    "parsed_gcs_file_path": f"parsed/air_facility_registration/"
                            f"{constants.CURRENT_DATE}/"
                            f"air_facility_registration.json",
    "data_source": "arcgis_apis",
    "ingestion_layer": "bq_reporting_job_audit",
    "layer_name": "air_facility_registration",
    "layer_url": "https://services6.arcgis.com/DZHaqZm9cxOD4CWM/ArcGIS/"
                 "rest/services/CLCPA_AFR/FeatureServer/0",
  },
  {
    "task_name":
      "major_oil_storage_facilities_bq_reporting_job_audit_ingestion",
    "query":
      f" SELECT COUNT(*) AS COUNT FROM "
      f"{constants.BQ_REPORTING_DATASET}."
      f"arcgis_major_oil_storage_facilities"
      f" WHERE ingestion_timestamp = ",
    "bq_table_name":
      f"{constants.BQ_REPORTING_DATASET}."
      f"arcgis_major_oil_storage_facilities",
    "gcs_bucket_name": constants.ARCGIS_BUCKET_NAME,
    "parsed_gcs_file_path": f"parsed/major_oil_storage_facilities/"
                            f"{constants.CURRENT_DATE}/"
                            f"major_oil_storage_facilities.json",
    "data_source": "arcgis_apis",
    "ingestion_layer": "bq_reporting_job_audit",
    "layer_name": "major_oil_storage_facilities",
    "layer_url": "https://services6.arcgis.com/DZHaqZm9cxOD4CWM/ArcGIS"
                 "/rest/services/Major_Oil_Storage_Facility/FeatureServer/0",
  },

]

SOCRATA_TASKS_CONFIG = [
  # SOCRATA RAW GCS INGESTION MAIN TASKS
  {
    "task_name": "adult_care_facility_map_raw_ingestion",
    "data_source": "socrata",
    "ingestion_layer": "gcs_raw",
    "service_endpoint": constants.SOCRATA_CLOUD_RUN_SERVICE_ENDPOINT
                        + "/process_raw_layer?"
                          "layer_name=adult_care_facility_map&"
                          "batch_timestamp={}&batch_unix_timestamp={}&"
                          f"bucket={constants.SOCRATA_BUCKET_NAME}",
  },
  {
    "task_name": "health_facility_general_information_raw_ingestion",
    "data_source": "socrata",
    "ingestion_layer": "gcs_raw",
    "service_endpoint": constants.SOCRATA_CLOUD_RUN_SERVICE_ENDPOINT
                        + "/process_raw_layer?"
                          "layer_name=health_facility_general_information&"
                          "batch_timestamp={}&batch_unix_timestamp={}&"
                          f"bucket={constants.SOCRATA_BUCKET_NAME}",
  },
  {
    "task_name": "health_facility_map_raw_ingestion",
    "data_source": "socrata",
    "ingestion_layer": "gcs_raw",
    "service_endpoint": constants.SOCRATA_CLOUD_RUN_SERVICE_ENDPOINT
                        + "/process_raw_layer?"
                          "layer_name=health_facility_map&"
                          "batch_timestamp={}&batch_unix_timestamp={}&"
                          f"bucket={constants.SOCRATA_BUCKET_NAME}",
  },
  {
    "task_name":
      "nyc_health_hospitals_patient_care_locations_2011_raw_ingestion",
    "data_source": "socrata",
    "ingestion_layer": "gcs_raw",
    "service_endpoint": constants.SOCRATA_CLOUD_RUN_SERVICE_ENDPOINT
                        + "/process_raw_layer?layer_name"
                          "=nyc_health_hospitals_patient_care_locations_2011&"
                          "batch_timestamp={}&batch_unix_timestamp={}&"
                          f"bucket={constants.SOCRATA_BUCKET_NAME}",
  },
  {
    "task_name": "archived_parks_properties_raw_ingestion",
    "data_source": "socrata",
    "ingestion_layer": "gcs_raw",
    "service_endpoint": constants.SOCRATA_CLOUD_RUN_SERVICE_ENDPOINT
                        + "/process_raw_layer?"
                          "layer_name=archived_parks_properties&"
                          "batch_timestamp={}&batch_unix_timestamp={}&"
                          f"bucket={constants.SOCRATA_BUCKET_NAME}",
  },
  {
    "task_name": "athletic_facilities_raw_ingestion",
    "data_source": "socrata",
    "ingestion_layer": "gcs_raw",
    "service_endpoint": constants.SOCRATA_CLOUD_RUN_SERVICE_ENDPOINT
                        + "/process_raw_layer?"
                          "layer_name=athletic_facilities&"
                          "batch_timestamp={}&batch_unix_timestamp={}&"
                          f"bucket={constants.SOCRATA_BUCKET_NAME}",
  },
  {
    "task_name": "child_care_regulated_programs_raw_ingestion",
    "data_source": "socrata",
    "ingestion_layer": "gcs_raw",
    "service_endpoint": constants.SOCRATA_CLOUD_RUN_SERVICE_ENDPOINT
                        + "/process_raw_layer?"
                          "layer_name=child_care_regulated_programs&"
                          "batch_timestamp={}&batch_unix_timestamp={}&"
                          f"bucket={constants.SOCRATA_BUCKET_NAME}",
  },
  {
    "task_name": "day_care_center_raw_ingestion",
    "data_source": "socrata",
    "ingestion_layer": "gcs_raw",
    "service_endpoint": constants.SOCRATA_CLOUD_RUN_SERVICE_ENDPOINT
                        + "/process_raw_layer?layer_name=day_care_center&"
                          "batch_timestamp={}&batch_unix_timestamp={}&"
                          f"bucket={constants.SOCRATA_BUCKET_NAME}",
  },
  # SOCRATA PARSE GCS INGESTION MAIN TASKS
  {
    "task_name": "adult_care_facility_map_parse_ingestion",
    "data_source": "socrata",
    "ingestion_layer": "gcs_parse",
    "service_endpoint": f"{constants.SOCRATA_CLOUD_RUN_SERVICE_ENDPOINT}"
                        f"/process_parse_layer?layer_name="
                        f"adult_care_facility_map"
                        f"&raw_gcs_ingestion_date={constants.CURRENT_DATE}"
                        "&batch_timestamp={}&batch_unix_timestamp={}"
                        f"&bucket={constants.SOCRATA_BUCKET_NAME}",
  },
  {
    "task_name": "health_facility_general_information_parse_ingestion",
    "data_source": "socrata",
    "ingestion_layer": "gcs_parse",
    "service_endpoint": f"{constants.SOCRATA_CLOUD_RUN_SERVICE_ENDPOINT}"
                        f"/process_parse_layer?layer_name="
                        f"health_facility_general_information"
                        f"&raw_gcs_ingestion_date={constants.CURRENT_DATE}"
                        "&batch_timestamp={}&batch_unix_timestamp={}"
                        f"&bucket={constants.SOCRATA_BUCKET_NAME}",

  },
  {
    "task_name": "health_facility_map_parse_ingestion",
    "data_source": "socrata",
    "ingestion_layer": "gcs_parse",
    "service_endpoint": f"{constants.SOCRATA_CLOUD_RUN_SERVICE_ENDPOINT}"
                        f"/process_parse_layer?layer_name="
                        f"health_facility_map"
                        f"&raw_gcs_ingestion_date={constants.CURRENT_DATE}"
                        "&batch_timestamp={}&batch_unix_timestamp={}"
                        f"&bucket={constants.SOCRATA_BUCKET_NAME}",
  },
  {
    "task_name":
      "nyc_health_hospitals_patient_care_locations_2011_parse_ingestion",
    "data_source": "socrata",
    "ingestion_layer": "gcs_parse",
    "service_endpoint": f"{constants.SOCRATA_CLOUD_RUN_SERVICE_ENDPOINT}"
                        f"/process_parse_layer?layer_name="
                        f"nyc_health_hospitals_patient_care_locations_2011"
                        f"&raw_gcs_ingestion_date={constants.CURRENT_DATE}"
                        "&batch_timestamp={}&batch_unix_timestamp={}"
                        f"&bucket={constants.SOCRATA_BUCKET_NAME}",
  },
  {
    "task_name": "archived_parks_properties_parse_ingestion",
    "data_source": "socrata",
    "ingestion_layer": "gcs_parse",
    "service_endpoint": f"{constants.SOCRATA_CLOUD_RUN_SERVICE_ENDPOINT}"
                        f"/process_parse_layer?layer_name="
                        f"archived_parks_properties"
                        f"&raw_gcs_ingestion_date={constants.CURRENT_DATE}"
                        "&batch_timestamp={}&batch_unix_timestamp={}"
                        f"&bucket={constants.SOCRATA_BUCKET_NAME}",

  },
  {
    "task_name": "athletic_facilities_parse_ingestion",
    "data_source": "socrata",
    "ingestion_layer": "gcs_parse",
    "service_endpoint": f"{constants.SOCRATA_CLOUD_RUN_SERVICE_ENDPOINT}"
                        f"/process_parse_layer?layer_name="
                        f"athletic_facilities"
                        f"&raw_gcs_ingestion_date={constants.CURRENT_DATE}"
                        "&batch_timestamp={}&batch_unix_timestamp={}"
                        f"&bucket={constants.SOCRATA_BUCKET_NAME}",
  },
  {
    "task_name": "child_care_regulated_programs_parse_ingestion",
    "data_source": "socrata",
    "ingestion_layer": "gcs_parse",
    "service_endpoint": f"{constants.SOCRATA_CLOUD_RUN_SERVICE_ENDPOINT}"
                        f"/process_parse_layer?layer_name="
                        f"child_care_regulated_programs"
                        f"&raw_gcs_ingestion_date={constants.CURRENT_DATE}"
                        "&batch_timestamp={}&batch_unix_timestamp={}"
                        f"&bucket={constants.SOCRATA_BUCKET_NAME}",
  },
  {
    "task_name": "day_care_center_parse_ingestion",
    "data_source": "socrata",
    "ingestion_layer": "gcs_parse",
    "service_endpoint": f"{constants.SOCRATA_CLOUD_RUN_SERVICE_ENDPOINT}"
                        f"/process_parse_layer?layer_name=day_care_center"
                        f"&raw_gcs_ingestion_date={constants.CURRENT_DATE}"
                        "&batch_timestamp={}&batch_unix_timestamp={}"
                        f"&bucket={constants.SOCRATA_BUCKET_NAME}",
  },
  # SOCRATA RAW BQ INGESTION

  {
    "task_name": "adult_care_facility_map_bq_raw_ingestion",
    "bq_table_name": f"{constants.SOCRATA_RAW_DATASET}."
                     f"adult_care_facility_map",
    "new_column_audit_table":
      f"{constants.BQ_METADATA_DATASET}.new_column_audit",
    "gcs_bucket_name": constants.SOCRATA_BUCKET_NAME,
    "parsed_gcs_file_path": f"parsed/adult_care_facility_map/"
                            f"{constants.CURRENT_DATE}/"
                            "adult_care_facility_map_{}.json",
    "data_source": "socrata",
    "ingestion_layer": "bq_raw",
    "layer_name": "adult_care_facility_map",
    "layer_url": "https://health.data.ny.gov/resource/"
                 "6wkx-ptu4.json?$select=count(*)",
  },
  {
    "task_name":
      "health_facility_general_information_bq_raw_ingestion",
    "bq_table_name": f"{constants.SOCRATA_RAW_DATASET}."
                     f"health_facility_general_information",
    "new_column_audit_table":
      f"{constants.BQ_METADATA_DATASET}.new_column_audit",
    "gcs_bucket_name": constants.SOCRATA_BUCKET_NAME,
    "parsed_gcs_file_path": f"parsed/health_facility_general_information/"
                            f"{constants.CURRENT_DATE}/"
                            "health_facility_general_information_{}.json",
    "data_source": "socrata",
    "ingestion_layer": "bq_raw",
    "layer_name": "health_facility_general_information",
    "layer_url": "https://health.data.ny.gov/"
                 "resource/vn5v-hh5r.json?$select=count(*)"
  },
  {
    "task_name": "health_facility_map_bq_raw_ingestion",
    "bq_table_name": f"{constants.SOCRATA_RAW_DATASET}.health_facility_map",
    "new_column_audit_table":
      f"{constants.BQ_METADATA_DATASET}.new_column_audit",
    "gcs_bucket_name": constants.SOCRATA_BUCKET_NAME,
    "parsed_gcs_file_path": f"parsed/health_facility_map/"
                            f"{constants.CURRENT_DATE}/"
                            "health_facility_map_{}.json",
    "data_source": "socrata",
    "ingestion_layer": "bq_raw",
    "layer_name": "health_facility_map",
    "layer_url": "https://health.data.ny.gov/"
                 "resource/875v-tpc8.json?$select=count(*)"
  },
  {
    "task_name":
      "nyc_health_hospitals_patient_care_locations_2011_bq_raw_ingestion",
    "bq_table_name": f"{constants.SOCRATA_RAW_DATASET}."
                     f"nyc_health_hospitals_patient_care_locations_2011",
    "new_column_audit_table":
      f"{constants.BQ_METADATA_DATASET}.new_column_audit",
    "gcs_bucket_name": constants.SOCRATA_BUCKET_NAME,
    "parsed_gcs_file_path": f"parsed/"
                            f"nyc_health_hospitals_patient_care_"
                            f"locations_2011/"
                            f"{constants.CURRENT_DATE}/"
                            f"nyc_health_hospitals_patient_care_"
                            "locations_2011_{}.json",
    "data_source": "socrata",
    "ingestion_layer": "bq_raw",
    "layer_name": "nyc_health_hospitals_patient_care_"
                  "locations_2011",
    "layer_url": "https://data.cityofnewyork.us/"
                 "resource/f7b6-v6v3.json?$select=count(*)"
  },
  {
    "task_name": "archived_parks_properties_bq_raw_ingestion",
    "bq_table_name": f"{constants.SOCRATA_RAW_DATASET}."
                     f"archived_parks_properties",
    "new_column_audit_table":
      f"{constants.BQ_METADATA_DATASET}.new_column_audit",
    "gcs_bucket_name": constants.SOCRATA_BUCKET_NAME,
    "parsed_gcs_file_path": f"parsed/archived_parks_properties/"
                            f"{constants.CURRENT_DATE}/"
                            "archived_parks_properties_{}.json",
    "data_source": "socrata",
    "ingestion_layer": "bq_raw",
    "layer_name": "archived_parks_properties",
    "layer_url": "https://data.cityofnewyork.us/"
                 "resource/ghu2-eden.json?$select=count(*)"
  },
  {
    "task_name": "athletic_facilities_bq_raw_ingestion",
    "bq_table_name": f"{constants.SOCRATA_RAW_DATASET}.athletic_facilities",
    "new_column_audit_table":
      f"{constants.BQ_METADATA_DATASET}.new_column_audit",
    "gcs_bucket_name": constants.SOCRATA_BUCKET_NAME,
    "parsed_gcs_file_path": f"parsed/athletic_facilities/"
                            f"{constants.CURRENT_DATE}/"
                            "athletic_facilities_{}.json",
    "data_source": "socrata",
    "ingestion_layer": "bq_raw",
    "layer_name": "athletic_facilities",
    "layer_url": "https://data.cityofnewyork.us/resource"
                 "/9wwi-sb8x.json?$select=count(*)",
  },
  {
    "task_name": "child_care_regulated_programs_bq_raw_ingestion",
    "bq_table_name": f"{constants.SOCRATA_RAW_DATASET}."
                     f"child_care_regulated_programs",
    "new_column_audit_table":
      f"{constants.BQ_METADATA_DATASET}.new_column_audit",
    "gcs_bucket_name": constants.SOCRATA_BUCKET_NAME,
    "parsed_gcs_file_path": f"parsed/child_care_regulated_programs/"
                            f"{constants.CURRENT_DATE}/"
                            "child_care_regulated_programs_{}.json",
    "data_source": "socrata",
    "ingestion_layer": "bq_raw",
    "layer_name": "child_care_regulated_programs",
    "layer_url":
      "https://data.ny.gov/resource/cb42-qumz.json?$select=count(*)"
  },
  {
    "task_name": "day_care_center_bq_raw_ingestion",
    "bq_table_name": f"{constants.SOCRATA_RAW_DATASET}.day_care_center",
    "new_column_audit_table":
      f"{constants.BQ_METADATA_DATASET}.new_column_audit",
    "gcs_bucket_name": constants.SOCRATA_BUCKET_NAME,
    "parsed_gcs_file_path": f"parsed/day_care_center/"
                            f"{constants.CURRENT_DATE}/"
                            "day_care_center_{}.json",
    "data_source": "socrata",
    "ingestion_layer": "bq_raw",
    "layer_name": "day_care_center",
    "layer_url": "https://data.cityofnewyork.us/"
                 "resource/sd93-evwm.json?$select=count(*)",
  },
  # SOCRATA JOB AUDIT RAW BQ INGESTION

  {
    "task_name":
      "adult_care_facility_map_bq_raw_job_audit_ingestion",
    "query":
      f" SELECT COUNT(*) AS COUNT FROM {constants.SOCRATA_RAW_DATASET}."
      f"adult_care_facility_map WHERE ingestion_timestamp = ",
    "bq_table_name": f"{constants.SOCRATA_RAW_DATASET}"
                     f".adult_care_facility_map",
    "gcs_bucket_name": constants.SOCRATA_BUCKET_NAME,
    "parsed_gcs_file_path": f"parsed/adult_care_facility_map/"
                            f"{constants.CURRENT_DATE}/"
                            f"adult_care_facility_map.json",
    "data_source": "socrata",
    "ingestion_layer": "bq_raw_job_audit",
    "layer_name": "adult_care_facility_map",
    "layer_url": "https://health.data.ny.gov/resource/"
                 "6wkx-ptu4.json?$select=count(*)",
  },
  {
    "task_name":
      "health_facility_general_information_"
      "bq_raw_job_audit_ingestion",
    "query": f" SELECT COUNT(*) AS COUNT FROM "
             f"{constants.SOCRATA_RAW_DATASET}."
             f"health_facility_general_information "
             f"WHERE ingestion_timestamp = ",
    "bq_table_name": f"{constants.SOCRATA_RAW_DATASET}."
                     f"health_facility_general_information",
    "gcs_bucket_name": constants.SOCRATA_BUCKET_NAME,
    "parsed_gcs_file_path": f"parsed/health_facility_general_information/"
                            f"{constants.CURRENT_DATE}/"
                            f"health_facility_general_information.json",
    "data_source": "socrata",
    "ingestion_layer": "bq_raw_job_audit",
    "layer_name": "health_facility_general_information",
    "layer_url": "https://health.data.ny.gov/"
                 "resource/vn5v-hh5r.json?$select=count(*)"
  },
  {
    "task_name": "health_facility_map_bq_raw_job_audit_ingestion",
    "query": f" SELECT COUNT(*) AS COUNT FROM "
             f"{constants.SOCRATA_RAW_DATASET}"
             f".health_facility_map "
             f"WHERE ingestion_timestamp = ",
    "bq_table_name": f"{constants.SOCRATA_RAW_DATASET}"
                     f".health_facility_map",
    "gcs_bucket_name": constants.SOCRATA_BUCKET_NAME,
    "parsed_gcs_file_path": f"parsed/health_facility_map/"
                            f"{constants.CURRENT_DATE}/"
                            f"health_facility_map.json",
    "data_source": "socrata",
    "ingestion_layer": "bq_raw_job_audit",
    "layer_name": "health_facility_map",
    "layer_url": "https://health.data.ny.gov/"
                 "resource/875v-tpc8.json?$select=count(*)"
  },
  {
    "task_name":
      "nyc_health_hospitals_patient_care_locations_2011_"
      "bq_raw_job_audit_ingestion",
    "query": f" SELECT COUNT(*) AS COUNT FROM "
             f"{constants.SOCRATA_RAW_DATASET}."
             f"nyc_health_hospitals_patient_care_locations_2011"
             f" WHERE ingestion_timestamp = ",
    "bq_table_name": f"{constants.SOCRATA_RAW_DATASET}."
                     f"nyc_health_hospitals_patient_care_locations_2011",
    "gcs_bucket_name": constants.SOCRATA_BUCKET_NAME,
    "parsed_gcs_file_path": f"parsed/"
                            f"nyc_health_hospitals_patient_care_"
                            f"locations_2011/"
                            f"{constants.CURRENT_DATE}/"
                            f"nyc_health_hospitals_patient_care_"
                            f"locations_2011.json",
    "data_source": "socrata",
    "ingestion_layer": "bq_raw_job_audit",
    "layer_name": "nyc_health_hospitals_patient_care_"
                  "locations_2011",
    "layer_url": "https://data.cityofnewyork.us/"
                 "resource/f7b6-v6v3.json?$select=count(*)"
  },
  {
    "task_name": "archived_parks_properties_bq_raw_job_audit_ingestion",
    "query": f" SELECT COUNT(*) AS COUNT FROM "
             f"{constants.SOCRATA_RAW_DATASET}."
             f"archived_parks_properties "
             f"WHERE ingestion_timestamp = ",
    "bq_table_name":
      f"{constants.SOCRATA_RAW_DATASET}.archived_parks_properties",
    "gcs_bucket_name": constants.SOCRATA_BUCKET_NAME,
    "parsed_gcs_file_path": f"parsed/archived_parks_properties/"
                            f"{constants.CURRENT_DATE}/"
                            f"archived_parks_properties.json",
    "data_source": "socrata",
    "ingestion_layer": "bq_raw_job_audit",
    "layer_name": "archived_parks_properties",
    "layer_url": "https://data.cityofnewyork.us/"
                 "resource/ghu2-eden.json?$select=count(*)"
  },
  {
    "task_name": "athletic_facilities_bq_raw_job_audit_ingestion",
    "query": f" SELECT COUNT(*) AS COUNT FROM "
             f"{constants.SOCRATA_RAW_DATASET}"
             f".athletic_facilities "
             f"WHERE ingestion_timestamp = ",
    "bq_table_name": f"{constants.SOCRATA_RAW_DATASET}.athletic_facilities",
    "gcs_bucket_name": constants.SOCRATA_BUCKET_NAME,
    "parsed_gcs_file_path": f"parsed/athletic_facilities/"
                            f"{constants.CURRENT_DATE}/"
                            f"athletic_facilities.json",
    "data_source": "socrata",
    "ingestion_layer": "bq_raw_job_audit",
    "layer_name": "athletic_facilities",
    "layer_url": "https://data.cityofnewyork.us/resource"
                 "/9wwi-sb8x.json?$select=count(*)",
  },
  {
    "task_name":
      "child_care_regulated_programs_bq_raw_job_audit_ingestion",
    "query": f" SELECT COUNT(*) AS COUNT FROM "
             f"{constants.SOCRATA_RAW_DATASET}."
             f"child_care_regulated_programs "
             f"WHERE ingestion_timestamp = ",
    "bq_table_name": f"{constants.SOCRATA_RAW_DATASET}."
                     f"child_care_regulated_programs",
    "gcs_bucket_name": constants.SOCRATA_BUCKET_NAME,
    "parsed_gcs_file_path": f"parsed/child_care_regulated_programs/"
                            f"{constants.CURRENT_DATE}/"
                            f"child_care_regulated_programs.json",
    "data_source": "socrata",
    "ingestion_layer": "bq_raw_job_audit",
    "layer_name": "child_care_regulated_programs",
    "layer_url":
      "https://data.ny.gov/resource/cb42-qumz.json?$select=count(*)"
  },
  {
    "task_name": "day_care_center_bq_raw_job_audit_ingestion",
    "query": f" SELECT COUNT(*) AS COUNT FROM "
             f"{constants.SOCRATA_RAW_DATASET}"
             f".day_care_center "
             f"WHERE ingestion_timestamp = ",
    "bq_table_name": f"{constants.SOCRATA_RAW_DATASET}.day_care_center",
    "gcs_bucket_name": constants.SOCRATA_BUCKET_NAME,
    "parsed_gcs_file_path": f"parsed/day_care_center/"
                            f"{constants.CURRENT_DATE}/"
                            f"day_care_center.json",
    "data_source": "socrata",
    "ingestion_layer": "bq_raw_job_audit",
    "layer_name": "day_care_center",
    "layer_url": "https://data.cityofnewyork.us/"
                 "resource/sd93-evwm.json?$select=count(*)",
  },

  # SOCRATA WH BQ INGESTION
  {
    "task_name": "adult_care_facility_map_wh_ingestion",
    "bq_table_name":
      f" SELECT * FROM {constants.SOCRATA_RAW_DATASET}"
      f".adult_care_facility_map",
    "data_source": "socrata",
    "ingestion_layer": "bq_warehouse",
    "layer_name": "adult_care_facility_map",
    "warehouse_table_name":
      f"{constants.BQ_WH_DATASET}.socrata_adult_care_facility_map",
    "layer_url": "https://health.data.ny.gov/resource/"
                 "6wkx-ptu4.json?$select=count(*)",

  },
  {
    "task_name": "health_facility_general_information_wh_ingestion",
    "bq_table_name":
      f" SELECT * FROM {constants.SOCRATA_RAW_DATASET}."
      f"health_facility_general_information",
    "data_source": "socrata",
    "ingestion_layer": "bq_warehouse",
    "layer_name": "health_facility_general_information",
    "warehouse_table_name":
      f"{constants.BQ_WH_DATASET}."
      f"socrata_health_facility_general_information",
    "layer_url": "https://health.data.ny.gov/"
                 "resource/vn5v-hh5r.json?$select=count(*)",

  },
  {
    "task_name": "health_facility_map_wh_ingestion",
    "bq_table_name":
      f" SELECT * FROM {constants.SOCRATA_RAW_DATASET}"
      f".health_facility_map",
    "data_source": "socrata",
    "ingestion_layer": "bq_warehouse",
    "layer_name": "health_facility_map",
    "warehouse_table_name":
      f"{constants.BQ_WH_DATASET}.socrata_health_facility_map",
    "layer_url": "https://health.data.ny.gov/"
                 "resource/875v-tpc8.json?$select=count(*)"

  },
  {
    "task_name": "nyc_health_hospitals_patient_care_"
                 "locations_2011_wh_ingestion",
    "bq_table_name":
      f" SELECT * FROM {constants.SOCRATA_RAW_DATASET}."
      f"nyc_health_hospitals_patient_care_locations_2011",
    "data_source": "socrata",
    "ingestion_layer": "bq_warehouse",
    "layer_name": "nyc_health_hospitals_patient_care_locations_2011",
    "warehouse_table_name":
      f"{constants.BQ_WH_DATASET}."
      f"socrata_nyc_health_hospitals_patient_care_locations_2011",
    "layer_url": "https://data.cityofnewyork.us/"
                 "resource/f7b6-v6v3.json?$select=count(*)"

  },
  {
    "task_name": "archived_parks_properties_wh_ingestion",
    "bq_table_name":
      f" SELECT * FROM "
      f"{constants.SOCRATA_RAW_DATASET}.archived_parks_properties",
    "data_source": "socrata",
    "ingestion_layer": "bq_warehouse",
    "layer_name": "archived_parks_properties",
    "warehouse_table_name":
      f"{constants.BQ_WH_DATASET}.socrata_archived_parks_properties",
    "layer_url": "https://data.cityofnewyork.us/"
                 "resource/ghu2-eden.json?$select=count(*)"

  },
  {
    "task_name": "athletic_facilities_wh_ingestion",
    "bq_table_name":
      f" SELECT * FROM {constants.SOCRATA_RAW_DATASET}.athletic_facilities",
    "data_source": "socrata",
    "ingestion_layer": "bq_warehouse",
    "layer_name": "athletic_facilities",
    "warehouse_table_name":
      f"{constants.BQ_WH_DATASET}.socrata_athletic_facilities",
    "layer_url": "https://data.cityofnewyork.us/resource"
                 "/9wwi-sb8x.json?$select=count(*)",

  },
  {
    "task_name": "child_care_regulated_programs_wh_ingestion",
    "bq_table_name":
      f" SELECT * FROM "
      f"{constants.SOCRATA_RAW_DATASET}.child_care_regulated_programs",
    "data_source": "socrata",
    "ingestion_layer": "bq_warehouse",
    "layer_name": "child_care_regulated_programs",
    "warehouse_table_name":
      f"{constants.BQ_WH_DATASET}.socrata_child_care_regulated_programs",
    "layer_url":
      "https://data.ny.gov/resource/cb42-qumz.json?$select=count(*)"

  },
  {
    "task_name": "day_care_center_wh_ingestion",
    "bq_table_name":
      f" SELECT * FROM {constants.SOCRATA_RAW_DATASET}.day_care_center",
    "data_source": "socrata",
    "ingestion_layer": "bq_warehouse",
    "layer_name": "day_care_center",
    "warehouse_table_name":
      f"{constants.BQ_WH_DATASET}.socrata_day_care_center",
    "layer_url": "https://data.cityofnewyork.us/"
                 "resource/sd93-evwm.json?$select=count(*)",

  },
  # SOCRATA JOB AUDIT WH BQ INGESTION

  {
    "task_name":
      "adult_care_facility_map_bq_wh_job_audit_ingestion",
    "query":
      f" SELECT COUNT(*) AS COUNT FROM {constants.BQ_WH_DATASET}."
      f"socrata_adult_care_facility_map "
      f"WHERE ingestion_timestamp = ",
    "bq_table_name": f"{constants.BQ_WH_DATASET}"
                     f".socrata_adult_care_facility_map",
    "gcs_bucket_name": constants.SOCRATA_BUCKET_NAME,
    "parsed_gcs_file_path": f"parsed/adult_care_facility_map/"
                            f"{constants.CURRENT_DATE}/"
                            f"adult_care_facility_map.json",
    "data_source": "socrata",
    "ingestion_layer": "bq_wh_job_audit",
    "layer_name": "adult_care_facility_map",
    "layer_url": "https://health.data.ny.gov/resource/"
                 "6wkx-ptu4.json?$select=count(*)",
  },
  {
    "task_name":
      "health_facility_general_information_"
      "bq_wh_job_audit_ingestion",
    "query": f" SELECT COUNT(*) AS COUNT "
             f"FROM {constants.BQ_WH_DATASET}."
             f"socrata_health_facility"
             f"_general_information"
             f" WHERE ingestion_timestamp = ",
    "bq_table_name": f"{constants.BQ_WH_DATASET}."
                     f"socrata_health_facility_general_information",
    "gcs_bucket_name": constants.SOCRATA_BUCKET_NAME,
    "parsed_gcs_file_path": f"parsed/health_facility_general_information/"
                            f"{constants.CURRENT_DATE}/"
                            f"health_facility_general_information.json",
    "data_source": "socrata",
    "ingestion_layer": "bq_wh_job_audit",
    "layer_name": "health_facility_general_information",
    "layer_url": "https://health.data.ny.gov/"
                 "resource/vn5v-hh5r.json?$select=count(*)"
  },
  {
    "task_name": "health_facility_map_bq_wh_job_audit_ingestion",
    "query": f" SELECT COUNT(*) AS COUNT FROM "
             f"{constants.BQ_WH_DATASET}"
             f".socrata_health_facility_map"
             f" WHERE ingestion_timestamp = ",
    "bq_table_name": f"{constants.BQ_WH_DATASET}.socrata_health_facility_map",
    "gcs_bucket_name": constants.SOCRATA_BUCKET_NAME,
    "parsed_gcs_file_path": f"parsed/health_facility_map/"
                            f"{constants.CURRENT_DATE}/"
                            f"health_facility_map.json",
    "data_source": "socrata",
    "ingestion_layer": "bq_wh_job_audit",
    "layer_name": "health_facility_map",
    "layer_url": "https://health.data.ny.gov/"
                 "resource/875v-tpc8.json?$select=count(*)"
  },
  {
    "task_name":
      "nyc_health_hospitals_patient_care_locations_2011_"
      "bq_wh_job_audit_ingestion",
    "query": f" SELECT COUNT(*) AS COUNT FROM "
             f"{constants.BQ_WH_DATASET}."
             f"socrata_nyc_health_hospitals_"
             f"patient_care_locations_2011 "
             f"WHERE ingestion_timestamp = ",
    "bq_table_name": f"{constants.BQ_WH_DATASET}."
                     f"socrata_nyc_health_hospitals_"
                     f"patient_care_locations_2011",
    "gcs_bucket_name": constants.SOCRATA_BUCKET_NAME,
    "parsed_gcs_file_path": f"parsed/"
                            f"nyc_health_hospitals_patient_care_"
                            f"locations_2011/"
                            f"{constants.CURRENT_DATE}/"
                            f"nyc_health_hospitals_patient_care_"
                            f"locations_2011.json",
    "data_source": "socrata",
    "ingestion_layer": "bq_wh_job_audit",
    "layer_name": "nyc_health_hospitals_patient_care_"
                  "locations_2011",
    "layer_url": "https://data.cityofnewyork.us/"
                 "resource/f7b6-v6v3.json?$select=count(*)"
  },
  {
    "task_name": "archived_parks_properties_"
                 "bq_wh_job_audit_ingestion",
    "query": f" SELECT COUNT(*) AS COUNT "
             f"FROM {constants.BQ_WH_DATASET}."
             f"socrata_archived_parks_properties"
             f" WHERE ingestion_timestamp = ",
    "bq_table_name":
      f"{constants.BQ_WH_DATASET}.socrata_archived_parks_properties",
    "gcs_bucket_name": constants.SOCRATA_BUCKET_NAME,
    "parsed_gcs_file_path": f"parsed/archived_parks_properties/"
                            f"{constants.CURRENT_DATE}/"
                            f"archived_parks_properties.json",
    "data_source": "socrata",
    "ingestion_layer": "bq_wh_job_audit",
    "layer_name": "archived_parks_properties",
    "layer_url": "https://data.cityofnewyork.us/"
                 "resource/ghu2-eden.json?$select=count(*)"
  },
  {
    "task_name": "athletic_facilities_bq_wh_"
                 "job_audit_ingestion",
    "query": f" SELECT COUNT(*) AS COUNT FROM "
             f"{constants.BQ_WH_DATASET}"
             f".socrata_athletic_facilities "
             f"WHERE ingestion_timestamp = ",
    "bq_table_name": f"{constants.BQ_WH_DATASET}"
                     f".socrata_athletic_facilities",
    "gcs_bucket_name": constants.SOCRATA_BUCKET_NAME,
    "parsed_gcs_file_path": f"parsed/athletic_facilities/"
                            f"{constants.CURRENT_DATE}/"
                            f"athletic_facilities.json",
    "data_source": "socrata",
    "ingestion_layer": "bq_wh_job_audit",
    "layer_name": "athletic_facilities",
    "layer_url": "https://data.cityofnewyork.us/resource"
                 "/9wwi-sb8x.json?$select=count(*)",
  },
  {
    "task_name":
      "child_care_regulated_programs_bq_wh_job_audit_ingestion",
    "query": f" SELECT COUNT(*) AS COUNT FROM"
             f" {constants.BQ_WH_DATASET}."
             f"socrata_child_care_regulated_programs "
             f"WHERE ingestion_timestamp = ",
    "bq_table_name": f"{constants.SOCRATA_RAW_DATASET}."
                     f"socrata_child_care_regulated_programs",
    "gcs_bucket_name": constants.SOCRATA_BUCKET_NAME,
    "parsed_gcs_file_path": f"parsed/child_care_regulated_programs/"
                            f"{constants.CURRENT_DATE}/"
                            f"child_care_regulated_programs.json",
    "data_source": "socrata",
    "ingestion_layer": "bq_wh_job_audit",
    "layer_name": "child_care_regulated_programs",
    "layer_url":
      "https://data.ny.gov/resource/cb42-qumz.json?$select=count(*)"
  },
  {
    "task_name": "day_care_center_bq_wh_job_audit_ingestion",
    "query": f" SELECT COUNT(*) AS COUNT FROM "
             f"{constants.BQ_WH_DATASET}"
             f".socrata_day_care_center "
             f"WHERE ingestion_timestamp = ",
    "bq_table_name": f"{constants.BQ_WH_DATASET}.socrata_day_care_center",
    "gcs_bucket_name": constants.SOCRATA_BUCKET_NAME,
    "parsed_gcs_file_path": f"parsed/day_care_center/"
                            f"{constants.CURRENT_DATE}/"
                            f"day_care_center.json",
    "data_source": "socrata",
    "ingestion_layer": "bq_wh_job_audit",
    "layer_name": "day_care_center",
    "layer_url": "https://data.cityofnewyork.us/"
                 "resource/sd93-evwm.json?$select=count(*)",
  },
  # REPORTING SOCRATA BQ INGESTION

  {
    "task_name": "adult_care_facility_map_reporting_ingestion",
    "data_source": "socrata",
    "ingestion_layer": "bq_reporting",
    "reporting_table_name":
      f"{constants.BQ_REPORTING_DATASET}."
      f"socrata_adult_care_facility_map",
    "source_table_name": f" SELECT * FROM  {constants.REPORTING_VIEWS}."
                         f"vw_socrata_adult_care_facility_map "
                         f"where ingestion_timestamp = ",
    "layer_name": "adult_care_facility_map",
    "layer_url": "https://health.data.ny.gov/resource/"
                 "6wkx-ptu4.json?$select=count(*)",

  },
  {
    "task_name": "health_facility_general_"
                 "information_reporting_ingestion",
    "data_source": "socrata",
    "ingestion_layer": "bq_reporting",
    "reporting_table_name":
      f"{constants.BQ_REPORTING_DATASET}."
      f"socrata_health_facility_general_information",
    "source_table_name": f" SELECT * FROM {constants.REPORTING_VIEWS}."
                         f"vw_socrata_health_facility_general_information "
                         f"where ingestion_timestamp = ",
    "layer_name": "health_facility_general_information",
    "layer_url": "https://health.data.ny.gov/"
                 "resource/vn5v-hh5r.json?$select=count(*)",
  },
  {
    "task_name": "health_facility_map_reporting_ingestion",
    "data_source": "socrata",
    "ingestion_layer": "bq_reporting",
    "reporting_table_name":
      f"{constants.BQ_REPORTING_DATASET}."
      f"socrata_health_facility_map",
    "source_table_name": f" SELECT * FROM {constants.REPORTING_VIEWS}."
                         f"vw_socrata_health_facility_map "
                         f"where ingestion_timestamp = ",
    "layer_name": "health_facility_map",
    "layer_url": "https://health.data.ny.gov/"
                 "resource/875v-tpc8.json?$select=count(*)"
  },
  {
    "task_name": "nyc_health_hospitals_patient_care_"
                 "locations_2011_reporting_ingestion",
    "data_source": "socrata",
    "ingestion_layer": "bq_reporting",
    "reporting_table_name":
      f"{constants.BQ_REPORTING_DATASET}."
      f"socrata_nyc_health_hospitals_patient_care_locations_2011",
    "source_table_name": f" SELECT * FROM {constants.REPORTING_VIEWS}."
                         f"vw_socrata_nyc_health_hospitals_"
                         f"patient_care_locations_2011 "
                         f"where ingestion_timestamp = ",
    "layer_name": "nyc_health_hospitals_patient_care_"
                  "locations_2011",
    "layer_url": "https://data.cityofnewyork.us/"
                 "resource/f7b6-v6v3.json?$select=count(*)"
  },
  {
    "task_name": "archived_parks_properties_"
                 "reporting_ingestion",
    "data_source": "socrata",
    "ingestion_layer": "bq_reporting",
    "reporting_table_name":
      f"{constants.BQ_REPORTING_DATASET}."
      f"socrata_archived_parks_properties",
    "source_table_name": f" SELECT * FROM {constants.REPORTING_VIEWS}."
                         f"vw_socrata_archived_parks_properties "
                         f"where ingestion_timestamp = ",
    "layer_name": "archived_parks_properties",
    "layer_url": "https://data.cityofnewyork.us/"
                 "resource/ghu2-eden.json?$select=count(*)"
  },
  {
    "task_name": "athletic_facilities_reporting_ingestion",
    "data_source": "socrata",
    "ingestion_layer": "bq_reporting",
    "reporting_table_name":
      f"{constants.BQ_REPORTING_DATASET}."
      f"socrata_athletic_facilities",
    "source_table_name": f" SELECT * FROM {constants.REPORTING_VIEWS}."
                         f"vw_socrata_athletic_facilities "
                         f"where ingestion_timestamp = ",
    "layer_name": "athletic_facilities",
    "layer_url": "https://data.cityofnewyork.us/resource"
                 "/9wwi-sb8x.json?$select=count(*)",
  },
  {
    "task_name": "child_care_regulated_programs"
                 "_reporting_ingestion",
    "data_source": "socrata",
    "ingestion_layer": "bq_reporting",
    "reporting_table_name":
      f"{constants.BQ_REPORTING_DATASET}."
      f"socrata_child_care_regulated_programs",
    "source_table_name": f" SELECT * FROM {constants.REPORTING_VIEWS}."
                         f"vw_socrata_child_care_regulated_programs "
                         f"where ingestion_timestamp = ",
    "layer_name": "child_care_regulated_programs",
    "layer_url":
      "https://data.ny.gov/resource/cb42-qumz.json?$select=count(*)"
  },
  {
    "task_name": "day_care_center_reporting_ingestion",
    "data_source": "socrata",
    "ingestion_layer": "bq_reporting",
    "reporting_table_name":
      f"{constants.BQ_REPORTING_DATASET}."
      f"socrata_day_care_center",
    "source_table_name": f" SELECT * FROM {constants.REPORTING_VIEWS}."
                         f"vw_socrata_day_care_center "
                         f"where ingestion_timestamp = ",
    "layer_name": "day_care_center",
    "layer_url": "https://data.cityofnewyork.us/"
                 "resource/sd93-evwm.json?$select=count(*)",
  },

  # SOCRATA JOB AUDIT REPORTING BQ INGESTION

  {
    "task_name":
      "adult_care_facility_map_bq_reporting_job_audit_ingestion",
    "query":
      f" SELECT COUNT(*) AS COUNT FROM"
      f" {constants.BQ_REPORTING_DATASET}."
      f"socrata_adult_care_facility_map "
      f"WHERE ingestion_timestamp = ",
    "bq_table_name": f"{constants.BQ_REPORTING_DATASET}"
                     f".socrata_adult_care_facility_map",
    "gcs_bucket_name": constants.SOCRATA_BUCKET_NAME,
    "parsed_gcs_file_path": f"parsed/adult_care_facility_map/"
                            f"{constants.CURRENT_DATE}/"
                            f"adult_care_facility_map.json",
    "data_source": "socrata",
    "ingestion_layer": "bq_reporting_job_audit",
    "layer_name": "adult_care_facility_map",
    "layer_url": "https://health.data.ny.gov/resource/"
                 "6wkx-ptu4.json?$select=count(*)",
  },
  {
    "task_name":
      "health_facility_general_information_"
      "bq_reporting_job_audit_ingestion",
    "query": f" SELECT COUNT(*) AS COUNT"
             f" FROM {constants.BQ_REPORTING_DATASET}."
             f"socrata_health_facility_general_information"
             f" WHERE ingestion_timestamp = ",
    "bq_table_name": f"{constants.BQ_REPORTING_DATASET}."
                     f"socrata_health_facility_general_information",
    "gcs_bucket_name": constants.SOCRATA_BUCKET_NAME,
    "parsed_gcs_file_path": f"parsed/health_facility_general_information/"
                            f"{constants.CURRENT_DATE}/"
                            f"health_facility_general_information.json",
    "data_source": "socrata",
    "ingestion_layer": "bq_reporting_job_audit",
    "layer_name": "health_facility_general_information",
    "layer_url": "https://health.data.ny.gov/"
                 "resource/vn5v-hh5r.json?$select=count(*)"
  },
  {
    "task_name": "health_facility_map_bq_reporting_job_audit_ingestion",
    "query": f" SELECT COUNT(*) AS COUNT FROM "
             f"{constants.BQ_REPORTING_DATASET}"
             f".socrata_health_facility_map "
             f"WHERE ingestion_timestamp = ",
    "bq_table_name": f"{constants.BQ_REPORTING_DATASET}"
                     f".socrata_health_facility_map",
    "gcs_bucket_name": constants.SOCRATA_BUCKET_NAME,
    "parsed_gcs_file_path": f"parsed/health_facility_map/"
                            f"{constants.CURRENT_DATE}/"
                            f"health_facility_map.json",
    "data_source": "socrata",
    "ingestion_layer": "bq_reporting_job_audit",
    "layer_name": "health_facility_map",
    "layer_url": "https://health.data.ny.gov/"
                 "resource/875v-tpc8.json?$select=count(*)"
  },
  {
    "task_name":
      "nyc_health_hospitals_patient_care_locations_2011_"
      "bq_reporting_job_audit_ingestion",
    "query": f" SELECT COUNT(*) AS COUNT FROM "
             f"{constants.BQ_REPORTING_DATASET}."
             f"socrata_nyc_health_hospitals_"
             f"patient_care_locations_2011 WHERE ingestion_timestamp = ",
    "bq_table_name": f"{constants.BQ_REPORTING_DATASET}."
                     f"socrata_nyc_health_hospitals_"
                     f"patient_care_locations_2011",
    "gcs_bucket_name": constants.SOCRATA_BUCKET_NAME,
    "parsed_gcs_file_path": f"parsed/"
                            f"nyc_health_hospitals_patient_care_"
                            f"locations_2011/"
                            f"{constants.CURRENT_DATE}/"
                            f"nyc_health_hospitals_patient_care_"
                            f"locations_2011.json",
    "data_source": "socrata",
    "ingestion_layer": "bq_reporting_job_audit",
    "layer_name": "nyc_health_hospitals_patient_care_"
                  "locations_2011",
    "layer_url": "https://data.cityofnewyork.us/"
                 "resource/f7b6-v6v3.json?$select=count(*)"
  },
  {
    "task_name": "archived_parks_properties_"
                 "bq_reporting_job_audit_ingestion",
    "query": f" SELECT COUNT(*) AS COUNT FROM "
             f"{constants.BQ_REPORTING_DATASET}."
             f"socrata_archived_parks_properties "
             f"WHERE ingestion_timestamp = ",
    "bq_table_name":
      f"{constants.BQ_REPORTING_DATASET}"
      f".socrata_archived_parks_properties",
    "gcs_bucket_name": constants.SOCRATA_BUCKET_NAME,
    "parsed_gcs_file_path": f"parsed/archived_parks_properties/"
                            f"{constants.CURRENT_DATE}/"
                            f"archived_parks_properties.json",
    "data_source": "socrata",
    "ingestion_layer": "bq_reporting_job_audit",
    "layer_name": "archived_parks_properties",
    "layer_url": "https://data.cityofnewyork.us/"
                 "resource/ghu2-eden.json?$select=count(*)"
  },
  {
    "task_name": "athletic_facilities_bq_"
                 "reporting_job_audit_ingestion",
    "query": f" SELECT COUNT(*) AS COUNT FROM "
             f"{constants.BQ_REPORTING_DATASET}"
             f".socrata_athletic_facilities "
             f"WHERE ingestion_timestamp = ",
    "bq_table_name": f"{constants.BQ_REPORTING_DATASET}"
                     f".socrata_athletic_facilities",
    "gcs_bucket_name": constants.SOCRATA_BUCKET_NAME,
    "parsed_gcs_file_path": f"parsed/athletic_facilities/"
                            f"{constants.CURRENT_DATE}/"
                            f"athletic_facilities.json",
    "data_source": "socrata",
    "ingestion_layer": "bq_reporting_job_audit",
    "layer_name": "athletic_facilities",
    "layer_url": "https://data.cityofnewyork.us/resource"
                 "/9wwi-sb8x.json?$select=count(*)",
  },
  {
    "task_name":
      "child_care_regulated_programs_bq_"
      "reporting_job_audit_ingestion",
    "query": f" SELECT COUNT(*) AS COUNT "
             f"FROM {constants.BQ_REPORTING_DATASET}."
             f"socrata_child_care_regulated_"
             f"programs WHERE ingestion_timestamp = ",
    "bq_table_name": f"{constants.BQ_REPORTING_DATASET}."
                     f"socrata_child_care_regulated_programs",
    "gcs_bucket_name": constants.SOCRATA_BUCKET_NAME,
    "parsed_gcs_file_path": f"parsed/child_care_regulated_programs/"
                            f"{constants.CURRENT_DATE}/"
                            f"child_care_regulated_programs.json",
    "data_source": "socrata",
    "ingestion_layer": "bq_reporting_job_audit",
    "layer_name": "child_care_regulated_programs",
    "layer_url":
      "https://data.ny.gov/resource/cb42-qumz.json?$select=count(*)"
  },
  {
    "task_name": "day_care_center_bq_reporting_"
                 "job_audit_ingestion",
    "query": f" SELECT COUNT(*) AS COUNT FROM "
             f"{constants.BQ_REPORTING_DATASET}."
             f"socrata_day_care_center "
             f"WHERE ingestion_timestamp = ",
    "bq_table_name": f"{constants.BQ_REPORTING_DATASET}."
                     f"socrata_day_care_center",
    "gcs_bucket_name": constants.SOCRATA_BUCKET_NAME,
    "parsed_gcs_file_path": f"parsed/day_care_center/"
                            f"{constants.CURRENT_DATE}/"
                            f"day_care_center.json",
    "data_source": "socrata",
    "ingestion_layer": "bq_reporting_job_audit",
    "layer_name": "day_care_center",
    "layer_url": "https://data.cityofnewyork.us/"
                 "resource/sd93-evwm.json?$select=count(*)",
  },

]

AQS_TASKS_CONFIG = [
  # AQS RAW GCS INGESTION MAIN TASKS
  {
    "task_name": "black_carbon_pm2_5_corrected_raw_ingestion",
    "data_source": "aqs",
    "ingestion_layer": "gcs_raw",
    "service_endpoint": f"{constants.AQS_CLOUD_RUN_SERVICE_ENDPOINT}/"
                        f"process_raw_layer?"
                        f"layer_name="
                        f"black_carbon_pm2_5_corrected"
                        f"&year={constants.AQS_API_YEAR[0]}&"
                        f"month={constants.AQS_API_MONTH}"
                        "&batch_timestamp={}&batch_unix_timestamp={}"
                        f"&bucket={constants.AQS_BUCKET_NAME}"
                        f"&lookup_month={constants.AQS_API_LOOKUP_MONTH}",
  },
  {
    "task_name": "carbon_monoxide_raw_ingestion",
    "data_source": "aqs",
    "ingestion_layer": "gcs_raw",
    "service_endpoint": f"{constants.AQS_CLOUD_RUN_SERVICE_ENDPOINT}/"
                        f"process_raw_layer?"
                        f"layer_name="
                        f"carbon_monoxide&year={constants.AQS_API_YEAR[0]}"
                        f"&month={constants.AQS_API_MONTH}"
                        "&batch_timestamp={}&batch_unix_timestamp={}"
                        f"&bucket={constants.AQS_BUCKET_NAME}"
                        f"&lookup_month={constants.AQS_API_LOOKUP_MONTH}",
  },
  {
    "task_name": "formaldehyde_raw_ingestion",
    "data_source": "aqs",
    "ingestion_layer": "gcs_raw",
    "service_endpoint": f"{constants.AQS_CLOUD_RUN_SERVICE_ENDPOINT}/"
                        f"process_raw_layer?"
                        f"layer_name="
                        f"formaldehyde&year={constants.AQS_API_YEAR[0]}"
                        f"&month={constants.AQS_API_MONTH}"
                        "&batch_timestamp={}&batch_unix_timestamp={}"
                        f"&bucket={constants.AQS_BUCKET_NAME}"
                        f"&lookup_month={constants.AQS_API_LOOKUP_MONTH}",
  },
  {
    "task_name": "nitric_oxide_raw_ingestion",
    "data_source": "aqs",
    "ingestion_layer": "gcs_raw",
    "service_endpoint": f"{constants.AQS_CLOUD_RUN_SERVICE_ENDPOINT}/"
                        f"process_raw_layer?"
                        f"layer_name="
                        f"nitric_oxide&year={constants.AQS_API_YEAR[0]}"
                        f"&month={constants.AQS_API_MONTH}"
                        "&batch_timestamp={}&batch_unix_timestamp={}"
                        f"&bucket={constants.AQS_BUCKET_NAME}"
                        f"&lookup_month={constants.AQS_API_LOOKUP_MONTH}",
  },
  {
    "task_name": "nitrogen_dioxide_raw_ingestion",
    "data_source": "aqs",
    "ingestion_layer": "gcs_raw",
    "service_endpoint": f"{constants.AQS_CLOUD_RUN_SERVICE_ENDPOINT}/"
                        f"process_raw_layer?"
                        f"layer_name="
                        f"nitrogen_dioxide"
                        f"&year={constants.AQS_API_YEAR[0]}&"
                        f"month={constants.AQS_API_MONTH}"
                        "&batch_timestamp={}&batch_unix_timestamp={}"
                        f"&bucket={constants.AQS_BUCKET_NAME}"
                        f"&lookup_month={constants.AQS_API_LOOKUP_MONTH}",
  },
  {
    "task_name": "ozone_raw_ingestion",
    "data_source": "aqs",
    "ingestion_layer": "gcs_raw",
    "service_endpoint": f"{constants.AQS_CLOUD_RUN_SERVICE_ENDPOINT}/"
                        f"process_raw_layer?"
                        f"layer_name="
                        f"ozone"
                        f"&year={constants.AQS_API_YEAR[0]}&"
                        f"month={constants.AQS_API_MONTH}"
                        "&batch_timestamp={}&batch_unix_timestamp={}"
                        f"&bucket={constants.AQS_BUCKET_NAME}"
                        f"&lookup_month={constants.AQS_API_LOOKUP_MONTH}",
  },
  {
    "task_name": "pm_25_raw_ingestion",
    "data_source": "aqs",
    "ingestion_layer": "gcs_raw",
    "service_endpoint": f"{constants.AQS_CLOUD_RUN_SERVICE_ENDPOINT}/"
                        f"process_raw_layer?"
                        f"layer_name="
                        f"pm_25&year={constants.AQS_API_YEAR[0]}&"
                        f"month={constants.AQS_API_MONTH}"
                        "&batch_timestamp={}&batch_unix_timestamp={}"
                        f"&bucket={constants.AQS_BUCKET_NAME}"
                        f"&lookup_month={constants.AQS_API_LOOKUP_MONTH}",
  },
  {
    "task_name": "sulfur_dioxide_raw_ingestion",
    "data_source": "aqs",
    "ingestion_layer": "gcs_raw",
    "service_endpoint": f"{constants.AQS_CLOUD_RUN_SERVICE_ENDPOINT}/"
                        f"process_raw_layer?"
                        f"layer_name="
                        f"sulfur_dioxide&year={constants.AQS_API_YEAR[0]}&"
                        f"month={constants.AQS_API_MONTH}"
                        "&batch_timestamp={}&batch_unix_timestamp={}"
                        f"&bucket={constants.AQS_BUCKET_NAME}"
                        f"&lookup_month={constants.AQS_API_LOOKUP_MONTH}",
  },
  {
    "task_name": "ethane_raw_ingestion",
    "data_source": "aqs",
    "ingestion_layer": "gcs_raw",
    "service_endpoint": f"{constants.AQS_CLOUD_RUN_SERVICE_ENDPOINT}/"
                        f"process_raw_layer?"
                        f"layer_name="
                        f"ethane&year={constants.AQS_API_YEAR[0]}&"
                        f"month={constants.AQS_API_MONTH}"
                        "&batch_timestamp={}&batch_unix_timestamp={}"
                        f"&bucket={constants.AQS_BUCKET_NAME}"
                        f"&lookup_month={constants.AQS_API_LOOKUP_MONTH}",
  },
  {
    "task_name": "toxics_and_carbonyls_raw_ingestion",
    "data_source": "aqs",
    "ingestion_layer": "gcs_raw",
    "service_endpoint": f"{constants.AQS_CLOUD_RUN_SERVICE_ENDPOINT}/"
                        f"process_raw_layer?"
                        f"layer_name="
                        f"toxics_and_carbonyls&year="
                        f"{constants.AQS_API_YEAR[0]}&"
                        f"month={constants.AQS_API_MONTH}"
                        "&batch_timestamp={}&batch_unix_timestamp={}"
                        f"&bucket={constants.AQS_BUCKET_NAME}"
                        f"&lookup_month={constants.AQS_API_LOOKUP_MONTH}",
  },

  # AQS PARSE GCS INGESTION MAIN TASKS

  {
    "task_name": "black_carbon_pm2_5_corrected_parse_ingestion",
    "data_source": "aqs",
    "ingestion_layer": "gcs_parse",
    "service_endpoint": f"{constants.AQS_CLOUD_RUN_SERVICE_ENDPOINT}"
                        f"/process_parse_layer?"
                        f"layer_name=black_carbon_pm2_5_corrected"
                        f"&raw_gcs_ingestion_date="
                        f"{constants.CURRENT_DATE}"
                        "&batch_timestamp={}&batch_unix_timestamp={}"
                        f"&bucket={constants.AQS_BUCKET_NAME}",
  },
  {
    "task_name": "carbon_monoxide_parse_ingestion",
    "data_source": "aqs",
    "ingestion_layer": "gcs_parse",
    "service_endpoint": f"{constants.AQS_CLOUD_RUN_SERVICE_ENDPOINT}"
                        f"/process_parse_layer?"
                        f"layer_name=carbon_monoxide"
                        f"&raw_gcs_ingestion_date={constants.CURRENT_DATE}"
                        "&batch_timestamp={}&batch_unix_timestamp={}"
                        f"&bucket={constants.AQS_BUCKET_NAME}",
  },
  {
    "task_name": "formaldehyde_parse_ingestion",
    "data_source": "aqs",
    "ingestion_layer": "gcs_parse",
    "service_endpoint": f"{constants.AQS_CLOUD_RUN_SERVICE_ENDPOINT}"
                        f"/process_parse_layer?"
                        f"layer_name=formaldehyde"
                        f"&raw_gcs_ingestion_date={constants.CURRENT_DATE}"
                        "&batch_timestamp={}&batch_unix_timestamp={}"
                        f"&bucket={constants.AQS_BUCKET_NAME}",
  },
  {
    "task_name": "nitric_oxide_parse_ingestion",
    "data_source": "aqs",
    "ingestion_layer": "gcs_parse",
    "service_endpoint": f"{constants.AQS_CLOUD_RUN_SERVICE_ENDPOINT}"
                        f"/process_parse_layer?"
                        f"layer_name=nitric_oxide"
                        f"&raw_gcs_ingestion_date={constants.CURRENT_DATE}"
                        "&batch_timestamp={}&batch_unix_timestamp={}"
                        f"&bucket={constants.AQS_BUCKET_NAME}",
  },
  {
    "task_name": "nitrogen_dioxide_parse_ingestion",
    "data_source": "aqs",
    "ingestion_layer": "gcs_parse",
    "service_endpoint": f"{constants.AQS_CLOUD_RUN_SERVICE_ENDPOINT}"
                        f"/process_parse_layer?"
                        f"layer_name=nitrogen_dioxide"
                        f"&raw_gcs_ingestion_date={constants.CURRENT_DATE}"
                        "&batch_timestamp={}&batch_unix_timestamp={}"
                        f"&bucket={constants.AQS_BUCKET_NAME}",
  },
  {
    "task_name": "ozone_parse_ingestion",
    "data_source": "aqs",
    "ingestion_layer": "gcs_parse",
    "service_endpoint": f"{constants.AQS_CLOUD_RUN_SERVICE_ENDPOINT}"
                        f"/process_parse_layer?"
                        f"layer_name=ozone"
                        f"&raw_gcs_ingestion_date={constants.CURRENT_DATE}"
                        "&batch_timestamp={}&batch_unix_timestamp={}"
                        f"&bucket={constants.AQS_BUCKET_NAME}",
  },
  {
    "task_name": "pm_25_parse_ingestion",
    "data_source": "aqs",
    "ingestion_layer": "gcs_parse",
    "service_endpoint": f"{constants.AQS_CLOUD_RUN_SERVICE_ENDPOINT}"
                        f"/process_parse_layer?"
                        f"layer_name=pm_25"
                        f"&raw_gcs_ingestion_date={constants.CURRENT_DATE}"
                        "&batch_timestamp={}&batch_unix_timestamp={}"
                        f"&bucket={constants.AQS_BUCKET_NAME}",
  },
  {
    "task_name": "sulfur_dioxide_parse_ingestion",
    "data_source": "aqs",
    "ingestion_layer": "gcs_parse",
    "service_endpoint": f"{constants.AQS_CLOUD_RUN_SERVICE_ENDPOINT}"
                        f"/process_parse_layer?"
                        f"layer_name=sulfur_dioxide"
                        f"&raw_gcs_ingestion_date={constants.CURRENT_DATE}"
                        "&batch_timestamp={}&batch_unix_timestamp={}"
                        f"&bucket={constants.AQS_BUCKET_NAME}",
  },
  {
    "task_name": "ethane_parse_ingestion",
    "data_source": "aqs",
    "ingestion_layer": "gcs_parse",
    "service_endpoint": f"{constants.AQS_CLOUD_RUN_SERVICE_ENDPOINT}"
                        f"/process_parse_layer?"
                        f"layer_name=ethane"
                        f"&raw_gcs_ingestion_date={constants.CURRENT_DATE}"
                        "&batch_timestamp={}&batch_unix_timestamp={}"
                        f"&bucket={constants.AQS_BUCKET_NAME}",
  },
  {
    "task_name": "toxics_and_carbonyls_parse_ingestion",
    "data_source": "aqs",
    "ingestion_layer": "gcs_parse",
    "service_endpoint": f"{constants.AQS_CLOUD_RUN_SERVICE_ENDPOINT}"
                        f"/process_parse_layer?"
                        f"layer_name=toxics_and_carbonyls"
                        f"&raw_gcs_ingestion_date={constants.CURRENT_DATE}"
                        "&batch_timestamp={}&batch_unix_timestamp={}"
                        f"&bucket={constants.AQS_BUCKET_NAME}",
  },

  # AQS RAW BQ INGESTION MAIN TASKS
  {
    "task_name": "black_carbon_pm2_5_corrected_bq_raw_ingestion",
    "bq_table_name": f"{constants.AQS_RAW_DATASET}."
                     f"black_carbon_pm2_5_corrected",
    "new_column_audit_table":
      f"{constants.BQ_METADATA_DATASET}.new_column_audit",
    "gcs_bucket_name": constants.AQS_BUCKET_NAME,
    "parsed_gcs_file_path": f"parsed/black_carbon_pm2_5_corrected/"
                            f"{constants.CURRENT_DATE}/"
                            "black_carbon_pm2_5_corrected_{}.json",
    "data_source": "aqs",
    "ingestion_layer": "bq_raw",
    "layer_name": "black_carbon_pm2_5_corrected",
    "layer_url": "https://aqs.epa.gov/data/api/annualData/byState?email="
                 + constants.AQS_EMAIL + "&key=" + constants.AQS_KEY +
                 "&param=88317&bdate={}0515&edate={}0515&state=36"
  },
  {
    "task_name": "carbon_monoxide_bq_raw_ingestion",
    "bq_table_name": f"{constants.AQS_RAW_DATASET}.carbon_monoxide",
    "new_column_audit_table":
      f"{constants.BQ_METADATA_DATASET}.new_column_audit",
    "gcs_bucket_name": constants.AQS_BUCKET_NAME,
    "parsed_gcs_file_path": f"parsed/carbon_monoxide/"
                            f"{constants.CURRENT_DATE}/"
                            "carbon_monoxide_{}.json",
    "data_source": "aqs",
    "ingestion_layer": "bq_raw",
    "layer_name": "carbon_monoxide",
    "layer_url": "https://aqs.epa.gov/data/api/annualData/byState?email="
                 + constants.AQS_EMAIL + "&key=" + constants.AQS_KEY +
                 "&param=42101&bdate={}0515&edate={}0515&state=36"
  },
  {
    "task_name": "formaldehyde_bq_raw_ingestion",
    "bq_table_name": f"{constants.AQS_RAW_DATASET}.formaldehyde",
    "new_column_audit_table":
      f"{constants.BQ_METADATA_DATASET}.new_column_audit",
    "gcs_bucket_name": constants.AQS_BUCKET_NAME,
    "parsed_gcs_file_path": f"parsed/formaldehyde/"
                            f"{constants.CURRENT_DATE}/"
                            "formaldehyde_{}.json",
    "data_source": "aqs",
    "ingestion_layer": "bq_raw",
    "layer_name": "formaldehyde",
    "layer_url": "https://aqs.epa.gov/data/api/annualData/byState?email="
                 + constants.AQS_EMAIL + "&key=" + constants.AQS_KEY +
                 "&param=43502&bdate={}0515&edate={}0515&state=36"
  },
  {
    "task_name": "nitric_oxide_bq_raw_ingestion",
    "bq_table_name": f"{constants.AQS_RAW_DATASET}.nitric_oxide",
    "new_column_audit_table":
      f"{constants.BQ_METADATA_DATASET}.new_column_audit",
    "gcs_bucket_name": constants.AQS_BUCKET_NAME,
    "parsed_gcs_file_path": f"parsed/nitric_oxide/"
                            f"{constants.CURRENT_DATE}/"
                            "nitric_oxide_{}.json",
    "data_source": "aqs",
    "ingestion_layer": "bq_raw",
    "layer_name": "nitric_oxide",
    "layer_url": "https://aqs.epa.gov/data/api/annualData/byState?email="
                 + constants.AQS_EMAIL + "&key=" + constants.AQS_KEY +
                 "&param=42601&bdate={}0515&edate={}0515&state=36"
  },
  {
    "task_name": "nitrogen_dioxide_bq_raw_ingestion",
    "bq_table_name": f"{constants.AQS_RAW_DATASET}.nitrogen_dioxide",
    "new_column_audit_table":
      f"{constants.BQ_METADATA_DATASET}.new_column_audit",
    "gcs_bucket_name": constants.AQS_BUCKET_NAME,
    "parsed_gcs_file_path": f"parsed/nitrogen_dioxide/"
                            f"{constants.CURRENT_DATE}/"
                            "nitrogen_dioxide_{}.json",
    "data_source": "aqs",
    "ingestion_layer": "bq_raw",
    "layer_name": "nitrogen_dioxide",
    "layer_url": "https://aqs.epa.gov/data/api/annualData/byState?email="
                 + constants.AQS_EMAIL + "&key=" + constants.AQS_KEY +
                 "&param=42602&bdate={}0515&edate={}0515&state=36"
  },
  {
    "task_name": "ozone_bq_raw_ingestion",
    "bq_table_name": f"{constants.AQS_RAW_DATASET}.ozone",
    "new_column_audit_table":
      f"{constants.BQ_METADATA_DATASET}.new_column_audit",
    "gcs_bucket_name": constants.AQS_BUCKET_NAME,
    "parsed_gcs_file_path": f"parsed/ozone/"
                            f"{constants.CURRENT_DATE}/"
                            "ozone_{}.json",
    "data_source": "aqs",
    "ingestion_layer": "bq_raw",
    "layer_name": "ozone",
    "layer_url": "https://aqs.epa.gov/data/api/annualData/byState?email="
                 + constants.AQS_EMAIL + "&key=" + constants.AQS_KEY +
                 "&param=44201&bdate={}0515&edate={}0515&state=36"
  },
  {
    "task_name": "pm_25_bq_raw_ingestion",
    "bq_table_name": f"{constants.AQS_RAW_DATASET}.pm_25",
    "new_column_audit_table":
      f"{constants.BQ_METADATA_DATASET}.new_column_audit",
    "gcs_bucket_name": constants.AQS_BUCKET_NAME,
    "parsed_gcs_file_path": f"parsed/pm_25/"
                            f"{constants.CURRENT_DATE}/"
                            "pm_25_{}.json",
    "data_source": "aqs",
    "ingestion_layer": "bq_raw",
    "layer_name": "pm_25",
    "layer_url": "https://aqs.epa.gov/data/api/annualData/byState?email="
                 + constants.AQS_EMAIL + "&key=" + constants.AQS_KEY +
                 "&param=88101&bdate={}0515&edate={}0515&state=36"
  },
  {
    "task_name": "sulfur_dioxide_bq_raw_ingestion",
    "bq_table_name": f"{constants.AQS_RAW_DATASET}.sulfur_dioxide",
    "new_column_audit_table":
      f"{constants.BQ_METADATA_DATASET}.new_column_audit",
    "gcs_bucket_name": constants.AQS_BUCKET_NAME,
    "parsed_gcs_file_path": f"parsed/sulfur_dioxide/"
                            f"{constants.CURRENT_DATE}/"
                            "sulfur_dioxide_{}.json",
    "data_source": "aqs",
    "ingestion_layer": "bq_raw",
    "layer_name": "sulfur_dioxide",
    "layer_url": "https://aqs.epa.gov/data/api/annualData/byState?email="
                 + constants.AQS_EMAIL + "&key=" + constants.AQS_KEY +
                 "&param=42401&bdate={}0515&edate={}0515&state=36",
  },
  {
    "task_name": "ethane_bq_raw_ingestion",
    "bq_table_name": f"{constants.AQS_RAW_DATASET}.ethane",
    "new_column_audit_table":
      f"{constants.BQ_METADATA_DATASET}.new_column_audit",
    "gcs_bucket_name": constants.AQS_BUCKET_NAME,
    "parsed_gcs_file_path": f"parsed/ethane/"
                            f"{constants.CURRENT_DATE}/"
                            "ethane_{}.json",
    "data_source": "aqs",
    "ingestion_layer": "bq_raw",
    "layer_name": "ethane",
    "layer_url": "https://aqs.epa.gov/data/api/annualData/byState?email="
                 + constants.AQS_EMAIL + "&key=" + constants.AQS_KEY +
                 "&param=43202&bdate={}0515&edate={}0515&state=36"
  },

  {
    "task_name": "toxics_and_carbonyls_bq_raw_ingestion",
    "bq_table_name": f"{constants.AQS_RAW_DATASET}.toxics_and_carbonyls",
    "new_column_audit_table":
      f"{constants.BQ_METADATA_DATASET}.new_column_audit",
    "gcs_bucket_name": constants.AQS_BUCKET_NAME,
    "parsed_gcs_file_path": f"parsed/toxics_and_carbonyls/"
                            f"{constants.CURRENT_DATE}/"
                            "toxics_and_carbonyls_{}.json",
    "data_source": "aqs",
    "ingestion_layer": "bq_raw",
    "layer_name": "toxics_and_carbonyls",
    "layer_url": "https://aqs.epa.gov/data/api/annualData/byState?email="
                 + constants.AQS_EMAIL + "&key=" + constants.AQS_KEY +
                 "&param=45201,45202,45203,45204,"
                 "45109&bdate={}0515&edate={}0515&state=36"
  },

  # AQS JOB AUDIT RAW BQ INGESTION MAIN TASKS
  {
    "task_name":
      "black_carbon_pm2_5_corrected_bq_raw_job_audit_ingestion",
    "bq_table_name": f"{constants.AQS_RAW_DATASET}."
                     f"black_carbon_pm2_5_corrected",
    "query": f" SELECT COUNT(*) AS COUNT FROM {constants.AQS_RAW_DATASET}."
             f"black_carbon_pm2_5_corrected WHERE ingestion_timestamp = ",
    "gcs_bucket_name": constants.AQS_BUCKET_NAME,
    "parsed_gcs_file_path": f"parsed/black_carbon_pm2_5_corrected/"
                            f"{constants.CURRENT_DATE}/"
                            "black_carbon_pm2_5_corrected_{}.json",
    "data_source": "aqs",
    "ingestion_layer": "bq_raw_job_audit",
    "layer_name": "black_carbon_pm2_5_corrected",
    "layer_url": "https://aqs.epa.gov/data/api/annualData/byState?email="
                 + constants.AQS_EMAIL + "&key=" + constants.AQS_KEY +
                 "&param=88317&bdate={}0515&edate={}0515&state=36"
  },
  {
    "task_name": "carbon_monoxide_bq_raw_job_audit_ingestion",
    "query":
      f" SELECT COUNT(*) AS COUNT FROM "
      f"{constants.AQS_RAW_DATASET}.carbon_monoxide "
      f"WHERE ingestion_timestamp = ",
    "bq_table_name": f"{constants.AQS_RAW_DATASET}"
                     f".carbon_monoxide",
    "gcs_bucket_name": constants.AQS_BUCKET_NAME,
    "parsed_gcs_file_path": f"parsed/carbon_monoxide/"
                            f"{constants.CURRENT_DATE}/"
                            "carbon_monoxide_{}.json",
    "data_source": "aqs",
    "ingestion_layer": "bq_raw_job_audit",
    "layer_name": "carbon_monoxide",
    "layer_url": "https://aqs.epa.gov/data/api/annualData/byState?email="
                 + constants.AQS_EMAIL + "&key=" + constants.AQS_KEY +
                 "&param=42101&bdate={}0515&edate={}0515&state=36"
  },
  {
    "task_name": "formaldehyde_bq_raw_job_audit_ingestion",
    "query": f" SELECT COUNT(*) AS COUNT "
             f"FROM {constants.AQS_RAW_DATASET}."
             f"formaldehyde WHERE ingestion_timestamp = ",
    "bq_table_name": f"{constants.AQS_RAW_DATASET}.formaldehyde",
    "gcs_bucket_name": constants.AQS_BUCKET_NAME,
    "parsed_gcs_file_path": f"parsed/formaldehyde/"
                            f"{constants.CURRENT_DATE}/"
                            "formaldehyde_{}.json",
    "data_source": "aqs",
    "ingestion_layer": "bq_raw_job_audit",
    "layer_name": "formaldehyde",
    "layer_url": "https://aqs.epa.gov/data/api/annualData/byState?email="
                 + constants.AQS_EMAIL + "&key=" + constants.AQS_KEY +
                 "&param=43502&bdate={}0515&edate={}0515&state=36"
  },
  {
    "task_name": "nitric_oxide_bq_raw_job_audit_ingestion",
    "query": f" SELECT COUNT(*) AS COUNT FROM "
             f"{constants.AQS_RAW_DATASET}"
             f".nitric_oxide "
             f"WHERE ingestion_timestamp = ",
    "bq_table_name": f"{constants.AQS_RAW_DATASET}.nitric_oxide",
    "gcs_bucket_name": constants.AQS_BUCKET_NAME,
    "parsed_gcs_file_path": f"parsed/nitric_oxide/"
                            f"{constants.CURRENT_DATE}/"
                            "nitric_oxide_{}.json",
    "data_source": "aqs",
    "ingestion_layer": "bq_raw_job_audit",
    "layer_name": "nitric_oxide",
    "layer_url": "https://aqs.epa.gov/data/api/annualData/byState?email="
                 + constants.AQS_EMAIL + "&key=" + constants.AQS_KEY +
                 "&param=42601&bdate={}0515&edate={}0515&state=36"
  },
  {
    "task_name": "nitrogen_dioxide_bq_raw_job_audit_ingestion",
    "query": f" SELECT COUNT(*) AS COUNT FROM "
             f"{constants.AQS_RAW_DATASET}"
             f".nitrogen_dioxide WHERE ingestion_timestamp = ",
    "bq_table_name": f"{constants.AQS_RAW_DATASET}.nitrogen_dioxide",
    "gcs_bucket_name": constants.AQS_BUCKET_NAME,
    "parsed_gcs_file_path": f"parsed/nitrogen_dioxide/"
                            f"{constants.CURRENT_DATE}/"
                            "nitrogen_dioxide_{}.json",
    "data_source": "aqs",
    "ingestion_layer": "bq_raw_job_audit",
    "layer_name": "nitrogen_dioxide",
    "layer_url": "https://aqs.epa.gov/data/api/annualData/byState?email="
                 + constants.AQS_EMAIL + "&key=" + constants.AQS_KEY +
                 "&param=42602&bdate={}0515&edate={}0515&state=36"
  },
  {
    "task_name": "ozone_bq_raw_job_audit_ingestion",
    "query": f" SELECT COUNT(*) AS COUNT "
             f"FROM {constants.AQS_RAW_DATASET}"
             f".ozone WHERE ingestion_timestamp = ",
    "bq_table_name": f"{constants.AQS_RAW_DATASET}.ozone",
    "gcs_bucket_name": constants.AQS_BUCKET_NAME,
    "parsed_gcs_file_path": f"parsed/ozone/"
                            f"{constants.CURRENT_DATE}/"
                            "ozone_{}.json",
    "data_source": "aqs",
    "ingestion_layer": "bq_raw_job_audit",
    "layer_name": "ozone",
    "layer_url": "https://aqs.epa.gov/data/api/annualData/byState?email="
                 + constants.AQS_EMAIL + "&key=" + constants.AQS_KEY +
                 "&param=44201&bdate={}0515&edate={}0515&state=36"
  },
  {
    "task_name": "pm_25_bq_raw_job_audit_ingestion",
    "query": f" SELECT COUNT(*) AS COUNT "
             f"FROM {constants.AQS_RAW_DATASET}"
             f".pm_25 WHERE ingestion_timestamp = ",
    "bq_table_name": f"{constants.AQS_RAW_DATASET}.pm_25",
    "gcs_bucket_name": constants.AQS_BUCKET_NAME,
    "parsed_gcs_file_path": f"parsed/pm_25/"
                            f"{constants.CURRENT_DATE}/"
                            "pm_25_{}.json",
    "data_source": "aqs",
    "ingestion_layer": "bq_raw_job_audit",
    "layer_name": "pm_25",
    "layer_url": "https://aqs.epa.gov/data/api/annualData/byState?email="
                 + constants.AQS_EMAIL + "&key=" + constants.AQS_KEY +
                 "&param=88101&bdate={}0515&edate={}0515&state=36"
  },
  {
    "task_name": "sulfur_dioxide_bq_raw_job_audit_ingestion",
    "query": f" SELECT COUNT(*) AS COUNT FROM "
             f"{constants.AQS_RAW_DATASET}"
             f".sulfur_dioxide WHERE ingestion_timestamp = ",
    "bq_table_name": f"{constants.AQS_RAW_DATASET}.sulfur_dioxide",
    "gcs_bucket_name": constants.AQS_BUCKET_NAME,
    "parsed_gcs_file_path": f"parsed/sulfur_dioxide/"
                            f"{constants.CURRENT_DATE}/"
                            "sulfur_dioxide_{}.json",
    "data_source": "aqs",
    "ingestion_layer": "bq_raw_job_audit",
    "layer_name": "sulfur_dioxide",
    "layer_url": "https://aqs.epa.gov/data/api/annualData/byState?email="
                 + constants.AQS_EMAIL + "&key=" + constants.AQS_KEY +
                 "&param=42401&bdate={}0515&edate={}0515&state=36",
  },
  {
    "task_name": "ethane_bq_raw_job_audit_ingestion",
    "query": f" SELECT COUNT(*) AS COUNT "
             f"FROM {constants.AQS_RAW_DATASET}.ethane"
             f" WHERE ingestion_timestamp = ",
    "bq_table_name": f"{constants.AQS_RAW_DATASET}.ethane",
    "gcs_bucket_name": constants.AQS_BUCKET_NAME,
    "parsed_gcs_file_path": f"parsed/ethane/"
                            f"{constants.CURRENT_DATE}/"
                            "ethane_{}.json",
    "data_source": "aqs",
    "ingestion_layer": "bq_raw_job_audit",
    "layer_name": "ethane",
    "layer_url": "https://aqs.epa.gov/data/api/annualData/byState?email="
                 + constants.AQS_EMAIL + "&key=" + constants.AQS_KEY +
                 "&param=43202&bdate={}0515&edate={}0515&state=36"
  },
  {
    "task_name": "toxics_and_carbonyls_bq_raw_job_audit_ingestion",
    "query": f" SELECT COUNT(*) AS COUNT FROM "
             f"{constants.AQS_RAW_DATASET}"
             f".toxics_and_carbonyls "
             f"WHERE ingestion_timestamp = ",
    "bq_table_name": f"{constants.AQS_RAW_DATASET}.toxics_and_carbonyls",
    "gcs_bucket_name": constants.AQS_BUCKET_NAME,
    "parsed_gcs_file_path": f"parsed/toxics_and_carbonyls/"
                            f"{constants.CURRENT_DATE}/"
                            "toxics_and_carbonyls_{}.json",
    "data_source": "aqs",
    "ingestion_layer": "bq_raw_job_audit",
    "layer_name": "toxics_and_carbonyls",
    "layer_url": "https://aqs.epa.gov/data/api/annualData/byState?email="
                 + constants.AQS_EMAIL + "&key=" + constants.AQS_KEY +
                 "&param=45201,45202,45203,45204,"
                 "45109&bdate={}0515&edate={}0515&state=36"
  },
  # AQS WH RAW BQ INGESTION MAIN TASKS
  {
    "task_name": "black_carbon_pm2_5_corrected_wh_ingestion",
    "bq_table_name":
      f" SELECT * FROM {constants.PROJECT_ID}."
      f"{constants.AQS_RAW_DATASET}.black_carbon_pm2_5_corrected",
    "data_source": "aqs",
    "ingestion_layer": "bq_warehouse",
    "warehouse_table_name":
      f"{constants.BQ_WH_DATASET}.aqs_black_carbon_pm2_5_corrected",
    "layer_name": "black_carbon_pm2_5_corrected",
    "layer_url": "https://aqs.epa.gov/data/api/annualData/byState?email="
                 + constants.AQS_EMAIL + "&key=" + constants.AQS_KEY +
                 "&param=88317&bdate={}0515&edate={}0515&state=36",
    "parsed_gcs_file_path": f"parsed/black_carbon_pm2_5_corrected/"
                            f"{constants.CURRENT_DATE}/"
                            "black_carbon_pm2_5_corrected_{}.json",

  },
  {
    "task_name": "carbon_monoxide_wh_ingestion",
    "bq_table_name":
      f" SELECT * FROM {constants.PROJECT_ID}."
      f"{constants.AQS_RAW_DATASET}.carbon_monoxide",
    "data_source": "aqs",
    "ingestion_layer": "bq_warehouse",
    "warehouse_table_name":
      f"{constants.BQ_WH_DATASET}.aqs_carbon_monoxide",
    "layer_name": "carbon_monoxide",
    "layer_url": "https://aqs.epa.gov/data/api/annualData/byState?email="
                 + constants.AQS_EMAIL + "&key=" + constants.AQS_KEY +
                 "&param=42101&bdate={}0515&edate={}0515&state=36",
    "parsed_gcs_file_path": f"parsed/carbon_monoxide/"
                            f"{constants.CURRENT_DATE}/"
                            "carbon_monoxide_{}.json",

  },
  {
    "task_name": "formaldehyde_wh_ingestion",
    "bq_table_name":
      f" SELECT * FROM {constants.PROJECT_ID}."
      f"{constants.AQS_RAW_DATASET}.formaldehyde",
    "data_source": "aqs",
    "ingestion_layer": "bq_warehouse",
    "warehouse_table_name":
      f"{constants.BQ_WH_DATASET}.aqs_formaldehyde",
    "layer_name": "formaldehyde",
    "layer_url": "https://aqs.epa.gov/data/api/annualData/byState?email="
                 + constants.AQS_EMAIL + "&key=" + constants.AQS_KEY +
                 "&param=43502&bdate={}0515&edate={}0515&state=36",
    "parsed_gcs_file_path": f"parsed/formaldehyde/"
                            f"{constants.CURRENT_DATE}/"
                            "formaldehyde_{}.json",

  },
  {
    "task_name": "nitric_oxide_wh_ingestion",
    "bq_table_name":
      f" SELECT * FROM {constants.PROJECT_ID}."
      f"{constants.AQS_RAW_DATASET}.nitric_oxide",
    "data_source": "aqs",
    "ingestion_layer": "bq_warehouse",
    "warehouse_table_name":
      f"{constants.BQ_WH_DATASET}.aqs_nitric_oxide",
    "layer_name": "nitric_oxide",
    "layer_url": "https://aqs.epa.gov/data/api/annualData/byState?email="
                 + constants.AQS_EMAIL + "&key=" + constants.AQS_KEY +
                 "&param=42601&bdate={}0515&edate={}0515&state=36",
    "parsed_gcs_file_path": f"parsed/nitric_oxide/"
                            f"{constants.CURRENT_DATE}/"
                            "nitric_oxide_{}.json",

  },
  {
    "task_name": "nitrogen_dioxide_wh_ingestion",
    "bq_table_name":
      f" SELECT * FROM {constants.PROJECT_ID}."
      f"{constants.AQS_RAW_DATASET}.nitrogen_dioxide",
    "data_source": "aqs",
    "ingestion_layer": "bq_warehouse",
    "warehouse_table_name":
      f"{constants.BQ_WH_DATASET}.aqs_nitrogen_dioxide",
    "layer_name": "nitrogen_dioxide",
    "layer_url": "https://aqs.epa.gov/data/api/annualData/byState?email="
                 + constants.AQS_EMAIL + "&key=" + constants.AQS_KEY +
                 "&param=42602&bdate={}0515&edate={}0515&state=36",
    "parsed_gcs_file_path": f"parsed/nitrogen_dioxide/"
                            f"{constants.CURRENT_DATE}/"
                            "nitrogen_dioxide_{}.json",

  },
  {
    "task_name": "ozone_wh_ingestion",
    "bq_table_name":
      f" SELECT * FROM {constants.PROJECT_ID}."
      f"{constants.AQS_RAW_DATASET}.ozone",
    "data_source": "aqs",
    "ingestion_layer": "bq_warehouse",
    "warehouse_table_name":
      f"{constants.BQ_WH_DATASET}.aqs_ozone",
    "layer_name": "ozone",
    "layer_url": "https://aqs.epa.gov/data/api/annualData/byState?email="
                 + constants.AQS_EMAIL + "&key=" + constants.AQS_KEY +
                 "&param=44201&bdate={}0515&edate={}0515&state=36",
    "parsed_gcs_file_path": f"parsed/ozone/"
                            f"{constants.CURRENT_DATE}/"
                            "ozone_{}.json",

  },
  {
    "task_name": "pm_25_wh_ingestion",
    "bq_table_name":
      f" SELECT * FROM {constants.PROJECT_ID}."
      f"{constants.AQS_RAW_DATASET}.pm_25",
    "data_source": "aqs",
    "ingestion_layer": "bq_warehouse",
    "warehouse_table_name":
      f"{constants.BQ_WH_DATASET}.aqs_pm_25",
    "layer_name": "pm_25",
    "layer_url": "https://aqs.epa.gov/data/api/annualData/byState?email="
                 + constants.AQS_EMAIL + "&key=" + constants.AQS_KEY +
                 "&param=88101&bdate={}0515&edate={}0515&state=36",
    "parsed_gcs_file_path": f"parsed/pm_25/"
                            f"{constants.CURRENT_DATE}/"
                            "pm_25_{}.json",

  },
  {
    "task_name": "sulfur_dioxide_wh_ingestion",
    "bq_table_name":
      f" SELECT * FROM {constants.PROJECT_ID}."
      f"{constants.AQS_RAW_DATASET}.sulfur_dioxide",
    "data_source": "aqs",
    "ingestion_layer": "bq_warehouse",
    "warehouse_table_name":
      f"{constants.BQ_WH_DATASET}.aqs_sulfur_dioxide",
    "layer_name": "sulfur_dioxide",
    "layer_url": "https://aqs.epa.gov/data/api/annualData/byState?email="
                 + constants.AQS_EMAIL + "&key=" + constants.AQS_KEY +
                 "&param=42401&bdate={}0515&edate={}0515&state=36",
    "parsed_gcs_file_path": f"parsed/sulfur_dioxide/"
                            f"{constants.CURRENT_DATE}/"
                            "sulfur_dioxide_{}.json",

  },
  {
    "task_name": "ethane_wh_ingestion",
    "bq_table_name":
      f" SELECT * FROM {constants.PROJECT_ID}."
      f"{constants.AQS_RAW_DATASET}.ethane",
    "data_source": "aqs",
    "ingestion_layer": "bq_warehouse",
    "warehouse_table_name":
      f"{constants.BQ_WH_DATASET}.aqs_ethane",
    "layer_name": "ethane",
    "layer_url": "https://aqs.epa.gov/data/api/annualData/byState?email="
                 + constants.AQS_EMAIL + "&key=" + constants.AQS_KEY +
                 "&param=43202&bdate={}0515&edate={}0515&state=36",
    "parsed_gcs_file_path": f"parsed/ethane/"
                            f"{constants.CURRENT_DATE}/"
                            "ethane_{}.json",

  },
  {
    "task_name": "toxics_and_carbonyls_wh_ingestion",
    "bq_table_name":
      f" SELECT * FROM {constants.PROJECT_ID}."
      f"{constants.AQS_RAW_DATASET}.toxics_and_carbonyls",
    "data_source": "aqs",
    "ingestion_layer": "bq_warehouse",
    "warehouse_table_name":
      f"{constants.BQ_WH_DATASET}.aqs_toxics_and_carbonyls",
    "layer_name": "toxics_and_carbonyls",
    "layer_url": "https://aqs.epa.gov/data/api/annualData/byState?email="
                 + constants.AQS_EMAIL + "&key=" + constants.AQS_KEY +
                 "&param=45201,45202,45203,"
                 "45204,45109&bdate={}0515&edate={}0515&state=36",
    "parsed_gcs_file_path": f"parsed/toxics_and_carbonyls/"
                            f"{constants.CURRENT_DATE}/"
                            "toxics_and_carbonyls_{}.json",

  },
  # AQS JOB AUDIT WH BQ INGESTION MAIN TASKS
  {
    "task_name":
      "black_carbon_pm2_5_corrected_bq_wh_job_audit_ingestion",
    "bq_table_name": f"{constants.BQ_WH_DATASET}."
                     f"aqs_black_carbon_pm2_5_corrected",
    "query": f" SELECT COUNT(*) AS COUNT FROM"
             f" {constants.BQ_WH_DATASET}."
             f"aqs_black_carbon_pm2_5_corrected"
             f" WHERE ingestion_timestamp = ",
    "gcs_bucket_name": constants.AQS_BUCKET_NAME,
    "parsed_gcs_file_path": f"parsed/black_carbon_pm2_5_corrected/"
                            f"{constants.CURRENT_DATE}/"
                            "black_carbon_pm2_5_corrected_{}.json",
    "data_source": "aqs",
    "ingestion_layer": "bq_wh_job_audit",
    "layer_name": "black_carbon_pm2_5_corrected",
    "layer_url": "https://aqs.epa.gov/data/api/annualData/byState?email="
                 + constants.AQS_EMAIL + "&key=" + constants.AQS_KEY +
                 "&param=88317&bdate={}0515&edate={}0515&state=36"
  },
  {
    "task_name": "carbon_monoxide_bq_wh_job_audit_ingestion",
    "query":
      f" SELECT COUNT(*) AS COUNT FROM "
      f"{constants.BQ_WH_DATASET}"
      f".aqs_carbon_monoxide "
      f"WHERE ingestion_timestamp = ",
    "bq_table_name": f"{constants.BQ_WH_DATASET}"
                     f".aqs_carbon_monoxide",
    "gcs_bucket_name": constants.AQS_BUCKET_NAME,
    "parsed_gcs_file_path": f"parsed/carbon_monoxide/"
                            f"{constants.CURRENT_DATE}/"
                            "carbon_monoxide_{}.json",
    "data_source": "aqs",
    "ingestion_layer": "bq_wh_job_audit",
    "layer_name": "carbon_monoxide",
    "layer_url": "https://aqs.epa.gov/data/api/annualData/byState?email="
                 + constants.AQS_EMAIL + "&key=" + constants.AQS_KEY +
                 "&param=42101&bdate={}0515&edate={}0515&state=36"
  },
  {
    "task_name": "formaldehyde_bq_wh_job_audit_ingestion",
    "query": f" SELECT COUNT(*) AS COUNT "
             f"FROM {constants.BQ_WH_DATASET}"
             f".aqs_formaldehyde "
             f"WHERE ingestion_timestamp = ",
    "bq_table_name": f"{constants.BQ_WH_DATASET}.aqs_formaldehyde",
    "gcs_bucket_name": constants.AQS_BUCKET_NAME,
    "parsed_gcs_file_path": f"parsed/formaldehyde/"
                            f"{constants.CURRENT_DATE}/"
                            "formaldehyde_{}.json",
    "data_source": "aqs",
    "ingestion_layer": "bq_wh_job_audit",
    "layer_name": "formaldehyde",
    "layer_url": "https://aqs.epa.gov/data/api/annualData/byState?email="
                 + constants.AQS_EMAIL + "&key=" + constants.AQS_KEY +
                 "&param=43502&bdate={}0515&edate={}0515&state=36"
  },
  {
    "task_name": "nitric_oxide_bq_wh_job_audit_ingestion",
    "query": f" SELECT COUNT(*) AS COUNT FROM "
             f"{constants.BQ_WH_DATASET}"
             f".aqs_nitric_oxide "
             f"WHERE ingestion_timestamp = ",
    "bq_table_name": f"{constants.BQ_WH_DATASET}.aqs_nitric_oxide",
    "gcs_bucket_name": constants.AQS_BUCKET_NAME,
    "parsed_gcs_file_path": f"parsed/nitric_oxide/"
                            f"{constants.CURRENT_DATE}/"
                            "nitric_oxide_{}.json",
    "data_source": "aqs",
    "ingestion_layer": "bq_wh_job_audit",
    "layer_name": "nitric_oxide",
    "layer_url": "https://aqs.epa.gov/data/api/annualData/byState?email="
                 + constants.AQS_EMAIL + "&key=" + constants.AQS_KEY +
                 "&param=42601&bdate={}0515&edate={}0515&state=36"
  },
  {
    "task_name": "nitrogen_dioxide_bq_wh_job_audit_ingestion",
    "query": f" SELECT COUNT(*) AS COUNT FROM "
             f"{constants.BQ_WH_DATASET}"
             f".aqs_nitrogen_dioxide "
             f"WHERE ingestion_timestamp = ",
    "bq_table_name": f"{constants.BQ_WH_DATASET}.aqs_nitrogen_dioxide",
    "gcs_bucket_name": constants.AQS_BUCKET_NAME,
    "parsed_gcs_file_path": f"parsed/nitrogen_dioxide/"
                            f"{constants.CURRENT_DATE}/"
                            "nitrogen_dioxide_{}.json",
    "data_source": "aqs",
    "ingestion_layer": "bq_wh_job_audit",
    "layer_name": "nitrogen_dioxide",
    "layer_url": "https://aqs.epa.gov/data/api/annualData/byState?email="
                 + constants.AQS_EMAIL + "&key=" + constants.AQS_KEY +
                 "&param=42602&bdate={}0515&edate={}0515&state=36"
  },
  {
    "task_name": "ozone_bq_wh_job_audit_ingestion",
    "query": f" SELECT COUNT(*) AS COUNT "
             f"FROM {constants.BQ_WH_DATASET}"
             f".aqs_ozone "
             f"WHERE ingestion_timestamp = ",
    "bq_table_name": f"{constants.BQ_WH_DATASET}.aqs_ozone",
    "gcs_bucket_name": constants.AQS_BUCKET_NAME,
    "parsed_gcs_file_path": f"parsed/ozone/"
                            f"{constants.CURRENT_DATE}/"
                            "ozone_{}.json",
    "data_source": "aqs",
    "ingestion_layer": "bq_wh_job_audit",
    "layer_name": "ozone",
    "layer_url": "https://aqs.epa.gov/data/api/annualData/byState?email="
                 + constants.AQS_EMAIL + "&key=" + constants.AQS_KEY +
                 "&param=44201&bdate={}0515&edate={}0515&state=36"
  },
  {
    "task_name": "pm_25_bq_wh_job_audit_ingestion",
    "query": f" SELECT COUNT(*) AS COUNT "
             f"FROM {constants.BQ_WH_DATASET}"
             f".aqs_pm_25 WHERE ingestion_timestamp = ",
    "bq_table_name": f"{constants.BQ_WH_DATASET}.aqs_pm_25",
    "gcs_bucket_name": constants.AQS_BUCKET_NAME,
    "parsed_gcs_file_path": f"parsed/pm_25/"
                            f"{constants.CURRENT_DATE}/"
                            "pm_25_{}.json",
    "data_source": "aqs",
    "ingestion_layer": "bq_wh_job_audit",
    "layer_name": "pm_25",
    "layer_url": "https://aqs.epa.gov/data/api/annualData/byState?email="
                 + constants.AQS_EMAIL + "&key=" + constants.AQS_KEY +
                 "&param=88101&bdate={}0515&edate={}0515&state=36"
  },
  {
    "task_name": "sulfur_dioxide_bq_wh_job_audit_ingestion",
    "query": f" SELECT COUNT(*) AS COUNT FROM "
             f"{constants.BQ_WH_DATASET}"
             f".aqs_sulfur_dioxide "
             f"WHERE ingestion_timestamp = ",
    "bq_table_name": f"{constants.BQ_WH_DATASET}.aqs_sulfur_dioxide",
    "gcs_bucket_name": constants.AQS_BUCKET_NAME,
    "parsed_gcs_file_path": f"parsed/sulfur_dioxide/"
                            f"{constants.CURRENT_DATE}/"
                            "sulfur_dioxide_{}.json",
    "data_source": "aqs",
    "ingestion_layer": "bq_wh_job_audit",
    "layer_name": "sulfur_dioxide",
    "layer_url": "https://aqs.epa.gov/data/api/annualData/byState?email="
                 + constants.AQS_EMAIL + "&key=" + constants.AQS_KEY +
                 "&param=42401&bdate={}0515&edate={}0515&state=36",
  },
  {
    "task_name": "ethane_bq_wh_job_audit_ingestion",
    "query": f" SELECT COUNT(*) AS COUNT "
             f"FROM {constants.BQ_WH_DATASET}"
             f".aqs_ethane"
             f" WHERE ingestion_timestamp = ",
    "bq_table_name": f"{constants.BQ_WH_DATASET}.aqs_ethane",
    "gcs_bucket_name": constants.AQS_BUCKET_NAME,
    "parsed_gcs_file_path": f"parsed/ethane/"
                            f"{constants.CURRENT_DATE}/"
                            "ethane_{}.json",
    "data_source": "aqs",
    "ingestion_layer": "bq_wh_job_audit",
    "layer_name": "ethane",
    "layer_url": "https://aqs.epa.gov/data/api/annualData/byState?email="
                 + constants.AQS_EMAIL + "&key=" + constants.AQS_KEY +
                 "&param=43202&bdate={}0515&edate={}0515&state=36"
  },
  {
    "task_name": "toxics_and_carbonyls_bq_wh_job_audit_ingestion",
    "query": f" SELECT COUNT(*) AS COUNT FROM "
             f"{constants.BQ_WH_DATASET}"
             f".aqs_toxics_and_carbonyls"
             f" WHERE ingestion_timestamp = ",
    "bq_table_name": f"{constants.BQ_WH_DATASET}.aqs_toxics_and_carbonyls",
    "gcs_bucket_name": constants.AQS_BUCKET_NAME,
    "parsed_gcs_file_path": f"parsed/toxics_and_carbonyls/"
                            f"{constants.CURRENT_DATE}/"
                            "toxics_and_carbonyls_{}.json",
    "data_source": "aqs",
    "ingestion_layer": "bq_wh_job_audit",
    "layer_name": "toxics_and_carbonyls",
    "layer_url": "https://aqs.epa.gov/data/api/annualData/byState?email="
                 + constants.AQS_EMAIL + "&key=" + constants.AQS_KEY +
                 "&param=45201,45202,45203,45204,"
                 "45109&bdate={}0515&edate={}0515&state=36"
  },
  # REPORTING AQS BQ INGESTION MAIN TASKS
  {
    "task_name": "black_carbon_pm2_5_corrected_reporting_ingestion",
    "data_source": "aqs",
    "ingestion_layer": "aqs_bq_reporting",
    "reporting_table_name":
      f"{constants.BQ_REPORTING_DATASET}."
      f"aqs_black_carbon_pm2_5_corrected",
    "source_table_name":
      "CALL `" + constants.PROJECT_ID + "." + constants.REPORTING_VIEWS +
      ".sp_black_carbon_pm2_5_corrected`( '{}');",
    "layer_name": "black_carbon_pm2_5_corrected",
    "layer_url": "https://aqs.epa.gov/data/api/annualData/byState?email="
                 + constants.AQS_EMAIL + "&key=" + constants.AQS_KEY +
                 "&param=88317,84313&bdate={}0515&edate={}0515&state=36",
    "parsed_gcs_file_path": f"parsed/black_carbon_pm2_5_corrected/"
                            f"{constants.CURRENT_DATE}/"
                            "black_carbon_pm2_5_corrected_{}.json",

  },
  {
    "task_name": "carbon_monoxide_reporting_ingestion",
    "data_source": "aqs",
    "ingestion_layer": "aqs_bq_reporting",
    "reporting_table_name":
      f"{constants.BQ_REPORTING_DATASET}."
      f"aqs_carbon_monoxide",
    "source_table_name":
      "CALL `" + constants.PROJECT_ID + "." + constants.REPORTING_VIEWS +
      ".sp_carbon_monoxide`( '{}');",
    "layer_name": "carbon_monoxide",
    "layer_url": "https://aqs.epa.gov/data/api/annualData/byState?email="
                 + constants.AQS_EMAIL + "&key=" + constants.AQS_KEY +
                 "&param=42101&bdate={}0515&edate={}0515&state=36",
    "parsed_gcs_file_path": f"parsed/carbon_monoxide/"
                            f"{constants.CURRENT_DATE}/"
                            "carbon_monoxide_{}.json",
  },
  {
    "task_name": "formaldehyde_reporting_ingestion",
    "data_source": "aqs",
    "ingestion_layer": "aqs_bq_reporting",
    "reporting_table_name":
      f"{constants.BQ_REPORTING_DATASET}."
      f"aqs_formaldehyde",
    "source_table_name":
      "CALL `" + constants.PROJECT_ID + "." + constants.REPORTING_VIEWS +
      ".sp_formaldehyde`( '{}');",
    "layer_name": "formaldehyde",
    "layer_url": "https://aqs.epa.gov/data/api/annualData/byState?email="
                 + constants.AQS_EMAIL + "&key=" + constants.AQS_KEY +
                 "&param=43502&bdate={}0515&edate={}0515&state=36",
    "parsed_gcs_file_path": f"parsed/formaldehyde/"
                            f"{constants.CURRENT_DATE}/"
                            "formaldehyde_{}.json",
  },
  {
    "task_name": "nitric_oxide_reporting_ingestion",
    "data_source": "aqs",
    "ingestion_layer": "aqs_bq_reporting",
    "reporting_table_name":
      f"{constants.BQ_REPORTING_DATASET}."
      f"aqs_nitric_oxide",
    "source_table_name":
      "CALL `" + constants.PROJECT_ID + "." + constants.REPORTING_VIEWS +
      ".sp_nitric_oxide`( '{}');",
    "layer_name": "nitric_oxide",
    "layer_url": "https://aqs.epa.gov/data/api/annualData/byState?email="
                 + constants.AQS_EMAIL + "&key=" + constants.AQS_KEY +
                 "&param=42601&bdate={}0515&edate={}0515&state=36",
    "parsed_gcs_file_path": f"parsed/nitric_oxide/"
                            f"{constants.CURRENT_DATE}/"
                            "nitric_oxide_{}.json",
  },
  {
    "task_name": "nitrogen_dioxide_reporting_ingestion",
    "data_source": "aqs",
    "ingestion_layer": "aqs_bq_reporting",
    "reporting_table_name":
      f"{constants.BQ_REPORTING_DATASET}."
      f"aqs_nitrogen_dioxide",
    "source_table_name":
      "CALL `" + constants.PROJECT_ID + "." + constants.REPORTING_VIEWS +
      ".sp_nitrogen_dioxide`( '{}');",
    "layer_name": "nitrogen_dioxide",
    "layer_url": "https://aqs.epa.gov/data/api/annualData/byState?email="
                 + constants.AQS_EMAIL + "&key=" + constants.AQS_KEY +
                 "&param=42602,42603&bdate={}0515&edate={}0515&state=36",
    "parsed_gcs_file_path": f"parsed/nitrogen_dioxide/"
                            f"{constants.CURRENT_DATE}/"
                            "nitrogen_dioxide_{}.json",

  },
  {
    "task_name": "ozone_reporting_ingestion",
    "data_source": "aqs",
    "ingestion_layer": "aqs_bq_reporting",
    "reporting_table_name":
      f"{constants.BQ_REPORTING_DATASET}."
      f"aqs_ozone",
    "source_table_name":
      "CALL `" + constants.PROJECT_ID + "." + constants.REPORTING_VIEWS +
      ".sp_ozone`( '{}');",
    "layer_name": "ozone",
    "layer_url": "https://aqs.epa.gov/data/api/annualData/byState?email="
                 + constants.AQS_EMAIL + "&key=" + constants.AQS_KEY +
                 "&param=44201&bdate={}0515&edate={}0515&state=36",
    "parsed_gcs_file_path": f"parsed/ozone/"
                            f"{constants.CURRENT_DATE}/"
                            "ozone_{}.json",
  },
  {
    "task_name": "pm_25_reporting_ingestion",
    "data_source": "aqs",
    "ingestion_layer": "aqs_bq_reporting",
    "reporting_table_name":
      f"{constants.BQ_REPORTING_DATASET}."
      f"aqs_pm_25",
    "source_table_name":
      "CALL `" + constants.PROJECT_ID + "." + constants.REPORTING_VIEWS +
      ".sp_pm_25`( '{}');",
    "layer_name": "pm_25",
    "layer_url": "https://aqs.epa.gov/data/api/annualData/byState?email="
                 + constants.AQS_EMAIL + "&key=" + constants.AQS_KEY +
                 "&param=88101,88502&bdate={}0515&edate={}0515&state=36",
    "parsed_gcs_file_path": f"parsed/pm_25/"
                            f"{constants.CURRENT_DATE}/"
                            "pm_25_{}.json",
  },
  {
    "task_name": "sulfur_dioxide_reporting_ingestion",
    "data_source": "aqs",
    "ingestion_layer": "aqs_bq_reporting",
    "reporting_table_name":
      f"{constants.BQ_REPORTING_DATASET}."
      f"aqs_sulfur_dioxide",
    "source_table_name":
      "CALL `" + constants.PROJECT_ID + "." + constants.REPORTING_VIEWS +
      ".sp_sulfur_dioxide`( '{}');",
    "layer_name": "sulfur_dioxide",
    "layer_url": "https://aqs.epa.gov/data/api/annualData/byState?email="
                 + constants.AQS_EMAIL + "&key=" + constants.AQS_KEY +
                 "&param=42401&bdate={}0515&edate={}0515&state=36",
    "parsed_gcs_file_path": f"parsed/sulfur_dioxide/"
                            f"{constants.CURRENT_DATE}/"
                            "sulfur_dioxide_{}.json",
  },
  {
    "task_name": "ethane_reporting_ingestion",
    "data_source": "aqs",
    "ingestion_layer": "aqs_bq_reporting",
    "reporting_table_name":
      f"{constants.BQ_REPORTING_DATASET}."
      f"aqs_ethane",
    "source_table_name":
      "CALL `" + constants.PROJECT_ID + "." + constants.REPORTING_VIEWS +
      ".sp_ethane`( '{}');",
    "layer_name": "ethane",
    "layer_url": "https://aqs.epa.gov/data/api/annualData/byState?email="
                 + constants.AQS_EMAIL + "&key=" + constants.AQS_KEY +
                 "&param=43202&bdate={}0515&edate={}0515&state=36",
    "parsed_gcs_file_path": f"parsed/ethane/"
                            f"{constants.CURRENT_DATE}/"
                            "ethane_{}.json",
  },
  {
    "task_name": "toxics_and_carbonyls_reporting_ingestion",
    "data_source": "aqs",
    "ingestion_layer": "aqs_bq_reporting",
    "reporting_table_name":
      f"{constants.BQ_REPORTING_DATASET}."
      f"aqs_toxics_and_carbonyls",
    "source_table_name":
      "CALL `" + constants.PROJECT_ID + "." + constants.REPORTING_VIEWS +
      ".sp_toxics_and_carbonyls`( '{}');",
    "layer_name": "toxics_and_carbonyls",
    "layer_url": "https://aqs.epa.gov/data/api/annualData/byState?email="
                 + constants.AQS_EMAIL + "&key=" + constants.AQS_KEY +
                 "&param=45201,45202,45203,"
                 "45204,45109&bdate={}0515&edate={}0515&state=36",
    "parsed_gcs_file_path": f"parsed/toxics_and_carbonyls/"
                            f"{constants.CURRENT_DATE}/"
                            "toxics_and_carbonyls_{}.json",
  },
  # AQS JOB AUDIT REPORTING BQ INGESTION MAIN TASKS
  {
    "task_name":
      "black_carbon_pm2_5_corrected_bq_reporting_"
      "job_audit_ingestion",
    "bq_table_name": f"{constants.BQ_REPORTING_DATASET}."
                     f"aqs_black_carbon_pm2_5_corrected",
    "query": f" SELECT COUNT(*) AS "
             f"COUNT FROM {constants.BQ_REPORTING_DATASET}."
             f"aqs_black_carbon_pm2_5_corrected"
             f" WHERE ingestion_timestamp = ",
    "gcs_bucket_name": constants.AQS_BUCKET_NAME,
    "parsed_gcs_file_path": f"parsed/black_carbon_pm2_5_corrected/"
                            f"{constants.CURRENT_DATE}/"
                            "black_carbon_pm2_5_corrected_{}.json",
    "data_source": "aqs",
    "ingestion_layer": "bq_reporting_job_audit",
    "layer_name": "black_carbon_pm2_5_corrected",
    "layer_url": "https://aqs.epa.gov/data/api/annualData/byState?email="
                 + constants.AQS_EMAIL + "&key=" + constants.AQS_KEY +
                 "&param=88317&bdate={}0515&edate={}0515&state=36"
  },
  {
    "task_name": "carbon_monoxide_bq_reporting_job_audit_ingestion",
    "query":
      f" SELECT COUNT(*) AS COUNT FROM "
      f"{constants.BQ_REPORTING_DATASET}"
      f".aqs_carbon_monoxide "
      f"WHERE ingestion_timestamp = ",
    "bq_table_name": f"{constants.BQ_REPORTING_DATASET}.aqs_carbon_monoxide",
    "gcs_bucket_name": constants.AQS_BUCKET_NAME,
    "parsed_gcs_file_path": f"parsed/carbon_monoxide/"
                            f"{constants.CURRENT_DATE}/"
                            "carbon_monoxide_{}.json",
    "data_source": "aqs",
    "ingestion_layer": "bq_reporting_job_audit",
    "layer_name": "carbon_monoxide",
    "layer_url": "https://aqs.epa.gov/data/api/annualData/byState?email="
                 + constants.AQS_EMAIL + "&key=" + constants.AQS_KEY +
                 "&param=42101&bdate={}0515&edate={}0515&state=36"
  },
  {
    "task_name": "formaldehyde_bq_reporting_job_audit_ingestion",
    "query": f" SELECT COUNT(*) AS COUNT "
             f"FROM {constants.BQ_REPORTING_DATASET}"
             f".aqs_formaldehyde "
             f"WHERE ingestion_timestamp = ",
    "bq_table_name": f"{constants.BQ_REPORTING_DATASET}.aqs_formaldehyde",
    "gcs_bucket_name": constants.AQS_BUCKET_NAME,
    "parsed_gcs_file_path": f"parsed/formaldehyde/"
                            f"{constants.CURRENT_DATE}/"
                            "formaldehyde_{}.json",
    "data_source": "aqs",
    "ingestion_layer": "bq_reporting_job_audit",
    "layer_name": "formaldehyde",
    "layer_url": "https://aqs.epa.gov/data/api/annualData/byState?email="
                 + constants.AQS_EMAIL + "&key=" + constants.AQS_KEY +
                 "&param=43502&bdate={}0515&edate={}0515&state=36"
  },
  {
    "task_name": "nitric_oxide_bq_reporting_"
                 "job_audit_ingestion",
    "query": f" SELECT COUNT(*) AS COUNT FROM "
             f"{constants.BQ_REPORTING_DATASET}"
             f".aqs_nitric_oxide WHERE ingestion_timestamp = ",
    "bq_table_name": f"{constants.BQ_REPORTING_DATASET}.aqs_nitric_oxide",
    "gcs_bucket_name": constants.AQS_BUCKET_NAME,
    "parsed_gcs_file_path": f"parsed/nitric_oxide/"
                            f"{constants.CURRENT_DATE}/"
                            "nitric_oxide_{}.json",
    "data_source": "aqs",
    "ingestion_layer": "bq_reporting_job_audit",
    "layer_name": "nitric_oxide",
    "layer_url": "https://aqs.epa.gov/data/api/annualData/byState?email="
                 + constants.AQS_EMAIL + "&key=" + constants.AQS_KEY +
                 "&param=42601&bdate={}0515&edate={}0515&state=36"
  },
  {
    "task_name": "nitrogen_dioxide_bq_reporting_"
                 "job_audit_ingestion",
    "query": f" SELECT COUNT(*) AS COUNT FROM "
             f"{constants.BQ_REPORTING_DATASET}"
             f".aqs_nitrogen_dioxide "
             f"WHERE ingestion_timestamp = ",
    "bq_table_name": f"{constants.BQ_REPORTING_DATASET}.aqs_nitrogen_dioxide",
    "gcs_bucket_name": constants.AQS_BUCKET_NAME,
    "parsed_gcs_file_path": f"parsed/nitrogen_dioxide/"
                            f"{constants.CURRENT_DATE}/"
                            "nitrogen_dioxide_{}.json",
    "data_source": "aqs",
    "ingestion_layer": "bq_reporting_job_audit",
    "layer_name": "nitrogen_dioxide",
    "layer_url": "https://aqs.epa.gov/data/api/annualData/byState?email="
                 + constants.AQS_EMAIL + "&key=" + constants.AQS_KEY +
                 "&param=42602&bdate={}0515&edate={}0515&state=36"
  },
  {
    "task_name": "ozone_bq_reporting_job_"
                 "audit_ingestion",
    "query": f" SELECT COUNT(*) AS COUNT "
             f"FROM {constants.BQ_REPORTING_DATASET}"
             f".aqs_ozone WHERE ingestion_timestamp = ",
    "bq_table_name": f"{constants.BQ_REPORTING_DATASET}.aqs_ozone",
    "gcs_bucket_name": constants.AQS_BUCKET_NAME,
    "parsed_gcs_file_path": f"parsed/ozone/"
                            f"{constants.CURRENT_DATE}/"
                            "ozone_{}.json",
    "data_source": "aqs",
    "ingestion_layer": "bq_reporting_job_audit",
    "layer_name": "ozone",
    "layer_url": "https://aqs.epa.gov/data/api/annualData/byState?email="
                 + constants.AQS_EMAIL + "&key=" + constants.AQS_KEY +
                 "&param=44201&bdate={}0515&edate={}0515&state=36"
  },
  {
    "task_name": "pm_25_bq_reporting_job_audit_ingestion",
    "query": f" SELECT COUNT(*) AS COUNT "
             f"FROM {constants.BQ_REPORTING_DATASET}"
             f".aqs_pm_25 WHERE ingestion_timestamp = ",
    "bq_table_name": f"{constants.BQ_REPORTING_DATASET}.aqs_pm_25",
    "gcs_bucket_name": constants.AQS_BUCKET_NAME,
    "parsed_gcs_file_path": f"parsed/pm_25/"
                            f"{constants.CURRENT_DATE}/"
                            "pm_25_{}.json",
    "data_source": "aqs",
    "ingestion_layer": "bq_reporting_job_audit",
    "layer_name": "pm_25",
    "layer_url": "https://aqs.epa.gov/data/api/annualData/byState?email="
                 + constants.AQS_EMAIL + "&key=" + constants.AQS_KEY +
                 "&param=88101&bdate={}0515&edate={}0515&state=36"
  },
  {
    "task_name": "sulfur_dioxide_bq_reporting_job_audit_ingestion",
    "query": f" SELECT COUNT(*) AS COUNT FROM "
             f"{constants.BQ_REPORTING_DATASET}"
             f".aqs_sulfur_dioxide "
             f"WHERE ingestion_timestamp = ",
    "bq_table_name": f"{constants.BQ_REPORTING_DATASET}.aqs_sulfur_dioxide",
    "gcs_bucket_name": constants.AQS_BUCKET_NAME,
    "parsed_gcs_file_path": f"parsed/sulfur_dioxide/"
                            f"{constants.CURRENT_DATE}/"
                            "sulfur_dioxide_{}.json",
    "data_source": "aqs",
    "ingestion_layer": "bq_reporting_job_audit",
    "layer_name": "sulfur_dioxide",
    "layer_url": "https://aqs.epa.gov/data/api/annualData/byState?email="
                 + constants.AQS_EMAIL + "&key=" + constants.AQS_KEY +
                 "&param=42401&bdate={}0515&edate={}0515&state=36",
  },
  {
    "task_name": "ethane_bq_reporting_job_audit_ingestion",
    "query": f" SELECT COUNT(*) AS COUNT "
             f"FROM {constants.BQ_REPORTING_DATASET}"
             f".aqs_ethane WHERE ingestion_timestamp = ",
    "bq_table_name": f"{constants.BQ_REPORTING_DATASET}.aqs_ethane",
    "gcs_bucket_name": constants.AQS_BUCKET_NAME,
    "parsed_gcs_file_path": f"parsed/ethane/"
                            f"{constants.CURRENT_DATE}/"
                            "ethane_{}.json",
    "data_source": "aqs",
    "ingestion_layer": "bq_reporting_job_audit",
    "layer_name": "ethane",
    "layer_url": "https://aqs.epa.gov/data/api/annualData/byState?email="
                 + constants.AQS_EMAIL + "&key=" + constants.AQS_KEY +
                 "&param=43202&bdate={}0515&edate={}0515&state=36"
  },
  {
    "task_name": "toxics_and_carbonyls_bq_reporting_job_audit_ingestion",
    "query": f" SELECT COUNT(*) AS COUNT FROM "
             f"{constants.BQ_REPORTING_DATASET}"
             f".aqs_toxics_and_carbonyls "
             f"WHERE ingestion_timestamp = ",
    "bq_table_name": f"{constants.BQ_REPORTING_DATASET}"
                     f".aqs_toxics_and_carbonyls",
    "gcs_bucket_name": constants.AQS_BUCKET_NAME,
    "parsed_gcs_file_path": f"parsed/toxics_and_carbonyls/"
                            f"{constants.CURRENT_DATE}/"
                            "toxics_and_carbonyls_{}.json",
    "data_source": "aqs",
    "ingestion_layer": "bq_reporting_job_audit",
    "layer_name": "toxics_and_carbonyls",
    "layer_url": "https://aqs.epa.gov/data/api/annualData/byState?email="
                 + constants.AQS_EMAIL + "&key=" + constants.AQS_KEY +
                 "&param=45201,45202,45203,45204,"
                 "45109&bdate={}0515&edate={}0515&state=36"
  },

]

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
