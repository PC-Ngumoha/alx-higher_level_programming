-- 101-avg_temperatures.sql
-- Displays a list of the average temperatures from the `temperature` table
SELECT city, AVG(value) AS avg_temp
FROM temperatures
WHERE month = 7 OR month = 8
GROUP BY city
ORDER BY AVG(value) DESC
LIMIT 3;
