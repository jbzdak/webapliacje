Zaj 2: solutions
=================


Q1
--

.. code-block:: sql

SELECT weekday, time_from, time_to FROM course_instance WHERE course_id = 55 AND year = 2015 ORDER BY year, weekday, time_from;
