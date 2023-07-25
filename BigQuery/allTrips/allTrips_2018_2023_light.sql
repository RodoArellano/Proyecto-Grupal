-- Previamente la tabla allTrips_2013_2023_light se crea con la misma Query allTrips_2018_2023
DELETE FROM `trip_records_clean.allTrips_2018_2023_light`
WHERE trip_id IN (
  SELECT trip_id
  FROM (
    SELECT trip_id, ROW_NUMBER() OVER (ORDER BY RAND()) AS row_num
    FROM `trip_records_clean.allTrips_2018_2023_light`
  ) AS subquery
  WHERE row_num > (SELECT 0.5 * COUNT(*) FROM `trip_records_clean.allTrips_2018_2023_light`)
)
