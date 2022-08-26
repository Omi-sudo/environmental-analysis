"""
arcgis_parsing_util.py module
This module will perform the parsing of input raw data into the desired parsed
format
"""
import sys
import json
import logging

from pyproj import Transformer

logging.basicConfig(level=logging.INFO)

p = Transformer.from_crs(26918, 4326)

def parse_geometry_rings_data(data):
  """
  This function will read and parse/transform the input raw data fetched from
  the GIS Data/Feature layer URL.
  :param data: Input Raw GIS Data/Feature layer data
  :return: Transformed/Parsed data in the below format
                    [<some_other Key value pairs>,"geometry":
                    {"rings": ["<some values>",.....,...],
                    "wkid": "<some values>",
                    "latestWkid": "<some values>"}]

    """
  try:

    feature = data["features"]
    data_list = []

    # Iterating through the feature list which contains actual data
    for rows in feature:
      row_data = rows["attributes"]
      geometry = rows["geometry"]
      rings = geometry["rings"]
      # Iterating through the outer most rings list --> [[[value1,value2]]]
      x3 = []
      for itr in range(0, len(rings)):
        x1 = ()
        x2 = []
        # Iterating through the middle rings list --> [[value1,value2]]
        for data_rings in rings[itr]:
          x = []
          data_rings_0, data_rings_1 = p.transform(data_rings[0], data_rings[1])
          x.append(data_rings_1)
          x.append(data_rings_0)
          temp = tuple(x)
          temp = " ".join(map(str, temp))
          x1 = x1 + (temp,)

        x2.append(tuple(x1))
        x3.append(tuple(x2))

      x4 = "MULTIPOLYGON" + str(tuple(x3))
      x4 = x4.replace("'),", "')")
      x4 = x4.replace("'", "")
      x4 = x4.replace(")),)", ")))")

      row_data["geo_metadata"] = x4

      data_list.append(row_data)

    return json.dumps(data_list, indent=4)


  except Exception as exception:
    logging.error("An exception occurred in [parse_geometry_rings_data]")
    logging.error("Exception occurred due to %s", str(exception))
    sys.exc_info()
    raise exception


def parse_geometry_data(data):
  """
    This function will read and parse/transform the input raw data fetched f
    rom the GIS Data/Feature layer URL.

    :param data: Input Raw GIS Data/Feature layer data
    :return: Transformed/Parsed data in the below format
                    [<some_other Key value pairs>,"geometry": {"latestWkid":
                    "<some values>","wkid": "<some values>",
                    "x": "<some values>",
                    "y": "<some values>"}]
    """

  try:

    feature = data["features"]
    data_list = []
    # Iterating through the feature list which contains actual data
    for rows in feature:
      row_data = rows["attributes"]
      # Checking if key geometry is present in data
      if "geometry" in rows.keys():
        row_data["geometry"] = {}
        # Checking if key spatialReference is present in data
        if "spatialReference" in rows["geometry"].keys():
          row_data["geometry"] = rows["geometry"]["spatialReference"]
          # Checking if key x is present in data
          if "x" in rows["geometry"].keys():
            x, y = p.transform(rows["geometry"]["x"], rows["geometry"]["y"])
            row_data["geometry"]["x"] = x
            # Checking if key y is present in data
            if "y" in rows["geometry"].keys():
              row_data["geometry"]["y"] = y
              data_list.append(row_data)

            else:
              data_list.append(row_data)

          else:
            x, y = p.transform(rows["geometry"]["x"], rows["geometry"]["y"])
            if "y" in rows["geometry"].keys():
              row_data["geometry"]["y"] = y
              data_list.append(row_data)
            else:
              data_list.append(row_data)

        else:
          x, y = p.transform(rows["geometry"]["x"], rows["geometry"]["y"])
          if "x" in rows["geometry"].keys():
            row_data["geometry"]["x"] = x
            if "y" in rows["geometry"].keys():
              row_data["geometry"]["y"] = y
              data_list.append(row_data)
            else:
              data_list.append(row_data)
          else:
            if "y" in rows["geometry"].keys():
              row_data["geometry"]["y"] = y
              data_list.append(row_data)
            else:
              data_list.append(row_data)

      else:
        data_list.append(row_data)

    for rows in data_list:
      rows["geo_metadata"] = rows.pop("geometry")

    return json.dumps(data_list, indent=4)


  except Exception as exception:
    logging.error("An exception occurred in [parse_geometry_data]")
    logging.error("Exception occurred due to %s", str(exception))
    sys.exc_info()
    raise exception

def no_parsing(data):
  """
     This function will returns the data
     list from raw data fetched from webservice.

     :param data: Input Raw GIS Data/Feature layer data
     :return: Transformed/Parsed data.
  """
  try:
    data = data["features"]
    data_list = []
    for row in data:
      data_list.append(row["attributes"])
    return json.dumps(data_list, indent=4)

  except Exception as exception:
    logging.error("An exception occurred in [no_parsing]")
    logging.error("Exception occurred due to %s", str(exception))
    sys.exc_info()
    raise exception
