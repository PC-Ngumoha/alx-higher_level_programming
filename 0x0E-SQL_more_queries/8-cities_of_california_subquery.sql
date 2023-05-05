-- 8-cities_of_california_subquery.sql
-- Creates a script that lists all cities of the state of 'California'
SELECT id, name 
FROM cities
WHERE state_id = (
SELECT id
FROM states
WHERE name = 'California'
);
