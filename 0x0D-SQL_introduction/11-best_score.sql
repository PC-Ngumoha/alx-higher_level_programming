-- 11-best_score.sql
-- List the records with 'score' >= 10 from highest score to lowest score
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
