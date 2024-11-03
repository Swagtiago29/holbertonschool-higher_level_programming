-- lists all shows contained in hbtn_0d_tvshows that have at least one genre linked
SELECT title, tv_show_genres.genre_id FROM tvshows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY title ASC, tv_show_genres.genre_id ASC;