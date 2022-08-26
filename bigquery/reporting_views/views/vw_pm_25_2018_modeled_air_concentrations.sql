SELECT
  CAST(census_tract AS STRING) AS census_tract,
  state,
  particulate_matter_2_5__microgram_per_cubic_meter,
  percentile_for_particulate_matter_2_5,
  ej_index_for_particulate_matter_2_5,
  record_date,
  ingestion_timestamp
FROM
  `ingestion.pm_25_2018_modeled_air_concentrations`