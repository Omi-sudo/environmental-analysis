# Cloud run code to transfer FTP data from GCS bucket to BigQuery.

## Prerequisites

- Cloud Run uses the same service account use by Cloud Composer, for detailed permission please refer TDD.

## Overview
Folder "composer/dags" contains all the python files and its utility module for all 4 dags ArcGIS_TO_GCP, SOCRATA_TO_GCP ,AQS_TO_GCP and FTP_TO_GCP

## Code Structure.
### Folder composer/dags

1. aqs_to_gcp.py - Main module to run the AQS_TO_GCP pipeline.
2. arcgis_to_gcp.py - Main module to run the ArcGIS_TO_GCP pipeline.
3. socrata_to_gcp.py - Main module to run the SOCRATA_TO_GCP pipeline.
4. ftp_to_gcp.py - Main module to run the FTP_TO_GCP pipeline.
5. config.py - Config file for cloud composer.This contains values in form of key value pairs.This makes easy to add the new end point.
6. constant.py - File containing constants variables.
7. storage_util.py - A utility module to connect and insert in GCS.
8. bq_utils.py - A utility module to connect, read and insert data to BigQuery.
9. job_audit_utils.py - A utility module to insert job audit logs into the BigQuery.
10.utils.py - A utility module which contains user defined functions which is required to execute FTP_TO_GCP pipeline. 


## How to add new data layer?

###For ArcGIS, Socrata and AQS

1.To add a new data layer you just need to add a new mapping in respective variable present in composer/dag/config.py
<br>
<br>e.g: To add new socrata data layer you need to add new mapping under SOCRATA_TASKS_CONFIG for the respective tasks.
<br>Note:You also need add respective cloud run mapping as mentioned in README.md files for respective apis.

###For FTP

1.To add the new FTP layer add the new bucket name(where the new files will be landed) in composer admin variable and change the respective table name in  composer/dag/config file in FTP_TASKS_CONFIG section.
