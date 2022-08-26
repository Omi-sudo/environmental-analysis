SELECT
  CAST(objectid AS STRING) AS object_id,
  sitetype AS site_type,
  sitename AS site_name,
  detail_url AS detail_url,
  spdesno AS spdes_no,
  geo_metadata,
  ST_GeogPoint(geo_metadata.x, geo_metadata.y) AS geometry,
  record_date,
  ingestion_timestamp
FROM
  `warehouse.arcgis_major_oil_storage_facilities`