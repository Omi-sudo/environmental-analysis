# Cloud run code to transfer FTP data from GCS bucket to BigQuery.

## Prerequisites
- Service Account for Cloud Run: </br>
  - Cloud Run uses the same service account use by Cloud Composer, for detailed permission please refer TDD.

##GCS file path<br>

Files from FTP server will be stored in respective bucket having path [BUCKET_NAME]/.

## Overview

As soon as the cloud run for ftp will trigger, it will fetch list of files from provided ftp bucket (Files will be picked from above mention bucket path) and start ingesting the data to BigQuery one by one.Also the audit logs will be saved in job audit table.
If any error occur in data from file it will skip that file and reason for failure updated with job_audit_table.<br>**Note**: Cloud run will process maximum 40 files per run. 

## Code Structure

### Folder cloud run/ftp

1. main.py - Python file which is the entry point of the program execution. 
   - Endpoint "/gcs_to_bq" : It will read the files from the GCS bucket and insert into respective table in BigQuery. 
2. requirements.txt - File containing package with version number.
3. Dockerfile - A text file with instructions to build the image. 
4. .dockerignore - File that allows to mention a list of files and/or directories which we might want to ignore while building the image.

## Below are the utility files used from cloud run-->

1. bq_utils.py - A utility module to connect, read and insert data to BigQuery.
2. storage_util.py - A utility module to connect and insert in GCS.
3. job_audit_utils.py - A utility module to insert job audit logs into the BigQuery.
4. constant.py -  File containing constants variables.


## Create the service using gcloud command

To create the cloud run service from local system, Navigate to the environmental analysis directory and execute the below command. 
<br>Note: 
Please mention respective Project ID in below command.

```
gcloud builds submit --region=us-east4 --config cloud_run/ftp_cloudbuild.yaml --substitutions=_LOCATION="us-east4",_PROJECT_ID="<PROJECT_ID>",_REPOSITORY="dec",_IMAGE="ftp",_CLOUD_RUN_SERVICE_NAME="ftp???,_COMPOSER_SERVICE_ACCOUNT="dec-cloudrun-dev@gcp-environmental-analysis.iam.gserviceaccount.com???

```
