variable "project_id" {
  type      = string
}

variable "dataset_location" {
  type        = string
  description = "BigQuery Dataset location"
  default     = "us-east4"
}

variable "ingestion" {
  type        = string
  default     = "ingestion"
}

variable "ingestion_arcgis" {
  type        = string
  default     = "ingestion_arcgis"
}

variable "ingestion_socrata" {
  type        = string
  default     = "ingestion_socrata"
}

variable "ingestion_aqs" {
  type        = string
  default     = "ingestion_aqs"
}

variable "ingestion_ftp" {
  type        = string
  default     = "ingestion_ftp"
}

variable "warehouse" {
  type        = string
  default     = "warehouse"
}

variable "reporting" {
  type        = string
  default     = "reporting"
}

variable "reporting_views" {
  type        = string
  default     = "reporting_views"
}

variable "job_metadata" {
  type        = string
  default     = "job_metadata"
}

variable "composer_sa" {
  type        = string
}

variable "cloudbuild_sa" {
  type        = string
}

variable "group_email" {
  type        = string
}

variable "reporting_tables" {
  description = "Table definitions. Options and partitioning default to null. Partitioning can only use `range` or `time`, set the unused one to null."
  type = map(object({
    friendly_name = string
    description   = string
    options = object({
      clustering      = list(string)
      encryption_key  = string
      expiration_time = number
    })
    partitioning  = object({
      field = string
      range = object({
        end      = number
        interval = number
        start    = number
      })
      time  = object({
        expiration_ms = number
        type          = string
      })
    })
    schema        = string
  }))

  default = {
    "active_landfills" = {
      friendly_name = "active_landfills"
      description   = "Active landfills operating as of 6/23/2021. Includes the following types: construction & demolition debris, municipal solid waste, ones located on Long Island, and industrial solid waste."
      options       = null
      partitioning  = {
        field = "ingestion_timestamp"
        range = null # use start/end/interval for range
        time  = { type = "DAY", expiration_ms = null }
      }
      schema        = "../../../bigquery/reporting/schemas/active_landfills.json"
    }
    "aqs_black_carbon_pm2_5_corrected" = {
      friendly_name = "aqs_black_carbon_pm2_5_corrected"
      description   = ""
      options       = null
      partitioning  = {
        field = "ingestion_timestamp"
        range = null # use start/end/interval for range
        time  = { type = "DAY", expiration_ms = null }
      }
      schema        = "../../../bigquery/reporting/schemas/aqs_black_carbon_pm2_5_corrected.json"
    }
    "aqs_carbon_monoxide" = {
      friendly_name = "aqs_carbon_monoxide"
      description   = ""
      options       = null
      partitioning  = {
        field = "ingestion_timestamp"
        range = null # use start/end/interval for range
        time  = { type = "DAY", expiration_ms = null }
      }
      schema        = "../../../bigquery/reporting/schemas/aqs_carbon_monoxide.json"
    }
    "aqs_ethane" = {
      friendly_name = "aqs_ethane"
      description   = ""
      options       = null
      partitioning  = {
        field = "ingestion_timestamp"
        range = null # use start/end/interval for range
        time  = { type = "DAY", expiration_ms = null }
      }
      schema        = "../../../bigquery/reporting/schemas/aqs_ethane.json"
    }
    "aqs_formaldehyde" = {
      friendly_name = "aqs_formaldehyde"
      description   = ""
      options       = null
      partitioning  = {
        field = "ingestion_timestamp"
        range = null # use start/end/interval for range
        time  = { type = "DAY", expiration_ms = null }
      }
      schema        = "../../../bigquery/reporting/schemas/aqs_formaldehyde.json"
    }
    "aqs_nitric_oxide" = {
      friendly_name = "aqs_nitric_oxide"
      description   = ""
      options       = null
      partitioning  = {
        field = "ingestion_timestamp"
        range = null # use start/end/interval for range
        time  = { type = "DAY", expiration_ms = null }
      }
      schema        = "../../../bigquery/reporting/schemas/aqs_nitric_oxide.json"
    }
    "aqs_nitrogen_dioxide" = {
      friendly_name = "aqs_nitrogen_dioxide"
      description   = ""
      options       = null
      partitioning  = {
        field = "ingestion_timestamp"
        range = null # use start/end/interval for range
        time  = { type = "DAY", expiration_ms = null }
      }
      schema        = "../../../bigquery/reporting/schemas/aqs_nitrogen_dioxide.json"
    }
    "aqs_ozone" = {
      friendly_name = "aqs_ozone"
      description   = ""
      options       = null
      partitioning  = {
        field = "ingestion_timestamp"
        range = null # use start/end/interval for range
        time  = { type = "DAY", expiration_ms = null }
      }
      schema        = "../../../bigquery/reporting/schemas/aqs_ozone.json"
    }
    "aqs_pm_25" = {
      friendly_name = "aqs_pm_25"
      description   = ""
      options       = null
      partitioning  = {
        field = "ingestion_timestamp"
        range = null # use start/end/interval for range
        time  = { type = "DAY", expiration_ms = null }
      }
      schema        = "../../../bigquery/reporting/schemas/aqs_pm_25.json"
    }
    "aqs_sulfur_dioxide" = {
      friendly_name = "aqs_sulfur_dioxide"
      description   = ""
      options       = null
      partitioning  = {
        field = "ingestion_timestamp"
        range = null # use start/end/interval for range
        time  = { type = "DAY", expiration_ms = null }
      }
      schema        = "../../../bigquery/reporting/schemas/aqs_sulfur_dioxide.json"
    }
    "aqs_toxics_and_carbonyls" = {
      friendly_name = "aqs_toxics_and_carbonyls"
      description   = ""
      options       = null
      partitioning  = {
        field = "ingestion_timestamp"
        range = null # use start/end/interval for range
        time  = { type = "DAY", expiration_ms = null }
      }
      schema        = "../../../bigquery/reporting/schemas/aqs_toxics_and_carbonyls.json"
    }
    "arcgis_air_facilities_system" = {
      friendly_name = "arcgis_air_facilities_system"
      description   = ""
      options       = null
      partitioning  = {
        field = "ingestion_timestamp"
        range = null # use start/end/interval for range
        time  = { type = "DAY", expiration_ms = null }
      }
      schema        = "../../../bigquery/reporting/schemas/arcgis_air_facilities_system.json"
    }
    "arcgis_air_facility_registration" = {
      friendly_name = "arcgis_air_facility_registration"
      description   = ""
      options       = null
      partitioning  = {
        field = "ingestion_timestamp"
        range = null # use start/end/interval for range
        time  = { type = "DAY", expiration_ms = null }
      }
      schema        = "../../../bigquery/reporting/schemas/arcgis_air_facility_registration.json"
    }
    "arcgis_atv_total_emissions_submitted" = {
      friendly_name = "arcgis_atv_total_emissions_submitted"
      description   = ""
      options       = null
      partitioning  = {
        field = "ingestion_timestamp"
        range = null # use start/end/interval for range
        time  = { type = "DAY", expiration_ms = null }
      }
      schema        = "../../../bigquery/reporting/schemas/arcgis_atv_total_emissions_submitted.json"
    }
    "arcgis_major_oil_storage_facilities" = {
      friendly_name = "arcgis_major_oil_storage_facilities"
      description   = "MOSF program applies to facilities that store 400,000 gallons or more of petroleum products in aboveground and underground storage tanks. These types of facilities process large quantities of petroleum products which can result in air releases of large quantities of volatile organic compounds some of which are hazardous air pollutants (e.g., benzene, toluene, and xylene). Additional community burdens include noise and emissions from truck traffic, rail, and marine transport. Many MOSF are in Ports which are often in proximity to environmental justice communities."
      options       = null
      partitioning  = {
        field = "ingestion_timestamp"
        range = null # use start/end/interval for range
        time  = { type = "DAY", expiration_ms = null }
      }
      schema        = "../../../bigquery/reporting/schemas/arcgis_major_oil_storage_facilities.json"
    }
    "arcgis_nursing_homes" = {
      friendly_name = "arcgis_nursing_homes"
      description   = "This feature class/shapefile contains nursing and assisted care facilities for the Homeland Infrastructure Foundation-Level Data (HIFLD) database."
      options       = null
      partitioning  = {
        field = "ingestion_timestamp"
        range = null # use start/end/interval for range
        time  = { type = "DAY", expiration_ms = null }
      }
      schema        = "../../../bigquery/reporting/schemas/arcgis_nursing_homes.json"
    }
    "arcgis_remediation_boundaries" = {
      friendly_name = "arcgis_remediation_boundaries"
      description   = ""
      options       = null
      partitioning  = {
        field = "ingestion_timestamp"
        range = null # use start/end/interval for range
        time  = { type = "DAY", expiration_ms = null }
      }
      schema        = "../../../bigquery/reporting/schemas/arcgis_remediation_boundaries.json"
    }
    "arcgis_remediation_sites" = {
      friendly_name = "arcgis_remediation_sites"
      description   = "NYSDEC’s database on the State’s Brownfield Cleanup program and Class II, and federal environmental remediation sites (USEPA National Priority List) sites as of July 26, 2010."
      options       = null
      partitioning  = {
        field = "ingestion_timestamp"
        range = null # use start/end/interval for range
        time  = { type = "DAY", expiration_ms = null }
      }
      schema        = "../../../bigquery/reporting/schemas/arcgis_remediation_sites.json"
    }
    "benzene_modeled_concentrations_2017_emissions" = {
      friendly_name = "benzene_modeled_concentrations_2017_emissions"
      description   = "USEPA modeled results from 2017 National Emissions Inventory. Comprehensive assessment of all sources - point, area, mobile, biogenic, fires, secondary formation, background concentration - across the US. 2014 version used for DAC layer."
      options       = null
      partitioning  = {
        field = "ingestion_timestamp"
        range = null # use start/end/interval for range
        time  = { type = "DAY", expiration_ms = null }
      }
      schema        = "../../../bigquery/reporting/schemas/benzene_modeled_concentrations_2017_emissions.json"
    }
    "diesel_trucks_bus_traffic" = {
      friendly_name = "diesel_trucks_bus_traffic"
      description   = "NYS Roadway Inventory System NYSDOT Traffic Viewer, annual average daily traffic counts for 2019 using Federal Highway Administration vehicle classes 4-13. A buffer of 150-meters was generated around each census tract (US Census, 2019) to estimate the extent of diesel emissions. The buffers were overlaid with the NYSDOT roads and counts of diesel vehicles was length-weighted to the portion of road segments located within the buffer. Within each tract’s buffer, the total of the length-weighted annual average daily diesel vehicle count was divided by the total length of all roads in the buffer."
      options       = null
      partitioning  = {
        field = "ingestion_timestamp"
        range = null # use start/end/interval for range
        time  = { type = "DAY", expiration_ms = null }
      }
      schema        = "../../../bigquery/reporting/schemas/diesel_trucks_bus_traffic.json"
    }
    "disadvantaged_communities_indicator" = {
      friendly_name = "disadvantaged_communities_indicator"
      description   = "The Climate Leadership and Community Protection Act (CLCPA) directs the Climate Justice Working Group (CJWG) to establish criteria for defining disadvantaged communities. This dataset identifies areas throughout the State that meet the draft disadvantaged community definition as voted on by the Climate Justice Working Group. The draft Disadvantaged Community definition shown here will undergo 120 days of public input process and pending potential changes by the CJWG, will require a vote by the CJWG to finalize the definition."
      options       = null
      partitioning  = {
        field = "ingestion_timestamp"
        range = null # use start/end/interval for range
        time  = { type = "DAY", expiration_ms = null }
      }
      schema        = "../../../bigquery/reporting/schemas/disadvantaged_communities_indicator.json"
    }
    "municipal_waste_combustors" = {
      friendly_name = "municipal_waste_combustors"
      description   = "Active municipal waste combustors operating as of 6/23/21."
      options       = null
      partitioning  = {
        field = "ingestion_timestamp"
        range = null # use start/end/interval for range
        time  = { type = "DAY", expiration_ms = null }
      }
      schema        = "../../../bigquery/reporting/schemas/municipal_waste_combustors.json"
    }
    "major_oil_storage_facilities" = {
      friendly_name = "major_oil_storage_facilities.json"
      description   = "MOSF program applies to facilities that store 400,000 gallons or more of petroleum products in aboveground and underground storage tanks. These types of facilities process large quantities of petroleum products which can result in air releases of large quantities of volatile organic compounds some of which are hazardous air pollutants (e.g., benzene, toluene, and xylene). Additional community burdens include noise and emissions from truck traffic, rail, and marine transport. Many MOSF are in Ports which are often in proximity to environmental justice communities."
      options       = null
      partitioning  = {
        field = "ingestion_timestamp"
        range = null # use start/end/interval for range
        time  = { type = "DAY", expiration_ms = null }
      }
      schema        = "../../../bigquery/reporting/schemas/major_oil_storage_facilities.json"
    }
    "nys_public_school_k_12" = {
      friendly_name = "nys_public_school_k_12"
      description   = "Shape files for Public Schools K-12, Revised 10/2017."
      options       = null
      partitioning  = {
        field = "ingestion_timestamp"
        range = null # use start/end/interval for range
        time  = { type = "DAY", expiration_ms = null }
      }
      schema        = "../../../bigquery/reporting/schemas/nys_public_school_k_12.json"
    }
    "pm_25_2018_modeled_air_concentrations" = {
      friendly_name = "pm_25_2018_modeled_air_concentrations"
      description   = "Estimated census-tract level PM2.5 ambient annual average concentrations using a Bayesian space-time downscaling fusion model. Estimates are based on 2018 emissions. If using the most recent data available,  currenty it's 2021 EJ screen data the check here to see what year each data layer represents or is based on https://www.epa.gov/ejscreen/overview-environmental-indicators-ejscreen."
      options       = null
      partitioning  = {
        field = "ingestion_timestamp"
        range = null # use start/end/interval for range
        time  = { type = "DAY", expiration_ms = null }
      }
      schema        = "../../../bigquery/reporting/schemas/pm_25_2018_modeled_air_concentrations.json"
    }
    "power_generation_facilities_facility" = {
      friendly_name = "power_generation_facilities_facility"
      description   = "Fossil-fuel power generation facilities from NYSDEC’s 2019 emissions inventory (NYSDEC 2019)."
      options       = null
      partitioning  = {
        field = "ingestion_timestamp"
        range = null # use start/end/interval for range
        time  = { type = "DAY", expiration_ms = null }
      }
      schema        = "../../../bigquery/reporting/schemas/power_generation_facilities_facility.json"
    }
    "power_generation_facilities_unit" = {
      friendly_name = "power_generation_facilities_unit"
      description   = ""
      options       = null
      partitioning  = {
        field = "ingestion_timestamp"
        range = null # use start/end/interval for range
        time  = { type = "DAY", expiration_ms = null }
      }
      schema        = "../../../bigquery/reporting/schemas/power_generation_facilities_unit.json"
    }
    "remediation_area" = {
      friendly_name = "remediation_area"
      description   = ""
      options       = null
      partitioning  = {
        field = "ingestion_timestamp"
        range = null # use start/end/interval for range
        time  = { type = "DAY", expiration_ms = null }
      }
      schema        = "../../../bigquery/reporting/schemas/remediation_area.json"
    }
    "remediation_point" = {
      friendly_name = "remediation_point"
      description   = ""
      options       = null
      partitioning  = {
        field = "ingestion_timestamp"
        range = null # use start/end/interval for range
        time  = { type = "DAY", expiration_ms = null }
      }
      schema        = "../../../bigquery/reporting/schemas/remediation_point.json"
    }
    "risk_management_plan_facilities" = {
      friendly_name = "risk_management_plan_facilities"
      description   = "Count of Risk Management Plan (RMP - potential chemical accident management plan) facilities within 5 km (or nearest one beyond 5 km), of each census tract divided by distance in kilometers based on data from 2021."
      options       = null
      partitioning  = {
        field = "ingestion_timestamp"
        range = null # use start/end/interval for range
        time  = { type = "DAY", expiration_ms = null }
      }
      schema        = "../../../bigquery/reporting/schemas/risk_management_plan_facilities.json"
    }
    "scrap_metal_processing_facilities" = {
      friendly_name = "scrap_metal_processing_facilities"
      description   = "Scrap metal processor means a facility engaged primarily in the purchase, processing and shipment of ferrous and/or non-ferrous scrap (including decommissioned vehicles), the end product of which is the production of raw material for remelting purposes for steel mills, foundries, smelters, refiners, and similar users. Vehicle dismantling facility means a facility that decommissions, dismantles, and recycles end of life vehicles."
      options       = null
      partitioning  = {
        field = "ingestion_timestamp"
        range = null # use start/end/interval for range
        time  = { type = "DAY", expiration_ms = null }
      }
      schema        = "../../../bigquery/reporting/schemas/scrap_metal_processing_facilities.json"
    }
    "socrata_adult_care_facility_map" = {
      friendly_name = "socrata_adult_care_facility_map"
      description   = "Map with exportable data."
      options       = null
      partitioning  = {
        field = "ingestion_timestamp"
        range = null # use start/end/interval for range
        time  = { type = "DAY", expiration_ms = null }
      }
      schema        = "../../../bigquery/reporting/schemas/socrata_adult_care_facility_map.json"
    }
    "socrata_archived_parks_properties" = {
      friendly_name = "socrata_archived_parks_properties"
      description   = "This data identifies City property under the jurisdiction of NYC Parks, which may be managed partially or solely by the Agency."
      options       = null
      partitioning  = {
        field = "ingestion_timestamp"
        range = null # use start/end/interval for range
        time  = { type = "DAY", expiration_ms = null }
      }
      schema        = "../../../bigquery/reporting/schemas/socrata_archived_parks_properties.json"
    }
    "socrata_athletic_facilities" = {
      friendly_name = "socrata_athletic_facilities"
      description   = ""
      options       = null
      partitioning  = {
        field = "ingestion_timestamp"
        range = null # use start/end/interval for range
        time  = { type = "DAY", expiration_ms = null }
      }
      schema        = "../../../bigquery/reporting/schemas/socrata_athletic_facilities.json"
    }
    "socrata_child_care_regulated_programs" = {
      friendly_name = "socrata_child_care_regulated_programs"
      description   = ""
      options       = null
      partitioning  = {
        field = "ingestion_timestamp"
        range = null # use start/end/interval for range
        time  = { type = "DAY", expiration_ms = null }
      }
      schema        = "../../../bigquery/reporting/schemas/socrata_child_care_regulated_programs.json"
    }
    "socrata_day_care_center" = {
      friendly_name = "socrata_day_care_center"
      description   = "Information on OCFS regulated child care programs; file was filtered for licensed daycare centers (DCC)."
      options       = null
      partitioning  = {
        field = "ingestion_timestamp"
        range = null # use start/end/interval for range
        time  = { type = "DAY", expiration_ms = null }
      }
      schema        = "../../../bigquery/reporting/schemas/socrata_day_care_center.json"
    }
    "socrata_health_facility_general_information" = {
      friendly_name = "socrata_health_facility_general_information"
      description   = "File was filtered for hospitals only."
      options       = null
      partitioning  = {
        field = "ingestion_timestamp"
        range = null # use start/end/interval for range
        time  = { type = "DAY", expiration_ms = null }
      }
      schema        = "../../../bigquery/reporting/schemas/socrata_health_facility_general_information.json"
    }
    "socrata_health_facility_map" = {
      friendly_name = "socrata_health_facility_map"
      description   = "Map with exportable data."
      options       = null
      partitioning  = {
        field = "ingestion_timestamp"
        range = null # use start/end/interval for range
        time  = { type = "DAY", expiration_ms = null }
      }
      schema        = "../../../bigquery/reporting/schemas/socrata_health_facility_map.json"
    }
    "socrata_nyc_health_hospitals_patient_care_locations_2011" = {
      friendly_name = "socrata_nyc_health_hospitals_patient_care_locations_2011"
      description   = ""
      options       = null
      partitioning  = {
        field = "ingestion_timestamp"
        range = null # use start/end/interval for range
        time  = { type = "DAY", expiration_ms = null }
      }
      schema        = "../../../bigquery/reporting/schemas/socrata_nyc_health_hospitals_patient_care_locations_2011.json"
    }
    "vehicle_dismantlers_facilities" = {
      friendly_name = "vehicle_dismantlers_facilities"
      description   = ""
      options       = null
      partitioning  = {
        field = "ingestion_timestamp"
        range = null # use start/end/interval for range
        time  = { type = "DAY", expiration_ms = null }
      }
      schema        = "../../../bigquery/reporting/schemas/vehicle_dismantlers_facilities.json"
    }
    "vehicle_traffic_density_2019_all_ny" = {
      friendly_name = "vehicle_traffic_density_2019_all_ny"
      description   = "Vehicle counts (average annual daily traffic) for 2019 at major roads (i.e., all interstate, principal arterials, and other collector highways in the national highway system) within 500 meters of a census block centroid, are divided by distance of the census block centroid in meters to the road. The results are population-weighted average to the census block group level (weighted by 2015-2019 ACS population). Since block group-level EJSCREEN data were obtained, they were aggregated to the tract-level by taking a weighted average of the block group observations, weighted by the proportion of the census tract population that was in the block group. If using the most recent data available, currenty it's 2021 EJ screen data the check here to see what year each data layer represents or is based on https://www.epa.gov/ejscreen/overview-environmental-indicators-ejscreen. "
      options       = null
      partitioning  = {
        field = "ingestion_timestamp"
        range = null # use start/end/interval for range
        time  = { type = "DAY", expiration_ms = null }
      }
      schema        = "../../../bigquery/reporting/schemas/vehicle_traffic_density_2019_all_ny.json"
    }
    "vehicle_traffic_density_2019_nyc" = {
      friendly_name = "vehicle_traffic_density_2019_nyc"
      description   = "Vehicle counts (average annual daily traffic) for 2019 at major roads (i.e., all interstate, principal arterials, and other collector highways in the national highway system) within 500 meters of a census block centroid, are divided by distance of the census block centroid in meters to the road. The results are population-weighted average to the census block group level (weighted by 2015-2019 ACS population). Since block group-level EJSCREEN data were obtained, they were aggregated to the tract-level by taking a weighted average of the block group observations, weighted by the proportion of the census tract population that was in the block group. If using the most recent data available, currenty it's 2021 EJ screen data the check here to see what year each data layer represents or is based on https://www.epa.gov/ejscreen/overview-environmental-indicators-ejscreen. "
      options       = null
      partitioning  = {
        field = "ingestion_timestamp"
        range = null # use start/end/interval for range
        time  = { type = "DAY", expiration_ms = null }
      }
      schema        = "../../../bigquery/reporting/schemas/vehicle_traffic_density_2019_nyc.json"
    }
    "ftp_airnow_i" = {
      friendly_name = "ftp_airnow_i"
      description   = "As part of the AirNow-International (AirNow-I) project, Sonoma Technology, Inc. (STI) developed a simple, compact data exchange format to transfer data between AirNow-I and other data management systems (DMS)."
      options       = null
      partitioning  = {
        field = "record_date"
        range = null # use start/end/interval for range
        time  = { type = "DAY", expiration_ms = null }
      }
      schema        = "../../../bigquery/reporting/schemas/ftp_airnow_i.json"
    }
  }
}

variable "reporting_vw" {
  description = "View definitions."
  type = map(object({
    friendly_name  = string
    query          = string
    use_legacy_sql = bool
  }))
  default = {
    "vw_active_landfills" = {
      friendly_name  = "vw_active_landfills"
      query          = "../../../bigquery/reporting_views/views/vw_active_landfills.sql"
      use_legacy_sql = false
    }
    "vw_arcgis_air_facilities_system" = {
      friendly_name  = "vw_arcgis_air_facilities_system"
      query          = "../../../bigquery/reporting_views/views/vw_arcgis_air_facilities_system.sql"
      use_legacy_sql = false
    }
    "vw_arcgis_air_facility_registration" = {
      friendly_name  = "vw_arcgis_air_facility_registration"
      query          = "../../../bigquery/reporting_views/views/vw_arcgis_air_facility_registration.sql"
      use_legacy_sql = false
    }
    "vw_arcgis_atv_total_emissions_submitted" = {
      friendly_name  = "vw_arcgis_atv_total_emissions_submitted"
      query          = "../../../bigquery/reporting_views/views/vw_arcgis_atv_total_emissions_submitted.sql"
      use_legacy_sql = false
    }
    "vw_arcgis_nursing_homes" = {
      friendly_name  = "vw_arcgis_nursing_homes"
      query          = "../../../bigquery/reporting_views/views/vw_arcgis_nursing_homes.sql"
      use_legacy_sql = false
    }
    "vw_arcgis_remediation_boundaries" = {
      friendly_name  = "vw_arcgis_remediation_boundaries"
      query          = "../../../bigquery/reporting_views/views/vw_arcgis_remediation_boundaries.sql"
      use_legacy_sql = false
    }
    "vw_arcgis_remediation_sites" = {
      friendly_name  = "vw_arcgis_remediation_sites"
      query          = "../../../bigquery/reporting_views/views/vw_arcgis_remediation_sites.sql"
      use_legacy_sql = false
    }
    "vw_arcgis_major_oil_storage_facilities" = {
      friendly_name  = "vw_argis_major_oil_storage_facilities"
      query          = "../../../bigquery/reporting_views/views/vw_arcgis_major_oil_storage_facilities.sql"
      use_legacy_sql = false
    }
    "vw_benzene_modeled_concentrations_2017_emissions" = {
      friendly_name  = "vw_benzene_modeled_concentrations_2017_emissions"
      query          = "../../../bigquery/reporting_views/views/vw_benzene_modeled_concentrations_2017_emissions.sql"
      use_legacy_sql = false
    }
    "vw_diesel_trucks_bus_traffic" = {
      friendly_name  = "vw_diesel_trucks_bus_traffic"
      query          = "../../../bigquery/reporting_views/views/vw_diesel_trucks_bus_traffic.sql"
      use_legacy_sql = false
    }
    "vw_disadvantaged_communities_indicator" = {
      friendly_name  = "vw_disadvantaged_communities_indicator"
      query          = "../../../bigquery/reporting_views/views/vw_disadvantaged_communities_indicator.sql"
      use_legacy_sql = false
    }
    "vw_municipal_waste_combustors" = {
      friendly_name  = "vw_municipal_waste_combustors"
      query          = "../../../bigquery/reporting_views/views/vw_municipal_waste_combustors.sql"
      use_legacy_sql = false
    }
    "vw_nys_public_school_k_12" = {
      friendly_name  = "vw_nys_public_school_k_12"
      query          = "../../../bigquery/reporting_views/views/vw_nys_public_school_k_12.sql"
      use_legacy_sql = false
    }
    "vw_pm_25_2018_modeled_air_concentrations" = {
      friendly_name  = "vw_pm_25_2018_modeled_air_concentrations"
      query          = "../../../bigquery/reporting_views/views/vw_pm_25_2018_modeled_air_concentrations.sql"
      use_legacy_sql = false
    }
    "vw_power_generation_facilities_facility" = {
      friendly_name  = "vw_power_generation_facilities_facility"
      query          = "../../../bigquery/reporting_views/views/vw_power_generation_facilities_facility.sql"
      use_legacy_sql = false
    }
    "vw_power_generation_facilities_unit" = {
      friendly_name  = "vw_power_generation_facilities_unit"
      query          = "../../../bigquery/reporting_views/views/vw_power_generation_facilities_unit.sql"
      use_legacy_sql = false
    }
    "vw_remediation_area" = {
      friendly_name  = "vw_remediation_area"
      query          = "../../../bigquery/reporting_views/views/vw_remediation_area.sql"
      use_legacy_sql = false
    }
    "vw_remediation_point" = {
      friendly_name  = "vw_remediation_point"
      query          = "../../../bigquery/reporting_views/views/vw_remediation_point.sql"
      use_legacy_sql = false
    }
    "vw_risk_management_plan_facilities" = {
      friendly_name  = "vw_risk_management_plan_facilities"
      query          = "../../../bigquery/reporting_views/views/vw_risk_management_plan_facilities.sql"
      use_legacy_sql = false
    }
    "vw_scrap_metal_processing_facilities" = {
      friendly_name  = "vw_scrap_metal_processing_facilities"
      query          = "../../../bigquery/reporting_views/views/vw_scrap_metal_processing_facilities.sql"
      use_legacy_sql = false
    }
    "vw_socrata_adult_care_facility_map" = {
      friendly_name  = "vw_socrata_adult_care_facility_map"
      query          = "../../../bigquery/reporting_views/views/vw_socrata_adult_care_facility_map.sql"
      use_legacy_sql = false
    }
    "vw_socrata_archived_parks_properties" = {
      friendly_name  = "vw_socrata_archived_parks_properties"
      query          = "../../../bigquery/reporting_views/views/vw_socrata_archived_parks_properties.sql"
      use_legacy_sql = false
    }
    "vw_socrata_athletic_facilities" = {
      friendly_name  = "vw_socrata_athletic_facilities"
      query          = "../../../bigquery/reporting_views/views/vw_socrata_athletic_facilities.sql"
      use_legacy_sql = false
    }
    "vw_socrata_child_care_regulated_programs" = {
      friendly_name  = "vw_socrata_child_care_regulated_programs"
      query          = "../../../bigquery/reporting_views/views/vw_socrata_child_care_regulated_programs.sql"
      use_legacy_sql = false
    }
    "vw_socrata_day_care_center" = {
      friendly_name  = "vw_socrata_day_care_center"
      query          = "../../../bigquery/reporting_views/views/vw_socrata_day_care_center.sql"
      use_legacy_sql = false
    }
    "vw_socrata_health_facility_general_information" = {
      friendly_name  = "vw_socrata_health_facility_general_information"
      query          = "../../../bigquery/reporting_views/views/vw_socrata_health_facility_general_information.sql"
      use_legacy_sql = false
    }
    "vw_socrata_health_facility_map" = {
      friendly_name  = "vw_socrata_health_facility_map"
      query          = "../../../bigquery/reporting_views/views/vw_socrata_health_facility_map.sql"
      use_legacy_sql = false
    }
    "vw_socrata_nyc_health_hospitals_patient_care_locations_2011" = {
      friendly_name  = "vw_socrata_nyc_health_hospitals_patient_care_locations_2011"
      query          = "../../../bigquery/reporting_views/views/vw_socrata_nyc_health_hospitals_patient_care_locations_2011.sql"
      use_legacy_sql = false
    }
    "vw_vehicle_dismantlers_facilities" = {
      friendly_name  = "vw_vehicle_dismantlers_facilities"
      query          = "../../../bigquery/reporting_views/views/vw_vehicle_dismantlers_facilities.sql"
      use_legacy_sql = false
    }
    "vw_vehicle_traffic_density_2019_all_ny" = {
      friendly_name  = "vw_vehicle_traffic_density_2019_all_ny"
      query          = "../../../bigquery/reporting_views/views/vw_vehicle_traffic_density_2019_all_ny.sql"
      use_legacy_sql = false
    }
    "vw_vehicle_traffic_density_2019_nyc" = {
      friendly_name  = "vw_vehicle_traffic_density_2019_nyc"
      query          = "../../../bigquery/reporting_views/views/vw_vehicle_traffic_density_2019_nyc.sql"
      use_legacy_sql = false
    }
    "vw_ftp_airnow_i" = {
      friendly_name  = "vw_ftp_airnow_i"
      query          = "../../../bigquery/reporting_views/views/vw_ftp_airnow_i.sql"
      use_legacy_sql = false
    }
    "vw_major_oil_storage_facilities" = {
      friendly_name  = "vw_major_oil_storage_facilities"
      query          = "../../../bigquery/reporting_views/views/vw_major_oil_storage_facilities.sql"
      use_legacy_sql = false
    }
  }
}

variable "ingestion_tables" {
  description = "Table definitions. Options and partitioning default to null. Partitioning can only use `range` or `time`, set the unused one to null."
  type        = map(object({
    friendly_name = string
    description   = string
    options       = object({
      clustering      = list(string)
      encryption_key  = string
      expiration_time = number
    })
    partitioning  = object({
      field = string
      range = object({
        end      = number
        interval = number
        start    = number
      })
      time  = object({
        expiration_ms = number
        type          = string
      })
    })
    schema        = string
  }))

  default = {
    "active_landfills" = {
      friendly_name = "active_landfills"
      description   = "Active landfills operating as of 6/23/2021. Includes the following types: construction & demolition debris, municipal solid waste, ones located on Long Island, and industrial solid waste."
      options       = null
      partitioning  = null
      schema        = "../../../bigquery/ingestion/schemas/active_landfills.json"
    }
    "benzene_modeled_concentrations_2017_emissions" = {
      friendly_name = "benzene_modeled_concentrations_2017_emissions"
      description   = "USEPA modeled results from 2017 National Emissions Inventory. Comprehensive assessment of all sources - point, area, mobile, biogenic, fires, secondary formation, background concentration - across the US. 2014 version used for DAC layer."
      options       = null
      partitioning  = null
      schema        = "../../../bigquery/ingestion/schemas/benzene_modeled_concentrations_2017_emissions.json"
    }
    "diesel_trucks_bus_traffic" = {
      friendly_name = "diesel_trucks_bus_traffic"
      description   = "NYS Roadway Inventory System NYSDOT Traffic Viewer, annual average daily traffic counts for 2019 using Federal Highway Administration vehicle classes 4-13. A buffer of 150-meters was generated around each census tract (US Census, 2019) to estimate the extent of diesel emissions. The buffers were overlaid with the NYSDOT roads and counts of diesel vehicles was length-weighted to the portion of road segments located within the buffer. Within each tract’s buffer, the total of the length-weighted annual average daily diesel vehicle count was divided by the total length of all roads in the buffer."
      options       = null
      partitioning  = null
      schema        = "../../../bigquery/ingestion/schemas/diesel_trucks_bus_traffic.json"
    }
    "disadvantaged_communities_indicator" = {
      friendly_name = "disadvantaged_communities_indicator"
      description   = "The Climate Leadership and Community Protection Act (CLCPA) directs the Climate Justice Working Group (CJWG) to establish criteria for defining disadvantaged communities. This dataset identifies areas throughout the State that meet the draft disadvantaged community definition as voted on by the Climate Justice Working Group. The draft Disadvantaged Community definition shown here will undergo 120 days of public input process and pending potential changes by the CJWG, will require a vote by the CJWG to finalize the definition."
      options       = null
      partitioning  = null
      schema        = "../../../bigquery/ingestion/schemas/disadvantaged_communities_indicator.json"
    }
    "municipal_waste_combustors" = {
      friendly_name = "municipal_waste_combustors"
      description   = "Active municipal waste combustors operating as of 6/23/21."
      options       = null
      partitioning  = null
      schema        = "../../../bigquery/ingestion/schemas/municipal_waste_combustors.json"
    }
    "major_oil_storage_facilities" = {
      friendly_name = "major_oil_storage_facilities"
      description   = "MOSF program applies to facilities that store 400,000 gallons or more of petroleum products in aboveground and underground storage tanks. These types of facilities process large quantities of petroleum products which can result in air releases of large quantities of volatile organic compounds some of which are hazardous air pollutants (e.g., benzene, toluene, and xylene). Additional community burdens include noise and emissions from truck traffic, rail, and marine transport. Many MOSF are in Ports which are often in proximity to environmental justice communities."
      options       = null
      partitioning  = null
      schema        = "../../../bigquery/ingestion/schemas/major_oil_storage_facilities.json"
    }
    "nys_public_school_k_12" = {
      friendly_name = "nys_public_school_k_12"
      description   = "Shape files for Public Schools K-12, Revised 10/2017."
      options       = null
      partitioning  = null
      schema        = "../../../bigquery/ingestion/schemas/nys_public_school_k_12.json"
    }
    "pm_25_2018_modeled_air_concentrations" = {
      friendly_name = "pm_25_2018_modeled_air_concentrations"
      description   = "Estimated census-tract level PM2.5 ambient annual average concentrations using a Bayesian space-time downscaling fusion model. Estimates are based on 2018 emissions. If using the most recent data available,  currenty it's 2021 EJ screen data the check here to see what year each data layer represents or is based on https://www.epa.gov/ejscreen/overview-environmental-indicators-ejscreen."
      options       = null
      partitioning  = null
      schema        = "../../../bigquery/ingestion/schemas/pm_25_2018_modeled_air_concentrations.json"
    }
    "power_generation_facilities_facility" = {
      friendly_name = "power_generation_facilities_facility"
      description   = "Fossil-fuel power generation facilities from NYSDEC’s 2019 emissions inventory (NYSDEC 2019)."
      options       = null
      partitioning  = null
      schema        = "../../../bigquery/ingestion/schemas/power_generation_facilities_facility.json"
    }
    "power_generation_facilities_unit" = {
      friendly_name = "power_generation_facilities_unit"
      description   = ""
      options       = null
      partitioning  = null
      schema        = "../../../bigquery/ingestion/schemas/power_generation_facilities_unit.json"
    }
    "remediation_area" = {
      friendly_name = "remediation_area"
      description   = ""
      options       = null
      partitioning  = null
      schema        = "../../../bigquery/ingestion/schemas/remediation_area.json"
    }
    "remediation_point" = {
      friendly_name = "remediation_point"
      description   = ""
      options       = null
      partitioning  = null
      schema        = "../../../bigquery/ingestion/schemas/remediation_point.json"
    }
    "risk_management_plan_facilities" = {
      friendly_name = "risk_management_plan_facilities"
      description   = "Count of Risk Management Plan (RMP - potential chemical accident management plan) facilities within 5 km (or nearest one beyond 5 km), of each census tract divided by distance in kilometers based on data from 2021."
      options       = null
      partitioning  = null
      schema        = "../../../bigquery/ingestion/schemas/risk_management_plan_facilities.json"
    }
    "scrap_metal_processing_facilities" = {
      friendly_name = "scrap_metal_processing_facilities"
      description   = "Scrap metal processor means a facility engaged primarily in the purchase, processing and shipment of ferrous and/or non-ferrous scrap (including decommissioned vehicles), the end product of which is the production of raw material for remelting purposes for steel mills, foundries, smelters, refiners, and similar users. Vehicle dismantling facility means a facility that decommissions, dismantles, and recycles end of life vehicles."
      options       = null
      partitioning  = null
      schema        = "../../../bigquery/ingestion/schemas/scrap_metal_processing_facilities.json"
    }
    "vehicle_dismantlers_facilities" = {
      friendly_name = "vehicle_dismantlers_facilities"
      description   = ""
      options       = null
      partitioning  = null
      schema        = "../../../bigquery/ingestion/schemas/vehicle_dismantlers_facilities.json"
    }
    "vehicle_traffic_density_2019_all_ny" = {
      friendly_name = "vehicle_traffic_density_2019_all_ny"
      description   = "Vehicle counts (average annual daily traffic) for 2019 at major roads (i.e., all interstate, principal arterials, and other collector highways in the national highway system) within 500 meters of a census block centroid, are divided by distance of the census block centroid in meters to the road. The results are population-weighted average to the census block group level (weighted by 2015-2019 ACS population). Since block group-level EJSCREEN data were obtained, they were aggregated to the tract-level by taking a weighted average of the block group observations, weighted by the proportion of the census tract population that was in the block group. If using the most recent data available, currenty it's 2021 EJ screen data the check here to see what year each data layer represents or is based on https://www.epa.gov/ejscreen/overview-environmental-indicators-ejscreen. "
      options       = null
      partitioning  = null
      schema        = "../../../bigquery/ingestion/schemas/vehicle_traffic_density_2019_all_ny.json"
    }
    "vehicle_traffic_density_2019_nyc" = {
      friendly_name = "vehicle_traffic_density_2019_nyc"
      description   = "Vehicle counts (average annual daily traffic) for 2019 at major roads (i.e., all interstate, principal arterials, and other collector highways in the national highway system) within 500 meters of a census block centroid, are divided by distance of the census block centroid in meters to the road. The results are population-weighted average to the census block group level (weighted by 2015-2019 ACS population). Since block group-level EJSCREEN data were obtained, they were aggregated to the tract-level by taking a weighted average of the block group observations, weighted by the proportion of the census tract population that was in the block group. If using the most recent data available, currenty it's 2021 EJ screen data the check here to see what year each data layer represents or is based on https://www.epa.gov/ejscreen/overview-environmental-indicators-ejscreen. "
      options       = null
      partitioning  = null
      schema        = "../../../bigquery/ingestion/schemas/vehicle_traffic_density_2019_nyc.json"
    }
  }
}

variable "ingestion_arcgis_tables" {
  description = "Table definitions. Options and partitioning default to null. Partitioning can only use `range` or `time`, set the unused one to null."
  type        = map(object({
    friendly_name = string
    description   = string
    options       = object({
      clustering      = list(string)
      encryption_key  = string
      expiration_time = number
    })
    partitioning  = object({
      field = string
      range = object({
        end      = number
        interval = number
        start    = number
      })
      time  = object({
        expiration_ms = number
        type          = string
      })
    })
    schema        = string
  }))

  default = {
    "air_facilities_system" = {
      friendly_name = "air_facilities_system"
      description   = ""
      options       = null
      partitioning  = null
      schema        = "../../../bigquery/ingestion_arcgis/schemas/air_facilities_system.json"
    }
    "air_facility_registration" = {
      friendly_name = "air_facility_registration"
      description   = ""
      options       = null
      partitioning  = null
      schema        = "../../../bigquery/ingestion_arcgis/schemas/air_facility_registration.json"
    }
    "atv_total_emissions_submitted" = {
      friendly_name = "atv_total_emissions_submitted"
      description   = ""
      options       = null
      partitioning  = null
      schema        = "../../../bigquery/ingestion_arcgis/schemas/atv_total_emissions_submitted.json"
    }
    "major_oil_storage_facilities" = {
      friendly_name = "major_oil_storage_facilities"
      description   = " MOSF program applies to facilities that store 400,000 gallons or more of petroleum products in aboveground and underground storage tanks. These types of facilities process large quantities of petroleum products which can result in air releases of large quantities of volatile organic compounds some of which are hazardous air pollutants (e.g., benzene, toluene, and xylene). Additional community burdens include noise and emissions from truck traffic, rail, and marine transport. Many MOSF are in Ports which are often in proximity to environmental justice communities."
      options       = null
      partitioning  = null
      schema        = "../../../bigquery/ingestion_arcgis/schemas/major_oil_storage_facilities.json"
    }
    "nursing_homes" = {
      friendly_name = "nursing_homes"
      description   = "This feature class/shapefile contains nursing and assisted care facilities for the Homeland Infrastructure Foundation-Level Data (HIFLD) database."
      options       = null
      partitioning  = null
      schema        = "../../../bigquery/ingestion_arcgis/schemas/nursing_homes.json"
    }
    "remediation_boundaries" = {
      friendly_name = "remediation_boundaries"
      description   = ""
      options       = null
      partitioning  = null
      schema        = "../../../bigquery/ingestion_arcgis/schemas/remediation_boundaries.json"
    }
    "remediation_sites" = {
      friendly_name = "remediation_sites"
      description   = "NYSDEC’s database on the State’s Brownfield Cleanup program and Class II, and federal environmental remediation sites (USEPA National Priority List) sites as of July 26, 2010."
      options       = null
      partitioning  = null
      schema        = "../../../bigquery/ingestion_arcgis/schemas/remediation_sites.json"
    }
  }
}

variable "ingestion_socrata_tables" {
  description = "Table definitions. Options and partitioning default to null. Partitioning can only use `range` or `time`, set the unused one to null."
  type        = map(object({
    friendly_name = string
    description   = string
    options       = object({
      clustering      = list(string)
      encryption_key  = string
      expiration_time = number
    })
    partitioning  = object({
      field = string
      range = object({
        end      = number
        interval = number
        start    = number
      })
      time  = object({
        expiration_ms = number
        type          = string
      })
    })
    schema        = string
  }))

  default = {
    "adult_care_facility_map" = {
      friendly_name = "adult_care_facility_map"
      description   = "Map with exportable data."
      options       = null
      partitioning  = null
      schema        = "../../../bigquery/ingestion_socrata/schemas/adult_care_facility_map.json"
    }
    "archived_parks_properties" = {
      friendly_name = "archived_parks_properties"
      description   = "This data identifies City property under the jurisdiction of NYC Parks, which may be managed partially or solely by the Agency."
      options       = null
      partitioning  = null
      schema        = "../../../bigquery/ingestion_socrata/schemas/archived_parks_properties.json"
    }
    "athletic_facilities" = {
      friendly_name = "athletic_facilities"
      description   = ""
      options       = null
      partitioning  = null
      schema        = "../../../bigquery/ingestion_socrata/schemas/athletic_facilities.json"
    }
    "child_care_regulated_programs" = {
      friendly_name = "child_care_regulated_programs"
      description   = ""
      options       = null
      partitioning  = null
      schema        = "../../../bigquery/ingestion_socrata/schemas/child_care_regulated_programs.json"
    }
    "day_care_center" = {
      friendly_name = "day_care_center"
      description   = "Information on OCFS regulated child care programs; file was filtered for licensed daycare centers (DCC)."
      options       = null
      partitioning  = null
      schema        = "../../../bigquery/ingestion_socrata/schemas/day_care_center.json"
    }
    "health_facility_general_information" = {
      friendly_name = "health_facility_general_information"
      description   = "File was filtered for hospitals only."
      options       = null
      partitioning  = null
      schema        = "../../../bigquery/ingestion_socrata/schemas/health_facility_general_information.json"
    }
    "health_facility_map" = {
      friendly_name = "health_facility_map"
      description   = "Map with exportable data."
      options       = null
      partitioning  = null
      schema        = "../../../bigquery/ingestion_socrata/schemas/health_facility_map.json"
    }
    "nyc_health_hospitals_patient_care_locations_2011" = {
      friendly_name = "nyc_health_hospitals_patient_care_locations_2011"
      description   = ""
      options       = null
      partitioning  = null
      schema        = "../../../bigquery/ingestion_socrata/schemas/nyc_health_hospitals_patient_care_locations_2011.json"
    }
  }
}

variable "ingestion_aqs_tables" {
  description = "Table definitions. Options and partitioning default to null. Partitioning can only use `range` or `time`, set the unused one to null."
  type        = map(object({
    friendly_name = string
    description   = string
    options       = object({
      clustering      = list(string)
      encryption_key  = string
      expiration_time = number
    })
    partitioning  = object({
      field = string
      range = object({
        end      = number
        interval = number
        start    = number
      })
      time  = object({
        expiration_ms = number
        type          = string
      })
    })
    schema        = string
  }))

  default = {
    "black_carbon_pm2_5_corrected" = {
      friendly_name = "black_carbon_pm2_5_corrected"
      description   = ""
      options       = null
      partitioning  = null
      schema        = "../../../bigquery/ingestion_aqs/schemas/black_carbon_pm2_5_corrected.json"
    }
    "carbon_monoxide" = {
      friendly_name = "carbon_monoxide"
      description   = ""
      options       = null
      partitioning  = null
      schema        = "../../../bigquery/ingestion_aqs/schemas/carbon_monoxide.json"
    }
    "ethane" = {
      friendly_name = "ethane"
      description   = ""
      options       = null
      partitioning  = null
      schema        = "../../../bigquery/ingestion_aqs/schemas/ethane.json"
    }
    "formaldehyde" = {
      friendly_name = "formaldehyde"
      description   = ""
      options       = null
      partitioning  = null
      schema        = "../../../bigquery/ingestion_aqs/schemas/formaldehyde.json"
    }
    "nitric_oxide" = {
      friendly_name = "nitric_oxide"
      description   = ""
      options       = null
      partitioning  = null
      schema        = "../../../bigquery/ingestion_aqs/schemas/nitric_oxide.json"
    }
    "nitrogen_dioxide" = {
      friendly_name = "nitrogen_dioxide"
      description   = ""
      options       = null
      partitioning  = null
      schema        = "../../../bigquery/ingestion_aqs/schemas/nitrogen_dioxide.json"
    }
    "ozone" = {
      friendly_name = "ozone"
      description   = ""
      options       = null
      partitioning  = null
      schema        = "../../../bigquery/ingestion_aqs/schemas/ozone.json"
    }
    "pm_25" = {
      friendly_name = "pm_25"
      description   = ""
      options       = null
      partitioning  = null
      schema        = "../../../bigquery/ingestion_aqs/schemas/pm_25.json"
    }
    "sulfur_dioxide" = {
      friendly_name = "sulfur_dioxide"
      description   = ""
      options       = null
      partitioning  = null
      schema        = "../../../bigquery/ingestion_aqs/schemas/sulfur_dioxide.json"
    }
    "toxics_and_carbonyls" = {
      friendly_name = "toxics_and_carbonyls"
      description   = ""
      options       = null
      partitioning  = null
      schema        = "../../../bigquery/ingestion_aqs/schemas/toxics_and_carbonyls.json"
    }
  }
}

variable "warehouse_tables" {
  description = "Table definitions. Options and partitioning default to null. Partitioning can only use `range` or `time`, set the unused one to null."
  type        = map(object({
    friendly_name = string
    description   = string
    options       = object({
      clustering      = list(string)
      encryption_key  = string
      expiration_time = number
    })
    partitioning  = object({
      field = string
      range = object({
        end      = number
        interval = number
        start    = number
      })
      time  = object({
        expiration_ms = number
        type          = string
      })
    })
    schema        = string
  }))

  default = {
    "aqs_black_carbon_pm2_5_corrected" = {
      friendly_name = "aqs_black_carbon_pm2_5_corrected"
      description   = ""
      options       = null
      partitioning  = {
        field = "ingestion_timestamp"
        range = null # use start/end/interval for range
        time  = { type = "DAY", expiration_ms = null }
      }
      schema        = "../../../bigquery/warehouse/schemas/aqs_black_carbon_pm2_5_corrected.json"
    }
    "aqs_carbon_monoxide" = {
      friendly_name = "aqs_carbon_monoxide"
      description   = ""
      options       = null
      partitioning  = {
        field = "ingestion_timestamp"
        range = null # use start/end/interval for range
        time  = { type = "DAY", expiration_ms = null }
      }
      schema        = "../../../bigquery/warehouse/schemas/aqs_carbon_monoxide.json"
    }
    "aqs_ethane" = {
      friendly_name = "aqs_ethane"
      description   = ""
      options       = null
      partitioning  = {
        field = "ingestion_timestamp"
        range = null # use start/end/interval for range
        time  = { type = "DAY", expiration_ms = null }
      }
      schema        = "../../../bigquery/warehouse/schemas/aqs_ethane.json"
    }
    "aqs_formaldehyde" = {
      friendly_name = "aqs_formaldehyde"
      description   = ""
      options       = null
      partitioning  = {
        field = "ingestion_timestamp"
        range = null # use start/end/interval for range
        time  = { type = "DAY", expiration_ms = null }
      }
      schema        = "../../../bigquery/warehouse/schemas/aqs_formaldehyde.json"
    }
    "aqs_nitric_oxide" = {
      friendly_name = "aqs_nitric_oxide"
      description   = ""
      options       = null
      partitioning  = {
        field = "ingestion_timestamp"
        range = null # use start/end/interval for range
        time  = { type = "DAY", expiration_ms = null }
      }
      schema        = "../../../bigquery/warehouse/schemas/aqs_nitric_oxide.json"
    }
    "aqs_nitrogen_dioxide" = {
      friendly_name = "aqs_nitrogen_dioxide"
      description   = ""
      options       = null
      partitioning  = {
        field = "ingestion_timestamp"
        range = null # use start/end/interval for range
        time  = { type = "DAY", expiration_ms = null }
      }
      schema        = "../../../bigquery/warehouse/schemas/aqs_nitrogen_dioxide.json"
    }
    "aqs_ozone" = {
      friendly_name = "aqs_ozone"
      description   = ""
      options       = null
      partitioning  = {
        field = "ingestion_timestamp"
        range = null # use start/end/interval for range
        time  = { type = "DAY", expiration_ms = null }
      }
      schema        = "../../../bigquery/warehouse/schemas/aqs_ozone.json"
    }
    "aqs_pm_25" = {
      friendly_name = "aqs_pm_25"
      description   = ""
      options       = null
      partitioning  = {
        field = "ingestion_timestamp"
        range = null # use start/end/interval for range
        time  = { type = "DAY", expiration_ms = null }
      }
      schema        = "../../../bigquery/warehouse/schemas/aqs_pm_25.json"
    }
    "aqs_sulfur_dioxide" = {
      friendly_name = "aqs_sulfur_dioxide"
      description   = ""
      options       = null
      partitioning  = {
        field = "ingestion_timestamp"
        range = null # use start/end/interval for range
        time  = { type = "DAY", expiration_ms = null }
      }
      schema        = "../../../bigquery/warehouse/schemas/aqs_sulfur_dioxide.json"
    }
    "aqs_toxics_and_carbonyls" = {
      friendly_name = "aqs_toxics_and_carbonyls"
      description   = ""
      options       = null
      partitioning  = {
        field = "ingestion_timestamp"
        range = null # use start/end/interval for range
        time  = { type = "DAY", expiration_ms = null }
      }
      schema        = "../../../bigquery/warehouse/schemas/aqs_toxics_and_carbonyls.json"
    }
    "arcgis_air_facilities_system" = {
      friendly_name = "arcgis_air_facilities_system"
      description   = ""
      options       = null
      partitioning  = {
        field = "ingestion_timestamp"
        range = null # use start/end/interval for range
        time  = { type = "DAY", expiration_ms = null }
      }
      schema        = "../../../bigquery/warehouse/schemas/arcgis_air_facilities_system.json"
    }
    "arcgis_air_facility_registration" = {
      friendly_name = "arcgis_air_facility_registration"
      description   = ""
      options       = null
      partitioning  = {
        field = "ingestion_timestamp"
        range = null # use start/end/interval for range
        time  = { type = "DAY", expiration_ms = null }
      }
      schema        = "../../../bigquery/warehouse/schemas/arcgis_air_facility_registration.json"
    }
    "arcgis_atv_total_emissions_submitted" = {
      friendly_name = "arcgis_atv_total_emissions_submitted"
      description   = ""
      options       = null
      partitioning  = {
        field = "ingestion_timestamp"
        range = null # use start/end/interval for range
        time  = { type = "DAY", expiration_ms = null }
      }
      schema        = "../../../bigquery/warehouse/schemas/arcgis_atv_total_emissions_submitted.json"
    }
    "arcgis_major_oil_storage_facilities" = {
      friendly_name = "arcgis_major_oil_storage_facilities"
      description   = "MOSF program applies to facilities that store 400,000 gallons or more of petroleum products in aboveground and underground storage tanks. These types of facilities process large quantities of petroleum products which can result in air releases of large quantities of volatile organic compounds some of which are hazardous air pollutants (e.g., benzene, toluene, and xylene). Additional community burdens include noise and emissions from truck traffic, rail, and marine transport. Many MOSF are in Ports which are often in proximity to environmental justice communities."
      options       = null
      partitioning  = {
        field = "ingestion_timestamp"
        range = null # use start/end/interval for range
        time  = { type = "DAY", expiration_ms = null }
      }
      schema        = "../../../bigquery/warehouse/schemas/arcgis_major_oil_storage_facilities.json"
    }
    "arcgis_nursing_homes" = {
      friendly_name = "arcgis_nursing_homes"
      description   = "This feature class/shapefile contains nursing and assisted care facilities for the Homeland Infrastructure Foundation-Level Data (HIFLD) database."
      options       = null
      partitioning  = {
        field = "ingestion_timestamp"
        range = null # use start/end/interval for range
        time  = { type = "DAY", expiration_ms = null }
      }
      schema        = "../../../bigquery/warehouse/schemas/arcgis_nursing_homes.json"
    }
    "arcgis_remediation_boundaries" = {
      friendly_name = "arcgis_remediation_boundaries"
      description   = ""
      options       = null
      partitioning  = {
        field = "ingestion_timestamp"
        range = null # use start/end/interval for range
        time  = { type = "DAY", expiration_ms = null }
      }
      schema        = "../../../bigquery/warehouse/schemas/arcgis_remediation_boundaries.json"
    }
    "arcgis_remediation_sites" = {
      friendly_name = "arcgis_remediation_sites"
      description   = "NYSDEC’s database on the State’s Brownfield Cleanup program and Class II, and federal environmental remediation sites (USEPA National Priority List) sites as of July 26, 2010."
      options       = null
      partitioning  = {
        field = "ingestion_timestamp"
        range = null # use start/end/interval for range
        time  = { type = "DAY", expiration_ms = null }
      }
      schema        = "../../../bigquery/warehouse/schemas/arcgis_remediation_sites.json"
    }
    "socrata_adult_care_facility_map" = {
      friendly_name = "socrata_adult_care_facility_map"
      description   = "Map with exportable data."
      options       = null
      partitioning  = {
        field = "ingestion_timestamp"
        range = null # use start/end/interval for range
        time  = { type = "DAY", expiration_ms = null }
      }
      schema        = "../../../bigquery/warehouse/schemas/socrata_adult_care_facility_map.json"
    }
    "socrata_archived_parks_properties" = {
      friendly_name = "socrata_archived_parks_properties"
      description   = "This data identifies City property under the jurisdiction of NYC Parks, which may be managed partially or solely by the Agency."
      options       = null
      partitioning  = {
        field = "ingestion_timestamp"
        range = null # use start/end/interval for range
        time  = { type = "DAY", expiration_ms = null }
      }
      schema        = "../../../bigquery/warehouse/schemas/socrata_archived_parks_properties.json"
    }
    "socrata_athletic_facilities" = {
      friendly_name = "socrata_athletic_facilities"
      description   = ""
      options       = null
      partitioning  = {
        field = "ingestion_timestamp"
        range = null # use start/end/interval for range
        time  = { type = "DAY", expiration_ms = null }
      }
      schema        = "../../../bigquery/warehouse/schemas/socrata_athletic_facilities.json"
    }
    "socrata_child_care_regulated_programs" = {
      friendly_name = "socrata_child_care_regulated_programs"
      description   = ""
      options       = null
      partitioning  = {
        field = "ingestion_timestamp"
        range = null # use start/end/interval for range
        time  = { type = "DAY", expiration_ms = null }
      }
      schema        = "../../../bigquery/warehouse/schemas/socrata_child_care_regulated_programs.json"
    }
    "socrata_day_care_center" = {
      friendly_name = "socrata_day_care_center"
      description   = "Information on OCFS regulated child care programs; file was filtered for licensed daycare centers (DCC)."
      options       = null
      partitioning  = {
        field = "ingestion_timestamp"
        range = null # use start/end/interval for range
        time  = { type = "DAY", expiration_ms = null }
      }
      schema        = "../../../bigquery/warehouse/schemas/socrata_day_care_center.json"
    }
    "socrata_health_facility_general_information" = {
      friendly_name = "socrata_health_facility_general_information"
      description   = "File was filtered for hospitals only."
      options       = null
      partitioning  = {
        field = "ingestion_timestamp"
        range = null # use start/end/interval for range
        time  = { type = "DAY", expiration_ms = null }
      }
      schema        = "../../../bigquery/warehouse/schemas/socrata_health_facility_general_information.json"
    }
    "socrata_health_facility_map" = {
      friendly_name = "socrata_health_facility_map"
      description   = "Map with exportable data."
      options       = null
      partitioning  = {
        field = "ingestion_timestamp"
        range = null # use start/end/interval for range
        time  = { type = "DAY", expiration_ms = null }
      }
      schema        = "../../../bigquery/warehouse/schemas/socrata_health_facility_map.json"
    }
    "socrata_nyc_health_hospitals_patient_care_locations_2011" = {
      friendly_name = "socrata_nyc_health_hospitals_patient_care_locations_2011"
      description   = ""
      options       = null
      partitioning  = {
        field = "ingestion_timestamp"
        range = null # use start/end/interval for range
        time  = { type = "DAY", expiration_ms = null }
      }
      schema        = "../../../bigquery/warehouse/schemas/socrata_nyc_health_hospitals_patient_care_locations_2011.json"
    }
    "ftp_airnow_i" = {
      friendly_name = "ftp_airnow_i"
      description   = ""
      options       = null
      partitioning  = {
        field = "record_date"
        range = null # use start/end/interval for range
        time  = { type = "DAY", expiration_ms = null }
      }
      schema        = "../../../bigquery/warehouse/schemas/ftp_airnow_i.json"
    }
  }
}

variable "job_metadata_tables" {
  description = "Table definitions."
  type        = map(object({
    friendly_name = string
    description   = string
    options       = object({
      clustering      = list(string)
      encryption_key  = string
      expiration_time = number
    })
    partitioning  = object({
      field = string
      range = object({
        end      = number
        interval = number
        start    = number
      })
      time  = object({
        expiration_ms = number
        type          = string
      })
    })
    schema        = string
  }))

  default = {
    "job_audit" = {
      friendly_name = "job_audit"
      description   = ""
      options       = null
      partitioning  = null
      schema        = "../../../bigquery/job_metadata/schemas/job_audit.json"
    }
    "new_column_audit" = {
      friendly_name = "new_column_audit"
      description   = ""
      options       = null
      partitioning  = null
      schema        = "../../../bigquery/job_metadata/schemas/new_column_audit.json"
    }
  }
}

variable "reporting_procedures" {
  description = "Procedure definitions."
  type        = map(object({
    routine_id      = string
    definition_body = string
  }))
  default     = {
    "sp_black_carbon_pm2_5_corrected" = {
      routine_id      = "sp_black_carbon_pm2_5_corrected"
      definition_body = "../../../bigquery/reporting_views/stored_procedures/sp_black_carbon_pm2_5_corrected.sql"
    }
    "sp_carbon_monoxide" = {
      routine_id      = "sp_carbon_monoxide"
      definition_body = "../../../bigquery/reporting_views/stored_procedures/sp_carbon_monoxide.sql"
    }
    "sp_ethane" = {
      routine_id      = "sp_ethane"
      definition_body = "../../../bigquery/reporting_views/stored_procedures/sp_ethane.sql"
    }
    "sp_formaldehyde" = {
      routine_id      = "sp_formaldehyde"
      definition_body = "../../../bigquery/reporting_views/stored_procedures/sp_formaldehyde.sql"
    }
    "sp_nitric_oxide" = {
      routine_id      = "sp_nitric_oxide"
      definition_body = "../../../bigquery/reporting_views/stored_procedures/sp_nitric_oxide.sql"
    }
    "sp_nitrogen_dioxide" = {
      routine_id      = "sp_nitrogen_dioxide"
      definition_body = "../../../bigquery/reporting_views/stored_procedures/sp_nitrogen_dioxide.sql"
    }
    "sp_ozone" = {
      routine_id      = "sp_ozone"
      definition_body = "../../../bigquery/reporting_views/stored_procedures/sp_ozone.sql"
    }
    "sp_pm_25" = {
      routine_id      = "sp_pm_25"
      definition_body = "../../../bigquery/reporting_views/stored_procedures/sp_pm_25.sql"
    }
    "sp_sulfur_dioxide" = {
      routine_id      = "sp_sulfur_dioxide"
      definition_body = "../../../bigquery/reporting_views/stored_procedures/sp_sulfur_dioxide.sql"
    }
    "sp_toxics_and_carbonyls" = {
      routine_id      = "sp_toxics_and_carbonyls"
      definition_body = "../../../bigquery/reporting_views/stored_procedures/sp_toxics_and_carbonyls.sql"
    }
  }
}

variable "ingestion_ftp_tables" {
  description = "Table definitions. Source is FTP."
  type        = map(object({
    friendly_name = string
    description   = string
    options       = object({
      clustering      = list(string)
      encryption_key  = string
      expiration_time = number
    })
    partitioning  = object({
      field = string
      range = object({
        end      = number
        interval = number
        start    = number
      })
      time  = object({
        expiration_ms = number
        type          = string
      })
    })
    schema        = string
  }))

  default = {
    "airnow_i" = {
      friendly_name = "airnow_i"
      description   = "As part of the AirNow-International (AirNow-I) project, Sonoma Technology, Inc. (STI) developed a simple, compact data exchange format to transfer data between AirNow-I and other data management systems (DMS)."
      options       = null
      partitioning  = null
      schema        = "../../../bigquery/ingestion_ftp/schemas/airnow_i.json"
    }
  }
}

variable "read_access_sa" {
  type = list(string)
}
