SELECT
  CAST(id AS STRING) AS id,
  state_name,
  ptraf,
  p_ptraf,
  d_ptraf_2,
  county,
  record_date,
  ingestion_timestamp
FROM
  `ingestion.vehicle_traffic_density_2019_nyc`