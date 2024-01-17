-- Retrieves the 'id' and 'name' of all cities in California from the database 'hbtn_0d_usa'.
-- The results are ordered by ascending 'cities.id'.
SELECT `id`, `name`
  FROM `cities`
 WHERE `state_id` IN
       (SELECT `id`
	  FROM `states`
	 WHERE `name` = "California")
 ORDER BY `id`;
