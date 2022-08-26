SELECT
  facility_name AS facility_name,
  location_address AS location_address,
  city AS city,
  state AS state,
  zip_code AS zip_code,
  county AS county,
  waste_types AS waste_types,
  activity_desc AS activity_desc,
  activity_number AS activity_number,
  east_coordinate AS east_coordinate,
  north_coordinate AS north_coordinate,
  latitude AS latitude,
  longitude AS longitude,
  ST_GeogPoint(latitude, longitude) AS geometry,
  record_date AS record_date,
  ingestion_timestamp AS ingestion_timestamp
FROM
  `ingestion.vehicle_dismantlers_facilities`