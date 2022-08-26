SELECT
  bbl,
  bin,
  city,
  housenum,
  name,
  streetname,
  geo_metadata AS geo_metadata,
  ST_GeogPoint(geo_metadata.coordinates.x[
  OFFSET
    (0)],
    geo_metadata.coordinates.y[
  OFFSET
    (0)]) AS geometry,
  url,
  zip,
  record_date,
  ingestion_timestamp
FROM
  `warehouse.socrata_day_care_center`