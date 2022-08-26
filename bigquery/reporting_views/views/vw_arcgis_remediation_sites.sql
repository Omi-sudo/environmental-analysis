SELECT
  siteclass AS siteclass,
  gisflag AS gisflag,
  geo_metadata AS geo_metadata,
  ST_GeogPoint(geo_metadata.y,
    geo_metadata.x) AS geometry,
  sitecode AS sitecode,
  objectid AS objectid,
  utmy AS utmy,
  sitename AS sitename,
  doc_url AS doc_url,
  detail_url AS detail_url,
  brown_url AS brown_url,
  record_date AS record_date,
  ingestion_timestamp AS ingestion_timestamp
FROM
  `warehouse.arcgis_remediation_sites`