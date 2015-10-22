SELECT DISTINCT c1.id, c1.* FROM course_instance c1

 INNER JOIN course_instance c2 ON  c1.id != c2.id AND c1.year = c2.year AND c2.weekday = c1.weekday
      AND c1.room_id = c2.room_id
      AND c2.time_from < c1.time_to and c2.time_to > c1.time_from
