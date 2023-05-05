-- 101-avg_temperatures.sql
-- Displays a list of the average temperatures from the `temperature` table
SELECT city, AVG(value) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY AVG(value) DESC;
