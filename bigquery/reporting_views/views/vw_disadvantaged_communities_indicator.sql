SELECT
  CAST(geoid AS STRING) AS geoid,
  dac_designation,
  redc,
  county,
  city_town,
  nyc_region,
  urban_rural,
  tribal_designation,
  household_low_count_flag,
  population_count,
  household_count,
  percentile_rank_combined_statewide,
  percentile_rank_combined_nyc,
  percentile_rank_combined_ros,
  combined_score,
  burden_score_percentile,
  vulnerability_score_percentile,
  burden_score,
  vulnerability_score,
  benzene_concentration,
  particulate_matter_25,
  traffic_truck_highways,
  traffic_number_vehicles,
  wastewater_discharge,
  housing_vacancy_rate,
  industrial_land_use,
  landfills,
  oil_storage,
  municipal_waste_combustors,
  power_generation_facilities,
  rmp_sites,
  remediation_sites,
  scrap_metal_processing,
  agricultural_land_use,
  coastal_flooding_storm_risk,
  days_above_90_degrees_2050,
  drive_time_healthcare,
  inland_flooding_risk,
  low_vegetative_cover,
  asian_percent,
  black_african_american_percent,
  redlining_updated,
  latino_percent,
  english_proficiency,
  native_indigenous,
  lmi_80_ami,
  lmi_poverty_federal,
  population_no_college,
  household_single_parent,
  unemployment_rate,
  asthma_ed_rate,
  copd_ed_rate,
  households_disabled,
  low_birth_weight,
  mi_hospitalization_rate,
  health_insurance_rate,
  age_over_65,
  premature_deaths,
  internet_access,
  home_energy_affordability,
  homes_built_before_1960,
  mobile_homes,
  rent_percent_income,
  renter_percent,
  record_date,
  ingestion_timestamp
FROM
  `ingestion.disadvantaged_communities_indicator`