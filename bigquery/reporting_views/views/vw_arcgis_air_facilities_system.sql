SELECT
  objectid,
  site_id AS site_id,
  dec_id AS dec_id,
  facility AS facility,
  permit_type AS permit_type,
  cas_number AS cas_number,
  contaminant AS contaminant,
  amount_lbs_per_year AS amount_lbs_per_year,
  nytmn_coordinate AS nytmn_coordinate,
  nytme_coordinate AS nytme_coordinate,
  longitude AS longitude,
  latitude AS latitude,
  ST_GeogPoint(longitude,
    latitude) AS geometry,
  record_date AS record_date,
  ingestion_timestamp AS ingestion_timestamp
FROM
  `warehouse.arcgis_air_facilities_system`