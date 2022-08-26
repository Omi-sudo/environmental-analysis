"""
arcgis_parsing_sample_data_test.py Module
This module contains sample data required to execute unit test cases
"""

geometry_data = {
        "features": [
            {
                "attributes": {
                    "DEC_ID": "0-9999-00075",
                    "FACILITY_NAME": "CAYUGA SALT MINE",
                    "MOREINFO": "https://www.dec.ny.gov/chemical/8569.html",
                    "NYTME_COORDINATE": 374213,
                    "OBJECTID": 7264048,
                },
                "geometry": {
                    "spatialReference": {"latestWkid": 26918, "wkid": 26918},
                    "x": 374213,
                    "y": 4710099,
                },
            }
        ],
        "fields": [
            {
                "alias": "OBJECTID",
                "defaultValue": None,
                "domain": None,
                "name": "OBJECTID",
                "sqlType": "sqlTypeOther",
                "type": "esriFieldTypeOID",
            }
        ],
        "geometryType": "esriGeometryPoint",
        "globalIdFieldName": "",
        "objectIdFieldName": "OBJECTID",
        "spatialReference": {"latestWkid": 26918, "wkid": 26918},
    }

geometry_rings_data = {
        "features": [
            {
                "attributes": {
                    "CITY": "UPTON",
                    "NAME": "BROOKHAVEN NATIONAL LABORATORY - WASTE "
                            "MANAGEMENT FACILITY",
                    "OBJECTID_1": 1,
                    "STATE": "NY",
                    "STREET1": "53 BELL AVE",
                    "STREET2": " ",
                    "Shape__Area": 17822344.1894531,
                    "Shape__Length": 16429.3896057846,
                    "ZIP": 11973,
                },
                "geometry": {
                    "rings": [
                        [
                            [678269.794900001, 4528654.6837],
                            [681162.560300001, 4528796.0595],
                        ]
                    ],
                    "spatialReference": {"latestWkid": 26918, "wkid": 26918},
                },
            }
        ],
        "fields": [
            {
                "alias": "OBJECTID_1",
                "defaultValue": None,
                "domain": None,
                "name": "OBJECTID_1",
                "sqlType": "sqlTypeOther",
                "type": "esriFieldTypeOID",
            }
        ],
        "geometryType": "esriGeometryPolygon",
        "globalIdFieldName": "",
        "objectIdFieldName": "OBJECTID_1",
        "spatialReference": {"latestWkid": 26918, "wkid": 26918},
    }

parsed_data = [{
                    "DEC_ID": "0-9999-00075",
                    "FACILITY_NAME": "CAYUGA SALT MINE",
                    "MOREINFO": "https://www.dec.ny.gov/chemical/8569.html",
                    "NYTME_COORDINATE": 374213,
                    "OBJECTID": 7264048,
              },
{
                    "DEC_ID": "0-9999-00075",
                    "FACILITY_NAME": "CAYUGA SALT MINE",
                    "MOREINFO": "https://www.dec.ny.gov/chemical/8569.html",
                    "NYTME_COORDINATE": 374213,
                    "OBJECTID": 7264048,
              }
]

