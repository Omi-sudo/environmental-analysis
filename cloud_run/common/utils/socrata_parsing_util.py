"""
socrata_parsing_util.py module
This module will perform the parsing of input raw data into the desired parsed
format
"""
import sys
import json
import logging

logging.basicConfig(level=logging.INFO)


def parse_geometry_coordinates_mutlipolygon_data(data):
  """
    This function will read and parse/transform the input
    raw data fetched from the SODA_API.
    :param data: Input Raw SODA_API data.
    :return: Transformed/Parsed data in the below format
    [<some_other Key value pairs>,geo_metadata": (((<value1>
    <value2>)))
    ,<some_other Key value pairs>,.....,...}]

  """
  try:
    # Iterating through the rows in data
    for rows in data:
      for key, values in rows.items():
        # Checking if key the_geom is present in data
        if key == "the_geom":
          x3 = []
          # Iterating through the coordinate values
          for coordinategrandparent in values["coordinates"]:
            x1 = ()
            x2 = []
            for coordinateparent in coordinategrandparent:
              for child in coordinateparent:
                x = []
                x.append(child[0])
                # collecting all y values and inserting into empty list
                x.append(child[1])
                var_1 = tuple(x)
                var_1 = " ".join(map(str, var_1))
                x1 = x1 + (var_1,)
            x2.append(tuple(x1))
            x3.append(tuple(x2))

          x4 = "MULTIPOLYGON" + str(tuple(x3))
          x4 = x4.replace("'),", "')")
          x4 = x4.replace("'", "")
          x4 = x4.replace(")),)", ")))")
          rows["geo_metadata"] = rows.pop("the_geom")
          rows["geo_metadata"] = x4
    return json.dumps(data, indent=4)



  except Exception as exception:
    logging.error("An exception occurred in "
                  "[parse_geometry_coordinates_mutlipolygon_data]")
    logging.error("Exception occurred due to %s", str(exception))
    sys.exc_info()
    raise exception
def parse_geometry_coordinates_point_data(data):
  """
    This function will read and parse/transform the input
    raw data fetched from the
    SODA_API.
    :param data: Input Raw SODA_API data.
    :return: Transformed/Parsed data in the below format
    [<some_other Key value pairs>,"geo_metadata":
     {"coordinates": ["<some values>"
    ,"<some values>",.....,...],"type": "<some values>"}] or

  """
  try:
    # Iterating through the rows in data
    for rows in data:
      # Iterating through the rows in data
      for i in list(rows):
        # Checking if key starts with ":@"
        # and removing prefix ":@" from that key.
        if i.startswith(":@"):
          new_key = i[2:]
          rows[new_key] = rows.pop(i)

      for key, values in rows.items():
        # Checking if key the_geom or georeference is present in rows.items
        if key in ("georeference", "the_geom"):
          type_of_data = rows[key]["type"]
          x = []
          y = []
          x.append(values["coordinates"][0])
          y.append(values["coordinates"][1])
          rows[key]["coordinates"] = {
                        "x": x,
                        "y": y
          }
          rows[key]["type"] = type_of_data

        if key == "additional_information":
          rows["additional_information"] = rows[key]["url"]

        if key == "georeference":
          rows["geo_metadata"] = rows.pop("georeference")
        elif key == "the_geom":
          rows["geo_metadata"] = rows.pop("the_geom")

    return json.dumps(data, indent=4)


  except Exception as exception:
    logging.error("An exception occurred in "
                  "[parse_geometry_coordinates_point_data]")
    logging.error("Exception occurred due to %s", str(exception))
    sys.exc_info()
    raise exception


def parse_human_address_data(data):
  """
    This function will read and parse/transform
    the input raw data fetched from the
    SODA_API.
    :param data: Input Raw SODA_API data.
    :return: Transformed/Parsed data in the below format
    [<some_other Key value pairs>,"geo_metadata":
    {"human_address":{key:value, key values...}]
  """
  try:
    # Iterating through the rows in data
    for rows in data:
      # Iterating through the rows in data
      for i in list(rows):
        # Checking if key starts with ":@"
        # and removing prefix ":@" from that key.
        if i.startswith(":@"):
          new_key = i[2:]
          rows[new_key] = rows.pop(i)

      for key, values in rows.items():
        # Checking if key geocoded_column is present in row.items
        if key == "geocoded_column":
          for row in [values]:
            for key1, values1 in row.items():
              # Checking if key the_human_address is present in row.items
              if key1 == "human_address":
                human_address = json.loads(values1)
                row["human_address"] = human_address
                rows[key] = row
          rows["geo_metadata"] = rows.pop("geocoded_column")
        # Checking if key location_1 is present in row.items
        elif key == "location_1":
          for row in [values]:
            for key1, values1 in row.items():
              if key1 == "human_address":
                human_address = json.loads(values1)
                row["human_address"] = human_address
                rows[key] = row
          rows["geo_metadata"] = rows.pop("location_1")

    return json.dumps(data, indent=4)

  except Exception as exception:
    logging.error("An exception occurred in [parse_human_address_data]")
    logging.error("Exception occurred due to %s", str(exception))
    sys.exc_info()
    raise exception

def prefix_check(data):
  """
      This function will read and remove the additional
      prefix from input raw data fetched from the
      SODA_API.Also replace key "facility_location" with
      "geo_metadata"
      :param data: Input Raw SODA_API data.
      :return: Transformed data with
    """
  try:
    for rows in data:
      # Checking if key starts with ":@" and removing prefix ":@" from that key.
      for i in list(rows):
        if i.startswith(":@"):
          new_key = i[2:]
          rows[new_key] = rows.pop(i)

      for key, values in rows.items():
        if key == "facility_location":
          rows["geo_metadata"] = values
          rows["geo_metadata"] = rows.pop("facility_location")

    return json.dumps(data, indent=4)

  except Exception as exception:
    logging.error("An exception occurred in [prefix_check]")
    logging.error("Exception occurred due to %s", str(exception))
    sys.exc_info()
    raise exception
