SELECT
  facility_name AS facility_name,
  location_address AS location_address,
  location_address2 AS location_address2,
  city AS city,
  state AS state,
  zip_code AS zip_code,
  county AS county,
  activity_desc AS activity_desc,
  activity_number AS activity_number,
  active AS active,
  east_coordinate AS east_coordinate,
  north_coordinate AS north_coordinate,
  latitude AS latitude,
  longitude AS longitude,
  ST_GeogPoint(latitude, longitude) AS geometry,
  accuracy_code AS accuracy_code,
  waste_types AS waste_types,
  regulatory_status AS regulatory_status,
  authorization_number AS authorization_number,
  record_date AS record_date,
  ingestion_timestamp AS ingestion_timestamp
FROM
  `ingestion.active_landfills`