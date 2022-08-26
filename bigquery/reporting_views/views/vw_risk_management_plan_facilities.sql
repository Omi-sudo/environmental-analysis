SELECT
  CAST(census_tract AS STRING) AS census_tract,
  state,
  rmp_facility_proximity,
  percentile_for_rmp_facility_proximity,
  ej_index_for_rmp_facility_proximity,
  record_date,
  ingestion_timestamp
FROM
  `ingestion.risk_management_plan_facilities`