-- count genre
SELECT tv_show_genres.title as genre, count(*) as number_of_shows
FROM tv_shows
INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
GROUP BY tv_show_genres.title