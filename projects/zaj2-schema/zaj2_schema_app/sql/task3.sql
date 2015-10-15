SELECT l.name, crs.name FROM lecturer l
  RIGHT OUTER JOIN course_instance ci ON l.id = ci.lecturer_id
  RIGHT OUTER JOIN course crs ON ci.course_id = crs.id
  ORDER BY crs.name;