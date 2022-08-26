import static_data_ingestion 

BQ_RAW_INGESTION_MAPPING = {
  "active_landfills": {
    "table_name": "active_landfills",
    "query": f" Insert into `{static_data_ingestion.DEST_PROJECT_ID}.ingestion.active_landfills` "
             f"SELECT * FROM `{static_data_ingestion.SOURCE_PROJECT_ID}.ingestion.active_landfills` "
  },
  "benzene_modeled_concentrations_2017_emissions": {
    "table_name": "benzene_modeled_concentrations_2017_emissions",
    "query": f"Insert into `{static_data_ingestion.DEST_PROJECT_ID}.ingestion.benzene_modeled_concentrations_2017_emissions` "
             f"SELECT * FROM `{static_data_ingestion.SOURCE_PROJECT_ID}.ingestion.benzene_modeled_concentrations_2017_emissions` "
  },
  "diesel_trucks_bus_traffic": {
    "table_name": "diesel_trucks_bus_traffic",
    "query": f"Insert into `{static_data_ingestion.DEST_PROJECT_ID}.ingestion.diesel_trucks_bus_traffic` "
             f"SELECT * FROM `{static_data_ingestion.SOURCE_PROJECT_ID}.ingestion.diesel_trucks_bus_traffic` "
  },
  "disadvantaged_communities_indicator": {
    "table_name": "disadvantaged_communities_indicator",
    "query": f"Insert into `{static_data_ingestion.DEST_PROJECT_ID}.ingestion.disadvantaged_communities_indicator` "
             f"SELECT * FROM `{static_data_ingestion.SOURCE_PROJECT_ID}.ingestion.disadvantaged_communities_indicator` "
  },
  "municipal_waste_combustors": {
    "table_name": "municipal_waste_combustors",
    "query": f"Insert Into `{static_data_ingestion.DEST_PROJECT_ID}.ingestion.municipal_waste_combustors` "
             f"SELECT * FROM `{static_data_ingestion.SOURCE_PROJECT_ID}.ingestion.municipal_waste_combustors` "
  },
  "nys_public_school_k_12": {
    "table_name": "nys_public_school_k_12",
    "query": f"Insert into `{static_data_ingestion.DEST_PROJECT_ID}.ingestion.nys_public_school_k_12` "
             f"SELECT * FROM `{static_data_ingestion.SOURCE_PROJECT_ID}.ingestion.nys_public_school_k_12` "
  },
  "pm_25_2018_modeled_air_concentrations": {
    "table_name": "pm_25_2018_modeled_air_concentrations",
    "query": f"Insert into `{static_data_ingestion.DEST_PROJECT_ID}.ingestion.pm_25_2018_modeled_air_concentrations` "
             f"SELECT * FROM `{static_data_ingestion.SOURCE_PROJECT_ID}.ingestion.pm_25_2018_modeled_air_concentrations` "
  },
  "power_generation_facilities_facility": {
    "table_name": "power_generation_facilities_facility",
    "query": f" Insert into `{static_data_ingestion.DEST_PROJECT_ID}.ingestion.power_generation_facilities_facility` "
             f"SELECT * FROM `{static_data_ingestion.SOURCE_PROJECT_ID}.ingestion.power_generation_facilities_facility` "
  },
  "power_generation_facilities_unit": {
    "table_name": "power_generation_facilities_unit",
    "query": f" Insert into `{static_data_ingestion.DEST_PROJECT_ID}.ingestion.power_generation_facilities_unit` "
                  f"SELECT * FROM `{static_data_ingestion.SOURCE_PROJECT_ID}.ingestion.power_generation_facilities_unit` "
  },
  "remediation_area": {
    "table_name": "remediation_area",
    "query": f"Insert into `{static_data_ingestion.DEST_PROJECT_ID}.ingestion.remediation_area` "
                  f"SELECT * FROM `{static_data_ingestion.SOURCE_PROJECT_ID}.ingestion.remediation_area` "
  },
  "remediation_point": {
    "table_name": "remediation_point",
    "query": f"Insert into `{static_data_ingestion.DEST_PROJECT_ID}.ingestion.remediation_point` "
             f"SELECT * FROM `{static_data_ingestion.SOURCE_PROJECT_ID}.ingestion.remediation_point` "
  },
  "risk_management_plan_facilities": {
    "table_name": "risk_management_plan_facilities",
    "query": f"Insert into `{static_data_ingestion.DEST_PROJECT_ID}.ingestion.risk_management_plan_facilities` "
             f"SELECT * FROM `{static_data_ingestion.SOURCE_PROJECT_ID}.ingestion.risk_management_plan_facilities` "
  },
  "scrap_metal_processing_facilities": {
    "table_name": "scrap_metal_processing_facilities",
    "query": f"Insert into `{static_data_ingestion.DEST_PROJECT_ID}.ingestion.scrap_metal_processing_facilities` "
             f"SELECT * FROM `{static_data_ingestion.SOURCE_PROJECT_ID}.ingestion.scrap_metal_processing_facilities` "
  },
  "vehicle_dismantlers_facilities": {
    "table_name": "vehicle_dismantlers_facilities",
    "query": f"Insert into `{static_data_ingestion.DEST_PROJECT_ID}.ingestion.vehicle_dismantlers_facilities` "
             f"SELECT * FROM `{static_data_ingestion.SOURCE_PROJECT_ID}.ingestion.vehicle_dismantlers_facilities` "
  },
  "vehicle_traffic_density_2019_all_ny": {
    "table_name": "vehicle_traffic_density_2019_all_ny",
    "query": f"Insert into `{static_data_ingestion.DEST_PROJECT_ID}.ingestion.vehicle_traffic_density_2019_all_ny` "
             f"SELECT * FROM `{static_data_ingestion.SOURCE_PROJECT_ID}.ingestion.vehicle_traffic_density_2019_all_ny` "
  },
  "vehicle_traffic_density_2019_nyc": {
    "table_name": "vehicle_traffic_density_2019_nyc",
    "query": f"Insert into `{static_data_ingestion.DEST_PROJECT_ID}.ingestion.vehicle_traffic_density_2019_nyc` "
             f"SELECT * FROM `{static_data_ingestion.SOURCE_PROJECT_ID}.ingestion.vehicle_traffic_density_2019_nyc` "
  },
  "major_oil_storage_facilities": {
    "table_name": "major_oil_storage_facilities",
    "query": f"Insert into `{static_data_ingestion.DEST_PROJECT_ID}.ingestion.major_oil_storage_facilities` "
             f"SELECT * FROM `{static_data_ingestion.SOURCE_PROJECT_ID}.ingestion.major_oil_storage_facilities` "
  }
}

BQ_REPORTING_INGESTION_MAPPING = {
  "active_landfills": {
    "table_name": "active_landfills",
    "query": f"Insert into `{static_data_ingestion.DEST_PROJECT_ID}.reporting.active_landfills` "
             f"SELECT * FROM `{static_data_ingestion.DEST_PROJECT_ID}.reporting_views.vw_active_landfills` "
  },
  "benzene_modeled_concentrations_2017_emissions": {
    "table_name": "benzene_modeled_concentrations_2017_emissions",
    "query": f"Insert into `{static_data_ingestion.DEST_PROJECT_ID}.reporting.benzene_modeled_concentrations_2017_emissions` "
             f"SELECT * FROM `{static_data_ingestion.DEST_PROJECT_ID}.reporting_views"
             f".vw_benzene_modeled_concentrations_2017_emissions` "
  },
  "diesel_trucks_bus_traffic": {
    "table_name": "diesel_trucks_bus_traffic",
    "query": f"Insert into `{static_data_ingestion.DEST_PROJECT_ID}.reporting.diesel_trucks_bus_traffic` "
             f"SELECT * FROM `{static_data_ingestion.DEST_PROJECT_ID}.reporting_views.vw_diesel_trucks_bus_traffic` "
  },
  "disadvantaged_communities_indicator": {
    "table_name": "disadvantaged_communities_indicator",
    "query": f"Insert into `{static_data_ingestion.DEST_PROJECT_ID}.reporting.disadvantaged_communities_indicator` "
             f"SELECT * FROM `{static_data_ingestion.DEST_PROJECT_ID}.reporting_views.vw_disadvantaged_communities_indicator` "
  },
  "municipal_waste_combustors": {
    "table_name": "municipal_waste_combustors",
    "query": f"Insert Into `{static_data_ingestion.DEST_PROJECT_ID}.reporting.municipal_waste_combustors` "
             f"SELECT * FROM `{static_data_ingestion.DEST_PROJECT_ID}.reporting_views.vw_municipal_waste_combustors` "
  },
  "nys_public_school_k_12": {
    "table_name": "nys_public_school_k_12",
    "query": f"Insert into `{static_data_ingestion.DEST_PROJECT_ID}.reporting.nys_public_school_k_12` "
             f"SELECT * FROM `{static_data_ingestion.DEST_PROJECT_ID}.reporting_views.vw_nys_public_school_k_12` "
  },
  "pm_25_2018_modeled_air_concentrations": {
    "table_name": "pm_25_2018_modeled_air_concentrations",
    "query": f"Insert into `{static_data_ingestion.DEST_PROJECT_ID}.reporting.pm_25_2018_modeled_air_concentrations` "
             f"SELECT * FROM `{static_data_ingestion.DEST_PROJECT_ID}.reporting_views.vw_pm_25_2018_modeled_air_concentrations` "
  },
  "power_generation_facilities_facility": {
    "table_name": "power_generation_facilities_facility",
    "query": f" Insert into `{static_data_ingestion.DEST_PROJECT_ID}.reporting.power_generation_facilities_facility` "
             f"SELECT * FROM `{static_data_ingestion.DEST_PROJECT_ID}.reporting_views.vw_power_generation_facilities_facility` "
  },
  "power_generation_facilities_unit": {
    "table_name": "power_generation_facilities_unit",
    "query": f" Insert into `{static_data_ingestion.DEST_PROJECT_ID}.reporting.power_generation_facilities_unit` "
             f"SELECT * FROM `{static_data_ingestion.DEST_PROJECT_ID}.reporting_views.vw_power_generation_facilities_unit` "
  },
  "remediation_area": {
    "table_name": "remediation_area",
    "query": f"Insert into `{static_data_ingestion.DEST_PROJECT_ID}.reporting.remediation_area` "
             f"SELECT * FROM `{static_data_ingestion.DEST_PROJECT_ID}.reporting_views.vw_remediation_area` "
  },
  "remediation_point": {
    "table_name": "remediation_point",
    "query": f"Insert into `{static_data_ingestion.DEST_PROJECT_ID}.reporting.remediation_point` "
             f"SELECT * FROM `{static_data_ingestion.DEST_PROJECT_ID}.reporting_views.vw_remediation_point` "
  },
  "risk_management_plan_facilities": {
    "table_name": "risk_management_plan_facilities",
    "query": f"Insert into `{static_data_ingestion.DEST_PROJECT_ID}.reporting.risk_management_plan_facilities` "
             f"SELECT * FROM `{static_data_ingestion.DEST_PROJECT_ID}.reporting_views.vw_risk_management_plan_facilities` "
  },
  "scrap_metal_processing_facilities": {
    "table_name": "scrap_metal_processing_facilities",
    "query": f"Insert into `{static_data_ingestion.DEST_PROJECT_ID}.reporting.scrap_metal_processing_facilities` "
             f"SELECT * FROM `{static_data_ingestion.DEST_PROJECT_ID}.reporting_views.vw_scrap_metal_processing_facilities` "
  },
  "vehicle_dismantlers_facilities": {
    "table_name": "vehicle_dismantlers_facilities",
    "query": f"Insert into `{static_data_ingestion.DEST_PROJECT_ID}.reporting.vehicle_dismantlers_facilities` "
             f"SELECT * FROM `{static_data_ingestion.DEST_PROJECT_ID}.reporting_views.vw_vehicle_dismantlers_facilities` "
  },
  "vehicle_traffic_density_2019_all_ny": {
    "table_name": "vehicle_traffic_density_2019_all_ny",
    "query": f"Insert into `{static_data_ingestion.DEST_PROJECT_ID}.reporting.vehicle_traffic_density_2019_all_ny` "
             f"SELECT * FROM `{static_data_ingestion.DEST_PROJECT_ID}.reporting_views.vw_vehicle_traffic_density_2019_all_ny` "
  },
  "vehicle_traffic_density_2019_nyc": {
    "table_name": "vehicle_traffic_density_2019_nyc",
    "query": f"Insert into `{static_data_ingestion.DEST_PROJECT_ID}.reporting.vehicle_traffic_density_2019_nyc` "
             f"SELECT * FROM `{static_data_ingestion.DEST_PROJECT_ID}.reporting_views.vw_vehicle_traffic_density_2019_nyc` "
  },
  "major_oil_storage_facilities": {
    "table_name": "major_oil_storage_facilities",
    "query": f"Insert into `{static_data_ingestion.DEST_PROJECT_ID}.reporting.major_oil_storage_facilities` "
             f"SELECT * FROM `{static_data_ingestion.DEST_PROJECT_ID}.reporting_views.vw_major_oil_storage_facilities` "
  }
}

AQS_MAPPING = {
  "aqs_black_carbon_pm2_5_corrected": {
    "table_name": "aqs_black_carbon_pm2_5_corrected",
    "query": f"Insert into `{static_data_ingestion.DEST_PROJECT_ID}.reporting.aqs_black_carbon_pm2_5_corrected` "
             f"SELECT * FROM `{static_data_ingestion.SOURCE_PROJECT_ID}.reporting.aqs_black_carbon_pm2_5_corrected` "
  },
  "aqs_carbon_monoxide": {
    "table_name": "aqs_carbon_monoxide",
    "query": f"Insert into `{static_data_ingestion.DEST_PROJECT_ID}.reporting.aqs_carbon_monoxide` "
             f"SELECT * FROM `{static_data_ingestion.SOURCE_PROJECT_ID}.reporting.aqs_carbon_monoxide` "
  },
  "aqs_ethane": {
    "table_name": "aqs_ethane",
    "query": f"Insert into `{static_data_ingestion.DEST_PROJECT_ID}.reporting.aqs_ethane` "
             f"SELECT * FROM `{static_data_ingestion.SOURCE_PROJECT_ID}.reporting.aqs_ethane` "
  },
  "aqs_formaldehyde": {
    "table_name": "aqs_formaldehyde",
    "query": f"Insert into `{static_data_ingestion.DEST_PROJECT_ID}.reporting.aqs_formaldehyde` "
             f"SELECT * FROM `{static_data_ingestion.SOURCE_PROJECT_ID}.reporting.aqs_formaldehyde` "
  },
  "aqs_nitric_oxide": {
    "table_name": "aqs_nitric_oxide",
    "query": f"Insert into `{static_data_ingestion.DEST_PROJECT_ID}.reporting.aqs_nitric_oxide` "
             f"SELECT * FROM `{static_data_ingestion.SOURCE_PROJECT_ID}.reporting.aqs_nitric_oxide` "
  },
  "aqs_nitrogen_dioxide": {
    "table_name": "aqs_nitrogen_dioxide",
    "query": f"Insert into `{static_data_ingestion.DEST_PROJECT_ID}.reporting.aqs_nitrogen_dioxide` "
             f"SELECT * FROM `{static_data_ingestion.SOURCE_PROJECT_ID}.reporting.aqs_nitrogen_dioxide` "
  },
  "aqs_ozone": {
    "table_name": "aqs_ozone",
    "query": f"Insert into `{static_data_ingestion.DEST_PROJECT_ID}.reporting.aqs_ozone` "
             f"SELECT * FROM `{static_data_ingestion.SOURCE_PROJECT_ID}.reporting.aqs_ozone` "
  },
  "aqs_pm_25": {
    "table_name": "aqs_pm_25",
    "query": f"Insert into `{static_data_ingestion.DEST_PROJECT_ID}.reporting.aqs_pm_25` "
             f"SELECT * FROM `{static_data_ingestion.SOURCE_PROJECT_ID}.reporting.aqs_pm_25` "
  },
  "aqs_sulfur_dioxide": {
    "table_name": "aqs_sulfur_dioxide",
    "query": f"Insert into `{static_data_ingestion.DEST_PROJECT_ID}.reporting.aqs_sulfur_dioxide` "
             f"SELECT * FROM `{static_data_ingestion.SOURCE_PROJECT_ID}.reporting.aqs_sulfur_dioxide` "
  },
  "aqs_toxics_and_carbonyls": {
    "table_name": "aqs_toxics_and_carbonyls",
    "query": f"Insert into `{static_data_ingestion.DEST_PROJECT_ID}.reporting.aqs_toxics_and_carbonyls` "
             f"SELECT * FROM `{static_data_ingestion.SOURCE_PROJECT_ID}.reporting.aqs_toxics_and_carbonyls` "
  },
}