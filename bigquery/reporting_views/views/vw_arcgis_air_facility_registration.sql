SELECT
  objectid,
  site_id as site_id,
  dec_id as dec_id,
  facility as facility,
  permit_type as permit_type,
  cas_num as cas_num,
  contaminant as contaminant,
  amount_lbs_per_year as amount_lbs_per_year,
  nytmn_coordinate as nytmn_coordinate,
  nytme_coordinate as nytme_coordinate,
  longitude as longitude,
  latitude as latitude,
  ST_GeogPoint(longitude,
    latitude) AS geometry,
  record_date as record_date,
  ingestion_timestamp as ingestion_timestamp
FROM
  `warehouse.arcgis_air_facility_registration`