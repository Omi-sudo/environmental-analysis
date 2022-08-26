"""
geo_point_conversion.py module
This module will convert the geo point values to respective
latitude and longitude and insert into table
"""
from pyproj import Transformer
from google.cloud import bigquery
import pandas as pd

# Constants
project_id = "gcp-environmental-analysis"
dataset_id = "ingestion"
table_id = "active_landfills_copy"

# Transform from NAD 83 Zone 18 to EPSG 4326
p = Transformer.from_crs(26918, 4326)

# Construct a BigQuery client object.
client = bigquery.Client()
query = f"""SELECT * FROM `{project_id}.{dataset_id}.{table_id}`"""
query_job = client.query(query)  # Make an API request.
job_config = bigquery.LoadJobConfig()
job_config.write_disposition = "WRITE_TRUNCATE"


table_ref = client.get_table(dataset_id+ "." +table_id)

result = query_job.result()

table_data = list()
for row in result:
    row = dict(row)
    long, lat = p.transform(row["east_coordinate"], row["north_coordinate"])
    row["latitude"] = lat
    row["longitude"] = long
    table_data.append(row)

insert_data = client.load_table_from_dataframe(
  dataframe=pd.DataFrame(table_data), destination=table_ref,job_config=job_config
)

insert_data.result()
print("Latitude and Longitude added successfully for all data")
