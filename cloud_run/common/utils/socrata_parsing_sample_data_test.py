"""
socrata_parsing_sample_data_test.py Module
This module contains sample data required to execute unit test cases
"""
human_address_data = [{
      ":@computed_region_92fq_4b7q": "45",
      ":@computed_region_efsh_h5xi": "18184",
      ":@computed_region_f5dn_yrer": "21",
      ":@computed_region_sbqj_enih": "35",
      ":@computed_region_yeji_bk3q": "2",
      "bbl": "3069900001",
      "bin": "3188417",
      "borough": "Brooklyn",
      "census_tract": "348",
      "community_board": "13",
      "council_district": "47",
      "cross_streets": "W. 22nd St. & W. 23rd St.",
      "facility_name": "Ida G. Israel Community Health Center",
      "facility_type": "Child Health Center",
      "latitude": "40.578468",
      "location_1": {
         "human_address": "{\"address\": \"2201 Neptune Avenue\", "
                          "\"city\": \"Brooklyn\", \"state\": "
                          "\"NY\", \"zip\": \"11224\"}",
         "latitude": "40.578488319967",
         "longitude": "-73.989497148121"
      },
      "longitude": "-73.989614",
      "nta": "Seagate-Coney Island",
      "phone": "718-946-3400",
      "postcode": "11224"
   }]


multipolygon_data =[
    {
        "acquisitio": "19530514000000.00000",
        "acres": "0.061",
        "borough": "Q",
        "class": "PARK",
        "commission": "20090423000000.00000",
        "communityb": "401",
        "councildis": "22",
        "department": "Q-01",
        "eapply": "Strippoli Square",
        "gisobjid": "100000375",
        "gispropnum": "Q355",
        "global_id": "{62700020-4840-4F4A-A15A-7D65B9A6A794}",
        "jurisdicti": "DPR",
        "location": "31 Ave., 51 St., 54 St.",
        "mapped": "True",
        "name311": "Strippoli Square",
        "nys_assemb": "30",
        "nys_senate": "12",
        "objectid": "5916",
        "omppropid": "Q355",
        "parentid": "Q-01",
        "permit": "Y",
        "permitdist": "Q-01",
        "permitpare": "Q-01",
        "pip_ratabl": "Yes",
        "precinct": "114",
        "retired": "False",
        "signname": "Strippoli Square",
        "subcategor": "Sitting Area/Triangle/Mall",
        "the_geom": {
            "coordinates": [
                [
                    [
                        [
                            -73.90748556731788,
                            40.75708917875267
                        ],
                        [
                            -73.90767966215755,
                            40.757071748493715
                        ],
                        [
                            -73.90757282834349,
                            40.757356495426514
                        ],
                        [
                            -73.90754040000033,
                            40.75736019659576
                        ],
                        [
                            -73.90748556731788,
                            40.75708917875267
                        ]
                    ]
                ]
            ],
            "type": "MultiPolygon"
        },
        "typecatego": "Triangle/Plaza",
        "url": "http://www.nycgovparks.org/parks/Q355/",
        "us_congres": "14",
        "waterfront": "No",
        "zipcode": "11377"
    }]

point_data = [
    {
        "bbl": "5045000015",
        "bin": "5061034.0",
        "city": "Staten Island",
        "housenum": "15",
        "name": "The Tanglewood School",
        "streetname": "TANGLEWOOD DRIVE",
        "the_geom": {
            "coordinates": [
                -74.15167796424373,
                40.567279208874524
            ],
            "type": "Point"
        },
        "url": "http://www.nyc.gov/html/doh/html/dc/dc.shtml",
        "zip": "10308"
    }
]
