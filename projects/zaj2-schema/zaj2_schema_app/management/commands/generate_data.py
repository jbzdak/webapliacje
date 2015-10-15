# -*- coding: utf-8 -*-
import datetime

from django.core.management.base import BaseCommand, CommandError
import random
from django.db import transaction

import names


from zaj2_schema_app import models

class Command(BaseCommand):

  def execute(self, *args, **options):

    with transaction.atomic():

      for ii in range(10):
        for jj in ['Projektowanie Webaplikacji', 'Analiza Matematyczna', 'Programowanie Obiektowe']:
          models.Course.objects.create(
            name = "{} {}".format(jj, ii)
          )

      for ii in range(100):
        models.Room.objects.create(
          room_name="Sala {}".format(ii),
          number_of_places=random.randint(5, 15)
        )

      for ii in range(100):
        models.Lecturer.objects.create(
          name = names.get_full_name()
        )

      rooms = models.Room.objects.all()
      lecturers = models.Lecturer.objects.all()
      for year in [2013, 2014, 2015]:
        for course in models.Course.objects.all():
          for ii in range(3):
            date_from = datetime.time(random.randint(8, 18))
            models.CourseInstance.objects.create(
              course = course,
              room = random.choice(rooms),
              lecturer = random.choice(lecturers),
              time_from=date_from,
              time_to = datetime.time(date_from.hour+2),
              year=year,
              weekday = random.randint(0, 7)
            )


      for ii in range(1000):
        student = models.Student.objects.create(
          name = names.get_full_name()
        )

        for jj in range(3):
          student.courses.add(random.choice(models.Course.objects.all()))

        student.save()

      for s in models.Student.objects.all():
        if random.randint(0, 10) != 5:
          for c in s.courses.all():
            for ii in range(10):
              models.Mark.objects.create(
                student = s, course=c,
                mark = random.randint(2, 5)
              )