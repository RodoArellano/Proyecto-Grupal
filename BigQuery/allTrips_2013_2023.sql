CREATE OR REPLACE TABLE `nyc-taxis-and-carbon-emission.trip_records_clean.allTrips_2013_2023`
AS (
  SELECT 
    ROW_NUMBER() OVER(ORDER BY pickup_datetime) - 1 AS trip_id,
    NULL AS vehicle_id,
    FORMAT_TIMESTAMP('%Y-%m-%d', pickup_datetime) AS time_id,
    *
  FROM (
    SELECT * FROM `nyc-taxis-and-carbon-emission.trip_records_clean.greenTrips_2013_2023`
    UNION ALL
    SELECT * FROM `nyc-taxis-and-carbon-emission.trip_records_clean.yellowTrips_2013_2023`
  ) AS combined_trips
  WHERE EXTRACT(YEAR FROM pickup_datetime) BETWEEN 2013 AND 2023
)
ORDER BY trip_id ASC