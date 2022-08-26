MERGE
 `reporting.aqs_nitric_oxide` AS destination
USING
 (
 SELECT
   cbsa_code AS cbsa_code,
   state AS state,
   state_code AS state_code,
   county AS county,
   county_code AS county_code,
   site_number AS site_number,
   qualifier AS qualifier,
   uncertainty AS uncertainty,
   detection_limit AS detection_limit,
   units_of_measure AS units_of_measure,
   sample_duration AS sample_duration,
   sample_measurement AS sample_measurement,
   datum AS datum,
   latitude AS latitude,
   longitude AS longitude,
   ST_GeogPoint(longitude,latitude) AS geometry,
   sample_frequency AS sample_frequency,
   units_of_measure_code AS units_of_measure_code,
   poc AS poc,
   parameter_code AS parameter_code,
   sample_duration_code AS sample_duration_code,
   parameter AS parameter,
   method AS method,
   method_code AS method_code,
   method_type AS method_type,
   CAST(date_local AS DATE) AS date_local,
   time_local AS time_local,
   CAST(date_gmt AS DATE) AS date_gmt,
   time_gmt AS time_gmt,
   CAST(date_of_last_change AS DATE) AS date_of_last_change,
   CAST(date_of_last_change AS DATE) AS record_date,
   ingestion_timestamp
 FROM
   `warehouse.aqs_nitric_oxide`
 WHERE
   ingestion_timestamp = ingestion_time_ts ) AS source
ON
 destination.state = source.state
 AND destination.county = source.county
 AND destination.site_number = source.site_number
 AND destination.poc = source.poc
 AND destination.parameter_code = source.parameter_code
 AND destination.sample_duration_code = source.sample_duration_code
 AND destination.date_local = source.date_local
 AND destination.time_local = source.time_local
 WHEN MATCHED THEN UPDATE SET destination.cbsa_code = source.cbsa_code, destination.state_code=source.state_code, destination.county_code = source.county_code, destination.qualifier = source.qualifier, destination.uncertainty = source.uncertainty, destination.detection_limit = source.detection_limit, destination.units_of_measure=source.units_of_measure, destination.sample_duration = source.sample_duration, destination.sample_measurement = source.sample_measurement, destination.datum = source.datum, destination.latitude = source.latitude, destination.longitude=source.longitude,destination.geometry=source.geometry, destination.sample_frequency = source.sample_frequency, destination.units_of_measure_code = source.units_of_measure_code, destination.parameter = source.parameter, destination.method = source.method, destination.method_code=source.method_code, destination.method_type=source.method_type, destination.date_gmt=source.date_gmt, destination.time_gmt=source.time_gmt, destination.date_of_last_change=source.date_of_last_change, destination.record_date=source.record_date, destination.ingestion_timestamp=source.ingestion_timestamp
 WHEN NOT MATCHED
 THEN
INSERT
 ( cbsa_code,
   state,
   state_code,
   county,
   county_code,
   site_number,
   qualifier,
   uncertainty,
   detection_limit,
   units_of_measure,
   sample_duration,
   sample_measurement,
   datum,
   latitude,
   longitude,
   geometry,
   sample_frequency,
   units_of_measure_code,
   poc,
   parameter_code,
   sample_duration_code,
   parameter,
   method,
   method_code,
   method_type,
   date_local,
   time_local,
   date_gmt,
   time_gmt,
   date_of_last_change,
   record_date,
   ingestion_timestamp)
VALUES
 ( source.cbsa_code, source.state, source.state_code, source.county, source.county_code, source.site_number, source.qualifier, source.uncertainty, source.detection_limit, source.units_of_measure, source.sample_duration, source.sample_measurement, source.datum, source.latitude, source.longitude, source.geometry, source.sample_frequency, source.units_of_measure_code, source.poc, source.parameter_code, source.sample_duration_code, source.parameter, source.method, source.method_code, source.method_type, source.date_local, source.time_local, source.date_gmt, source.time_gmt, source.date_of_last_change, source.record_date, source.ingestion_timestamp);


