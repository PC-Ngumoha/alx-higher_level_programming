-- 16-no_link.sql
-- Lists names and scores by order of descending scores
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
