-- list dexter
SELECT tv_shows.tite, count(*) FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
WHERE tv_genres.name = 'Comedy'
GROUP BY tv_shows.tite
HAVING COUNT(*) = 1;