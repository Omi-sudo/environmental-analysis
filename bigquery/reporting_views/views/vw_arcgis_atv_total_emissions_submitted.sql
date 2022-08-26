SELECT
  objectid,
  site_id AS site_id,
  dec_id AS dec_id,
  facility_name AS facility_name,
  permit_type AS permit_type,
  CAST(statement_year AS INT64) AS statement_year,
  cas_num AS cas_num,
  contaminant AS contaminant,
  chemical_family AS chemical_family,
  amount_lbs_per_yr AS amount_lbs_per_yr,
  nytmn_coordinate AS nytmn_coordinate,
  nytme_coordinate AS nytme_coordinate,
  longitude AS longitude,
  latitude AS latitude,
  ST_GeogPoint(longitude,
    latitude) AS geometry,
  record_date AS record_date,
  ingestion_timestamp AS ingestion_timestamp
FROM
  `warehouse.arcgis_atv_total_emissions_submitted`