SELECT
  shape__length AS shape_length,
  shape__area AS shape_area,
  gisflag AS gisflag,
  program AS program,
  geo_metadata AS geo_metadata,
  ST_GEOGFROMTEXT(geo_metadata, make_valid => true) as geometry,
  sitecode AS sitecode,
  objectid AS objectid,
  siteclass AS siteclass,
  sitename AS sitename,
  detail_url AS detail_url,
  record_date AS record_date,
  ingestion_timestamp AS ingestion_timestamp
FROM
  `warehouse.arcgis_remediation_boundaries`