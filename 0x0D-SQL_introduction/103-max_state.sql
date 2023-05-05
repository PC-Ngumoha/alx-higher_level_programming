-- 103-max_state.sql
-- Displays the max temperature value for each state
SELECT state, MAX(value) AS max_temp
FROM temperatures
GROUP BY state
ORDER BY state;
