CREATE OR REPLACE TABLE `nyc-taxis-and-carbon-emission.trip_records_clean.yellowTrips_2013_2023`
AS
SELECT pickup_datetime, dropoff_datetime, trip_distance, payment_type, pickup_location_id, dropoff_location_id, CAST(total_amount AS NUMERIC) AS total_amount, CAST(tip_amount AS NUMERIC) AS tip_amount
FROM `bigquery-public-data.new_york_taxi_trips.tlc_yellow_trips_2013`
WHERE passenger_count > 0 AND trip_distance > 0 AND total_amount > 0
UNION ALL
SELECT pickup_datetime, dropoff_datetime, trip_distance, payment_type, pickup_location_id, dropoff_location_id, CAST(total_amount AS NUMERIC) AS total_amount, CAST(tip_amount AS NUMERIC) AS tip_amount
FROM `bigquery-public-data.new_york_taxi_trips.tlc_yellow_trips_2014`
WHERE passenger_count > 0 AND trip_distance > 0 AND total_amount > 0
UNION ALL
SELECT pickup_datetime, dropoff_datetime, trip_distance, payment_type, pickup_location_id, dropoff_location_id, CAST(total_amount AS NUMERIC) AS total_amount, CAST(tip_amount AS NUMERIC) AS tip_amount
FROM `bigquery-public-data.new_york_taxi_trips.tlc_yellow_trips_2015`
WHERE passenger_count > 0 AND trip_distance > 0 AND total_amount > 0
UNION ALL
SELECT pickup_datetime, dropoff_datetime, trip_distance, payment_type, pickup_location_id, dropoff_location_id, CAST(total_amount AS NUMERIC) AS total_amount, CAST(tip_amount AS NUMERIC) AS tip_amount
FROM `bigquery-public-data.new_york_taxi_trips.tlc_yellow_trips_2016`
WHERE passenger_count > 0 AND trip_distance > 0 AND total_amount > 0
UNION ALL
SELECT pickup_datetime, dropoff_datetime, trip_distance, payment_type, pickup_location_id, dropoff_location_id, CAST(total_amount AS NUMERIC) AS total_amount, CAST(tip_amount AS NUMERIC) AS tip_amount
FROM `bigquery-public-data.new_york_taxi_trips.tlc_yellow_trips_2017`
WHERE passenger_count > 0 AND trip_distance > 0 AND total_amount > 0
UNION ALL
SELECT pickup_datetime, dropoff_datetime, trip_distance, payment_type, pickup_location_id, dropoff_location_id, CAST(total_amount AS NUMERIC) AS total_amount, CAST(tip_amount AS NUMERIC) AS tip_amount
FROM `bigquery-public-data.new_york_taxi_trips.tlc_yellow_trips_2018`
WHERE passenger_count > 0 AND trip_distance > 0 AND total_amount > 0
UNION ALL
SELECT pickup_datetime, dropoff_datetime, trip_distance, payment_type, pickup_location_id, dropoff_location_id, CAST(total_amount AS NUMERIC) AS total_amount, CAST(tip_amount AS NUMERIC) AS tip_amount
FROM `bigquery-public-data.new_york_taxi_trips.tlc_yellow_trips_2019`
WHERE passenger_count > 0 AND trip_distance > 0 AND total_amount > 0
UNION ALL
SELECT pickup_datetime, dropoff_datetime, trip_distance, payment_type, pickup_location_id, dropoff_location_id, CAST(total_amount AS NUMERIC) AS total_amount, CAST(tip_amount AS NUMERIC) AS tip_amount
FROM `bigquery-public-data.new_york_taxi_trips.tlc_yellow_trips_2020`
WHERE passenger_count > 0 AND trip_distance > 0 AND total_amount > 0
UNION ALL
SELECT pickup_datetime, dropoff_datetime, trip_distance, payment_type, pickup_location_id, dropoff_location_id, CAST(total_amount AS NUMERIC) AS total_amount, CAST(tip_amount AS NUMERIC) AS tip_amount
FROM `bigquery-public-data.new_york_taxi_trips.tlc_yellow_trips_2021`
WHERE passenger_count > 0 AND trip_distance > 0 AND total_amount > 0
UNION ALL
SELECT pickup_datetime, dropoff_datetime, trip_distance, payment_type, pickup_location_id, dropoff_location_id, CAST(total_amount AS NUMERIC) AS total_amount, CAST(tip_amount AS NUMERIC) AS tip_amount
FROM `bigquery-public-data.new_york_taxi_trips.tlc_yellow_trips_2022`
WHERE passenger_count > 0 AND trip_distance > 0 AND total_amount > 0
UNION ALL
SELECT pickup_datetime, dropoff_datetime, trip_distance, payment_type, pickup_location_id, dropoff_location_id, CAST(total_amount AS NUMERIC) AS total_amount, CAST(tip_amount AS NUMERIC) AS tip_amount
FROM `bigquery-public-data.new_york_taxi_trips.tlc_yellow_trips_2023`
WHERE passenger_count > 0 AND trip_distance > 0 AND total_amount > 0