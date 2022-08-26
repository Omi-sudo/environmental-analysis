SELECT
  facility_name AS facility_name,
  location_address AS location_address,
  city AS city,
  state AS state,
  zip_code AS zip_code,
  county AS county,
  activity_desc AS activity_desc,
  activity_number AS activity_number,
  east_coordinate AS east_coordinate,
  north_coordinate AS north_coordinate,
  latitude AS latitude,
  longitude AS longitude,
  ST_GeogPoint(latitude, longitude) AS geometry,
  regulatory_status AS regulatory_status,
  authorization_number AS authorization_number,
  authorization_issue_date AS authorization_issue_date,
  expiration_date AS expiration_date,
  date_of_last_inspection AS date_of_last_inspection,
  record_date AS record_date,
  ingestion_timestamp AS ingestion_timestamp
FROM
  `ingestion.municipal_waste_combustors`