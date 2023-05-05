-- 9-cities_by_state_join.sql
-- Lists all the cities on the database with their corresponding state name
SELECT cities.id, cities.name, states.name
FROM cities
INNER JOIN states
ON cities.state_id = states.id
ORDER BY cities.id ASC;
