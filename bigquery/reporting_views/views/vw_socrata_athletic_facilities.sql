SELECT
  CAST(accessible AS string) AS accessible,
  CAST(adult_baseball AS STRING) AS adult_baseball,
  CAST(adult_football AS STRING) AS adult_football,
  CAST(adult_softball AS STRING) AS adult_softball,
  CAST(basketball AS STRING) AS basketball,
  CAST(bocce AS STRING) AS bocce,
  borough,
  communityboard,
  councildistrict,
  CAST(cricket AS STRING) AS cricket,
  department,
  dimensions,
  featurestatus,
  field_lighted,
  field_number,
  CAST(flagfootball AS STRING) AS flagfootball,
  CAST(frisbee AS STRING) AS frisbee,
  gispropnum,
  CAST(handball AS STRING) AS handball,
  CAST(hockey AS STRING) AS hockey,
  CAST(kickball AS STRING) AS kickball,
  CAST(lacrosse AS STRING) AS lacrosse,
  CAST(ll_baseb_12andunder AS STRING) AS ll_baseb_12andunder,
  CAST(ll_baseb_13andolder AS STRING) AS ll_baseb_13andolder,
  CAST(ll_softball AS STRING) AS ll_softball,
  CAST(maintenanceagreement AS STRING) AS maintenanceagreement,
  geo_metadata,
  ST_GEOGFROMTEXT(geo_metadata,
    make_valid => TRUE) AS geometry,
  CAST(netball AS STRING) AS netball,
  CAST(nonregulation_soccer AS STRING) AS nonregulation_soccer,
  precinct,
  primary_sport,
  CAST(regulation_soccer AS STRING) AS regulation_soccer,
  CAST(rugby AS STRING) AS rugby,
  starea,
  stlength,
  surface_type,
  system,
  CAST(t_ball AS STRING) AS t_ball,
  CAST(tennis AS STRING) AS tennis,
  CAST(track_and_field AS STRING) AS track_and_field,
  CAST(volleyball AS STRING) AS volleyball,
  CAST(wheelchairfootball AS STRING) AS wheelchairfootball,
  CAST(youth_football AS STRING) AS youth_football,
  zipcode,
  CAST(pickleball AS STRING) AS pickleball,
  record_date,
  ingestion_timestamp
FROM
  `warehouse.socrata_athletic_facilities`