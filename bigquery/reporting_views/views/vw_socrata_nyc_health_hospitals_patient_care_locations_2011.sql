SELECT
  borough,
  computed_region_92fq_4b7q,
  computed_region_efsh_h5xi,
  computed_region_f5dn_yrer,
  computed_region_sbqj_enih,
  computed_region_yeji_bk3q,
  facility_name,
  facility_type,
  STRUCT(STRUCT(geo_metadata.human_address.address AS address,
      geo_metadata.human_address.city AS city,
      geo_metadata.human_address.state AS state,
      geo_metadata.human_address.zip AS zip) AS human_address,
    CAST(geo_metadata.longitude AS FLOAT64) AS longitude,
    CAST( geo_metadata.latitude AS FLOAT64) AS latitude) AS geo_metadata,
  ST_GeogPoint(CAST(
    IF
      (geo_metadata.longitude IS NOT NULL,
        geo_metadata.longitude,
        longitude) AS FLOAT64),
    CAST(
    IF
      (geo_metadata.latitude IS NOT NULL,
        geo_metadata.latitude,
        latitude) AS FLOAT64)) AS geometry,
  phone,
  bbl,
  bin,
  census_tract,
  community_board,
  council_district,
  cross_streets,
  CAST(latitude AS FLOAT64) AS latitude,
  CAST(longitude AS FLOAT64) AS longitude,
  nta,
  postcode,
  record_date,
  ingestion_timestamp
FROM
  `warehouse.socrata_nyc_health_hospitals_patient_care_locations_2011`