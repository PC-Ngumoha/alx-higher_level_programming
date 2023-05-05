-- 13-count_shows_by_genre.sql
-- Displays a lists of genres and the number of shows under each genre
SELECT tv_genres.name AS genre, COUNT(tv_show_genres.show_id) AS number_of_shows
FROM tv_genres
LEFT JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
WHERE tv_show_genres.genre_id IS NOT NULL
GROUP BY tv_genres.id
ORDER BY COUNT(tv_show_genres.show_id) DESC;
