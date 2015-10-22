SELECT
    c.id,
    c.name,
    s.id,
    s.name,
    AVG(m.mark)
  FROM student s

  INNER JOIN student_course cs ON cs.student_id=s.id
  INNER JOIN course c ON c.id = cs.course_id
  LEFT OUTER JOIN mark m ON m.student_id = cs.student_id AND c.id = m.course_id
  GROUP BY c.id, s.id
  ORDER BY s.name, c.name;