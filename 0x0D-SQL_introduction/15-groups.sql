-- 15-groups.sql
-- Returns the number of records with the same scores
SELECT score, COUNT(score) AS number
FROM second_table
GROUP BY score
ORDER BY COUNT(score) DESC;
