# Cloud run code to transfer data from Socrata Data Endpoints to GCS

## Prerequisites

- Service Account for Cloud Run: </br>
  - Cloud Run uses the same service account use by Cloud Composer, for detailed permission please refer TDD.

- GCS Bucket to stage data

## GCS file path
```
-For raw data : [BUCKET_NAME]/raw/[WEBSERVICE_NAME]/[CURRENT_DATE]/[WEBSERVICE_NAME]_unix_ingestion_timestamp.json
-For parsed data: [BUCKET_NAME]/parsed/[WEBSERVICE_NAME]/[CURRENT_DATE]/[WEBSERVICE_NAME]_unix_ingestion_timestamp.json 
```


## Overview
As soon as get request has been sent to the cloud run url it will fetch the data from rest endpoint for the different datasets hosted at socrata/soda apis platform and write into the GCS buckets.

All the data written under the given GCS bucket. Raw data will be written in the raw folder structure and parsed data will be written in parsed folder structure as mentioned above in GCS file path. 

## Folder Structure 

.dockerignore </br>
Dockerfile </br>
main.py </br>
main_test.py </br>
requirements.txt </br>

## Code Structure & Description

1. main.py - Python module which is the entry point for the program execution. 
   This module has two endpoints:
   - /process_raw_layer: which will fetch the data from socrata/soda api platform and write into the specified raw GCS location 
     for the specified pollutants mentioned in config.py.
   - /process_parse_layer: this will fetch the data from the GCS location for a specific pollutant and write into the specified parse GCS location.
   
2. main_test.py - this module contains unit test cases for main.py module
  
3. requirements.txt - File containing list of PYPI packages with the appropriate versions required for pipeline execution.

4. Dockerfile - Dockerfile to build an artifact registry image.

5. dockerignore - File that allows to mention a list of files and/or directories which we need to ignore while building the image.


### Utility Modules
1. socrata_parsing_util.py - This module contains the raw data parsing logic required for socrata cloud run pipeline
2. constant.py - This module contains constants variables which is being used frequently in pipeline.
3. config.py - Config file for cloud run. It contains the all the info needed for pipeline execution in key, val pairs. This makes easy to introduce a new data_layer/pollutant.
4. bq_utils.py - This module contains all the functions needs to interact with BigQuery
5. storage_util.py - This module contains all the functions needs to interact with Cloud Storage.
6. secrets_util.py - This is the utility module to access the secrets stored in gcp environment
7. job_audit_utils.py - This module contains function to gather all the audit metrics of pipeline


## How to introduce a new data layer in pipeline ?

In order to add a new mapping for a new data layer refer the existing mapping at 
socrata_data_layer_and_gcp_mapping variable present in cloud_run/common/config.py
## Spin Up Cloud Run service from local system
To create a cloud run service for this pipeline module, navigate to the root directory environmental-analysis as the present working directory,
execute pwd command on terminal to know present working directory, and cd {/path} to navigate on a certain directory.

once you're at environmental-analysis, execute below-mentioned command. The command will execute the environmental-analysis/cloud_run/socrata_cloudbuild.yaml which will create an artifact registry than deploy it as a cloud run service.
```
gcloud builds submit --region=us-east4 --config cloud_run/socrata_cloudbuild.yaml --substitutions=_LOCATION="us-east4",_PROJECT_ID="<GCP-PROJECT-ID>",_REPOSITORY="dec",_IMAGE="socrata",_CLOUD_RUN_SERVICE_NAME="<Cloud-run-service-name>",_MEMORY="<Memory>",_COMPOSER_SERVICE_ACCOUNT="<service-account-email-attached-with-cloud-composer-env>"

```