SELECT
  facility_name,
  CAST(decid AS STRING),
  CAST(oris_id AS STRING),
  CAST(ptid AS STRING),
  unit_id,
  source_id,
  nameplate_mw,
  gb_year,
  primary_fuel,
  secondary_fuel,
  generation_gwh_2019,
  record_date,
  ingestion_timestamp
FROM
  `ingestion.power_generation_facilities_unit`