"""
config.py module.
This module has all the mapping configurations info like web service url,
GCS locations and parsing type required to fetch data from different web
services and write the data over a specified GCS locations
"""
from common import constant

# Data layer and GCP Mapping
arcgis_data_layer_and_gcp_mapping = {
  "nursing_homes": {
    "data_source": "arcgis_apis",
    "parsing_type": "geometry_data",
    "layer_name": "nursing_homes",
    "layer_url": "https://services1.arcgis.com/Hp6G80Pky0om7QvQ/"
                 "ArcGIS/rest/services/NursingHomes/FeatureServer/0",
    "parsed_gcs_file_uri": "parsed/"
                           "nursing_homes/"
                           f"{constant.CURRENT_DATE}/"
                           "nursing_homes_{}.json",
    "raw_gcs_file_uri": "raw/"
                        "nursing_homes/"
                        f"{constant.CURRENT_DATE}/"
                        "nursing_homes_{}.json"
  },
  "remediation_sites": {
    "data_source": "arcgis_apis",
    "parsing_type": "geometry_data",
    "layer_name": "remediation_sites",
    "layer_url": "https://services6.arcgis.com/DZHaqZm9cxOD4CWM/"
                 "ArcGIS/rest/services/Remediation_Sites/FeatureServer/0",
    "parsed_gcs_file_uri": "parsed/"
                           "remediation_sites/"
                           f"{constant.CURRENT_DATE}/"
                           "remediation_sites_{}.json",
    "raw_gcs_file_uri": "raw/"
                        "remediation_sites/"
                        f"{constant.CURRENT_DATE}/"
                        "remediation_sites_{}.json"
  },
  "remediation_boundaries": {
    "data_source": "arcgis_apis",
    "parsing_type": "geometry_rings_data",
    "layer_name": "remediation_boundaries",
    "layer_url": "https://services6.arcgis.com/DZHaqZm9cxOD4CWM/ArcGIS/"
                 "rest/services/Remediation_Boundaries/FeatureServer/0",
    "parsed_gcs_file_uri": "parsed/"
                           "remediation_boundaries/"
                           f"{constant.CURRENT_DATE}/"
                           "remediation_boundaries_{}.json",
    "raw_gcs_file_uri": "raw/"
                        "remediation_boundaries/"
                        f"{constant.CURRENT_DATE}/"
                        "remediation_boundaries_{}.json"
  },

  "air_title_v": {
    "data_source": "arcgis_apis",
    "parsing_type": "no_parsing",
    "layer_name": "air_title_v",
    "layer_url": "https://services6.arcgis.com/DZHaqZm9cxOD4CWM/ArcGIS/rest/"
                 "services/CLCPA_ATV/FeatureServer/0",
    "parsed_gcs_file_uri": "parsed/"
                           "air_title_v/"
                           f"{constant.CURRENT_DATE}/"
                           "air_title_v_{}.json",
    "raw_gcs_file_uri": "raw/"
                        "air_title_v/"
                        f"{constant.CURRENT_DATE}/"
                        "air_title_v_{}.json"
  },
  "air_facilities_system": {
    "data_source": "arcgis_apis",
    "parsing_type": "no_parsing",
    "layer_name": "air_facilities_system",
    "layer_url": "https://services6.arcgis.com/DZHaqZm9cxOD4CWM/ArcGIS/rest/"
                 "services/CLCPA_ASF/FeatureServer/0",
    "parsed_gcs_file_uri": "parsed/"
                           "air_facilities_system/"
                           f"{constant.CURRENT_DATE}/"
                           "air_facilities_system_{}.json",
    "raw_gcs_file_uri": "raw/"
                        "air_facilities_system/"
                        f"{constant.CURRENT_DATE}/"
                        "air_facilities_system_{}.json"
  },
  "air_facility_registration": {
    "data_source": "arcgis_apis",
    "parsing_type": "no_parsing",
    "layer_name": "air_facility_registration",
    "layer_url": "https://services6.arcgis.com/DZHaqZm9cxOD4CWM/ArcGIS/"
                 "rest/services/CLCPA_AFR/FeatureServer/0",
    "parsed_gcs_file_uri": "parsed/"
                           "air_facility_registration/"
                           f"{constant.CURRENT_DATE}/"
                           "air_facility_registration_{}.json",
    "raw_gcs_file_uri": "raw/"
                        "air_facility_registration/"
                        f"{constant.CURRENT_DATE}/"
                        "air_facility_registration_{}.json"
  },
  "major_oil_storage_facilities": {
    "data_source": "arcgis_apis",
    "parsing_type": "geometry_data",
    "layer_name": "major_oil_storage_facilities",
    "layer_url": "https://services6.arcgis.com/DZHaqZm9cxOD4CWM/ArcGIS"
                 "/rest/services/Major_Oil_Storage_Facility/FeatureServer/0",
    "parsed_gcs_file_uri": "parsed/"
                           "major_oil_storage_facilities/"
                           f"{constant.CURRENT_DATE}/"
                           "major_oil_storage_facilities_{}.json",
    "raw_gcs_file_uri": "raw/"
                        "major_oil_storage_facilities/"
                        f"{constant.CURRENT_DATE}/"
                        "major_oil_storage_facilities_{}.json"
  }

}

socrata_data_layer_and_gcp_mapping = {
  "adult_care_facility_map": {
    "data_source": "socrata",
    "layer_name": "adult_care_facility_map",
    "url": "https://health.data.ny.gov/resource/"
           "6wkx-ptu4.json?$select=count(*)",
    "parsed_gcs_file_uri": "parsed/"
                           "adult_care_facility_map/"
                           f"{constant.CURRENT_DATE}/"
                           "adult_care_facility_map_{}.json",
    "raw_gcs_file_uri": "raw/"
                        "adult_care_facility_map/"
                        f"{constant.CURRENT_DATE}/"
                        "adult_care_facility_map_{}.json",
    "domain_name": "health.data.ny.gov",
    "dataset_name": "6wkx-ptu4",
    "parsing_type": "human_address_data",
    "title": "Adult Care Facility Directory"

  },
  "health_facility_general_information": {
    "data_source": "socrata",
    "layer_name": "health_facility_general_information",
    "url": "https://health.data.ny.gov/"
           "resource/vn5v-hh5r.json?$select=count(*)",
    "parsed_gcs_file_uri": "parsed/"
                           "health_facility_general_information/"
                           f"{constant.CURRENT_DATE}/"
                           "health_facility_general_information_{}.json",
    "raw_gcs_file_uri": "raw/"
                        "health_facility_general_information/"
                        f"{constant.CURRENT_DATE}/"
                        "health_facility_general_information_{}.json",
    "domain_name": "health.data.ny.gov",
    "dataset_name": "vn5v-hh5r",
    "parsing_type": "no_parsing",
    "title": "Health Facility General Information"

  },
  "health_facility_map": {
    "data_source": "socrata",
    "layer_name": "health_facility_map",
    "url": "https://health.data.ny.gov/"
           "resource/875v-tpc8.json?$select=count(*)",
    "parsed_gcs_file_uri": "parsed/"
                           "health_facility_map/"
                           f"{constant.CURRENT_DATE}/"
                           "health_facility_map_{}.json",
    "raw_gcs_file_uri": "raw/"
                        "health_facility_map/"
                        f"{constant.CURRENT_DATE}/"
                        "health_facility_map_{}.json",
    "domain_name": "health.data.ny.gov",
    "dataset_name": "875v-tpc8",
    "parsing_type": "no_parsing",
    "title": "Health Facility Map"
  },

  "nyc_health_hospitals_patient_care_locations_2011": {
    "data_source": "socrata",
    "layer_name":
      "nyc_health_hospitals_patient_care_locations_2011",
    "url": "https://data.cityofnewyork.us/"
           "resource/f7b6-v6v3.json?$select=count(*)",
    "parsed_gcs_file_uri": "parsed/"
                           "nyc_health_hospitals_patient_"
                           "care_locations_2011/"
                           f"{constant.CURRENT_DATE}/"
                           "nyc_health_hospitals_patient_care"
                           "_locations_2011_{}.json",
    "raw_gcs_file_uri": "raw/"
                        "nyc_health_hospitals_patient_"
                        "care_locations_2011/"
                        f"{constant.CURRENT_DATE}/"
                        "nyc_health_hospitals_patient_"
                        "care_locations_2011_{}.json",
    "domain_name": "data.cityofnewyork.us",
    "dataset_name": "f7b6-v6v3",
    "parsing_type": "human_address_data",
    "title": "NYC Health + Hospitals patient care locations - 2011"

  },

  "archived_parks_properties": {
    "data_source": "socrata",
    "layer_name": "archived_parks_properties",
    "url": "https://data.cityofnewyork.us/"
           "resource/ghu2-eden.json?$select=count(*)",
    "parsed_gcs_file_uri": "parsed/"
                           "archived_parks_properties/"
                           f"{constant.CURRENT_DATE}/"
                           "archived_parks_properties_{}.json",
    "raw_gcs_file_uri": "raw/"
                        "archived_parks_properties/"
                        f"{constant.CURRENT_DATE}/"
                        "archived_parks_properties_{}.json",
    "domain_name": "data.cityofnewyork.us",
    "dataset_name": "ghu2-eden",
    "parsing_type": "multipolygon_data",
    "title": "ARCHIVED - Parks Properties"
  },

  "athletic_facilities": {
    "data_source": "socrata",
    "layer_name": "athletic_facilities",
    "url": "https://data.cityofnewyork.us/"
           "resource/9wwi-sb8x.json?$select=count(*)",
    "parsed_gcs_file_uri": "parsed/"
                           "athletic_facilities/"
                           f"{constant.CURRENT_DATE}/"
                           "athletic_facilities_{}.json",

    "raw_gcs_file_uri": "raw/"
                        "athletic_facilities/"
                        f"{constant.CURRENT_DATE}/"
                        "athletic_facilities_{}.json",
    "domain_name": "data.cityofnewyork.us",
    "dataset_name": "9wwi-sb8x",
    "parsing_type": "multipolygon_data",
    "title": "ARCHIVE - Athletic Facilities"

  },
  "child_care_regulated_programs": {
    "data_source": "socrata",
    "layer_name": "child_care_regulated_programs",
    "url": "https://data.ny.gov/resource/cb42-qumz.json?$select=count(*)",
    "parsed_gcs_file_uri": "parsed/"
                           "child_care_regulated_programs/"
                           f"{constant.CURRENT_DATE}/"
                           "child_care_regulated_programs_{}.json",
    "raw_gcs_file_uri": "raw/ "
                        "child_care_regulated_programs/"
                        f"{constant.CURRENT_DATE}/"
                        "child_care_regulated_programs_{}.json",
    "domain_name": "data.ny.gov",
    "dataset_name": "cb42-qumz",
    "parsing_type": "point_data",
    "title": "Child Care Regulated Programs"
  },

  "day_care_center": {
    "data_source": "socrata",
    "layer_name": "day_care_center",
    "url": "https://data.cityofnewyork.us/"
           "resource/sd93-evwm.json?$select=count(*)",
    "parsed_gcs_file_uri": "parsed/"
                           "day_care_center/"
                           f"{constant.CURRENT_DATE}/"
                           "day_care_center_{}.json",
    "raw_gcs_file_uri": "raw/"
                        "day_care_center/"
                        f"{constant.CURRENT_DATE}/"
                        "day_care_center_{}.json",
    "domain_name": "data.cityofnewyork.us",

    "dataset_name": "sd93-evwm",
    "parsing_type": "point_data",
    "title": "Day Care Center"
  },
}

aqs_api_data_layer_and_gcp_mapping = {

  "black_carbon_pm2_5_corrected": {
    "data_source": "aqs",
    "param": "88317,84313",
    "layer_name": "black_carbon_pm2_5_corrected",
    "layer_url": "https://aqs.epa.gov/data/api/sampleData/byState?email="
                 + constant.AQS_EMAIL + "&key=" + constant.AQS_KEY +
                 "&param=88317,88313&bdate={}&edate={}&state=36",
    "parsed_gcs_file_uri": "parsed/black_carbon_pm2_5_corrected/"
                           f"{constant.CURRENT_DATE}/"
                           "black_carbon_pm2_5_corrected_{}.json",
    "raw_gcs_file_uri": "raw/black_carbon_pm2_5_corrected/"
                        f"{constant.CURRENT_DATE}/"
                        "black_carbon_pm2_5_corrected_{}.json",

  },
  "carbon_monoxide": {
    "data_source": "aqs",
    "param": "42101",
    "layer_name": "carbon_monoxide",
    "layer_url": "https://aqs.epa.gov/data/api/sampleData/byState?email="
                 + constant.AQS_EMAIL + "&key=" + constant.AQS_KEY +
                 "&param=42101&bdate={}&edate={}&state=36",
    "parsed_gcs_file_uri": "parsed/carbon_monoxide/"
                           f"{constant.CURRENT_DATE}/"
                           "carbon_monoxide_{}.json",
    "raw_gcs_file_uri": "raw/carbon_monoxide/"
                        f"{constant.CURRENT_DATE}/"
                        "carbon_monoxide_{}.json",
  },
  "formaldehyde": {
    "data_source": "aqs",
    "param": "43502",
    "layer_name": "formaldehyde",
    "layer_url": "https://aqs.epa.gov/data/api/sampleData/byState?email="
                 + constant.AQS_EMAIL + "&key=" + constant.AQS_KEY +
                 "&param=43502&bdate={}&edate={}&state=36",
    "parsed_gcs_file_uri": "parsed/formaldehyde/"
                           f"{constant.CURRENT_DATE}/"
                           "formaldehyde_{}.json",
    "raw_gcs_file_uri": "raw/formaldehyde/"
                        f"{constant.CURRENT_DATE}/"
                        "formaldehyde_{}.json",
  },
  "nitric_oxide": {
    "data_source": "aqs",
    "param": "42601",
    "layer_name": "nitric_oxide",
    "layer_url": "https://aqs.epa.gov/data/api/sampleData/byState?email="
                 + constant.AQS_EMAIL + "&key=" + constant.AQS_KEY +
                 "&param=42601&bdate={}&edate={}&state=36",
    "parsed_gcs_file_uri": "parsed/nitric_oxide/"
                           f"{constant.CURRENT_DATE}/"
                           "nitric_oxide_{}.json",
    "raw_gcs_file_uri": "raw/nitric_oxide/"
                        f"{constant.CURRENT_DATE}/"
                        "nitric_oxide_{}.json",
  },
  "nitrogen_dioxide": {
    "data_source": "aqs",
    "param": "42602,42603",
    "layer_name": "nitrogen_dioxide",
    "layer_url": "https://aqs.epa.gov/data/api/sampleData/byState?email="
                 + constant.AQS_EMAIL + "&key=" + constant.AQS_KEY +
                 "&param=42602,42603&bdate={}&edate={}&state=36",
    "parsed_gcs_file_uri": "parsed/nitrogen_dioxide/"
                           f"{constant.CURRENT_DATE}/"
                           "nitrogen_dioxide_{}.json",
    "raw_gcs_file_uri": "raw/nitrogen_dioxide/"
                        f"{constant.CURRENT_DATE}/"
                        "nitrogen_dioxide_{}.json",
  },
  "ozone": {
    "data_source": "aqs",
    "param": "44201",
    "layer_name": "ozone",
    "layer_url": "https://aqs.epa.gov/data/api/sampleData/byState?email="
                 + constant.AQS_EMAIL + "&key=" + constant.AQS_KEY +
                 "&param=44201&bdate={}&edate={}&state=36",
    "parsed_gcs_file_uri": "parsed/ozone/"
                           f"{constant.CURRENT_DATE}/"
                           "ozone_{}.json",
    "raw_gcs_file_uri": "raw/ozone/"
                        f"{constant.CURRENT_DATE}/"
                        "ozone_{}.json",
  },

  "pm_25": {
    "data_source": "aqs",
    "param": "88101,88502",
    "layer_name": "pm_25",
    "layer_url": "https://aqs.epa.gov/data/api/sampleData/byState?email="
                 + constant.AQS_EMAIL + "&key=" + constant.AQS_KEY +
                 "&param=88101,88502&bdate={}&edate={}&state=36",
    "parsed_gcs_file_uri": "parsed/pm_25/"
                           f"{constant.CURRENT_DATE}/"
                           "pm_25_{}.json",
    "raw_gcs_file_uri": "raw/pm_25/"
                        f"{constant.CURRENT_DATE}/"
                        "pm_25_{}.json",
  },

  "sulfur_dioxide": {
    "data_source": "aqs",
    "param": "42401",
    "layer_name": "sulfur_dioxide",
    "layer_url": "https://aqs.epa.gov/data/api/sampleData/byState?email="
                 + constant.AQS_EMAIL + "&key=" + constant.AQS_KEY +
                 "&param=42401&bdate={}&edate={}&state=36",
    "parsed_gcs_file_uri": "parsed/sulfur_dioxide/"
                           f"{constant.CURRENT_DATE}/"
                           "sulfur_dioxide_{}.json",
    "raw_gcs_file_uri": "raw/sulfur_dioxide/"
                        f"{constant.CURRENT_DATE}/"
                        "sulfur_dioxide_{}.json",
  },
  "ethane": {
    "data_source": "aqs",
    "param": "43202",
    "layer_name": "ethane",
    "layer_url": "https://aqs.epa.gov/data/api/sampleData/byState?email="
                 + constant.AQS_EMAIL + "&key=" + constant.AQS_KEY +
                 "&param=43202&bdate={}&edate={}&state=36",
    "parsed_gcs_file_uri": "parsed/ethane/"
                           f"{constant.CURRENT_DATE}/"
                           "ethane_{}.json",
    "raw_gcs_file_uri": "raw/ethane/"
                        f"{constant.CURRENT_DATE}/"
                        "ethane_{}.json",
  },
  "toxics_and_carbonyls": {
    "data_source": "aqs",
    "param": "45201,45202,45203,45204,45109",
    "layer_name": "toxics_and_carbonyls",
    "layer_url": "https://aqs.epa.gov/data/api/sampleData/byState?email="
                 + constant.AQS_EMAIL + "&key=" + constant.AQS_KEY +
                 "&param=45201,45202,45203,"
                 "45204,45109&bdate={}&edate={}&state=36",
    "parsed_gcs_file_uri": "parsed/toxics_and_carbonyls/"
                           f"{constant.CURRENT_DATE}/"
                           "toxics_and_carbonyls_{}.json",
    "raw_gcs_file_uri": "raw/toxics_and_carbonyls/"
                        f"{constant.CURRENT_DATE}/"
                        "toxics_and_carbonyls_{}.json",
  }
}
