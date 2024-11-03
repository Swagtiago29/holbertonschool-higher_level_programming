-- lists all shows contained in hbtn_0d_tvshows that have at least one genre linked
SELECT title, tv_show_genres.genre_id FROM tvshows
JOIN tv_show_genres ON tvshows.id = tv_show_genres.tv_show_id
ORDER BY title ASC, tv_show_genres.genre_id ASC;