-- Retrieves the 'title' and 'genre_id' of all shows in the 'hbtn_0d_tvshows' database.
-- Displays NULL for shows without genres. Records are ordered by ascending 'tv_shows.title' and 'tv_show_genres.genre_id'.
SELECT s.`title`, g.`genre_id`
  FROM `tv_shows` AS s
       LEFT JOIN `tv_show_genres` AS g
       ON s.`id` = g.`show_id`
 ORDER BY s.`title`, g.`genre_id`;
