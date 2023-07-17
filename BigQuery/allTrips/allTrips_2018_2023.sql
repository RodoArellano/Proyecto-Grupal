CREATE OR REPLACE TABLE `nyc-taxis-and-carbon-emission.trip_records_clean.allTrips_2018_2023`
AS (
  SELECT 
    ROW_NUMBER() OVER(ORDER BY pickup_datetime) - 1 AS trip_id,
    NULL AS vehicle_id,
    DATE(pickup_datetime) AS time_id,
    *
  FROM (
    SELECT * FROM `nyc-taxis-and-carbon-emission.trip_records_clean.greenTrips_2018_2023`
    UNION ALL
    SELECT * FROM `nyc-taxis-and-carbon-emission.trip_records_clean.yellowTrips_2018_2023`
  ) AS combined_trips
  WHERE EXTRACT(YEAR FROM pickup_datetime) BETWEEN 2018 AND 2023
)
ORDER BY trip_id ASC