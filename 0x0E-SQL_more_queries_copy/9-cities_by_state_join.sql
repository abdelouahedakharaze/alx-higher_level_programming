-- Retrieves the 'id' and 'name' of all cities in the database 'hbtn_0d_usa'.
-- The results are joined with the corresponding state names and ordered by ascending 'cities.id'.
SELECT c.`id`, c.`name`, s.`name`
  FROM `cities` AS c
       INNER JOIN `states` AS s
       ON c.`state_id` = s.`id`
 ORDER BY c.`id`;
