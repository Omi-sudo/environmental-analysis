SELECT
  site_code,
  site_name,
  program,
  site_class,
  detail_url,
  area_sqm,
  record_date,
  CAST(ingestion_timestamp AS TIMESTAMP) AS ingestion_timestamp
FROM
  `ingestion.remediation_area`