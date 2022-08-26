SELECT
  facility_name as facility_name,
  location_address as location_address,
  city as city,
  state as state,
  zip_code as zip_code,
  county as county,
  waste_types as waste_types,
  activity_desc as activity_desc ,
  activity_number as activity_number,
  east_coordinate as east_coordinate,
  north_coordinate as north_coordinate,
  latitude as latitude,
  longitude as longitude,
  ST_GeogPoint(latitude,longitude) AS geometry,
  record_date as record_date,
  ingestion_timestamp as ingestion_timestamp
FROM
  `ingestion.scrap_metal_processing_facilities`