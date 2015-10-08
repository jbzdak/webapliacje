# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand, CommandError
import random
from django.db import transaction

import names


from zaj2_schema_app import models

class Command(BaseCommand):

  def execute(self, *args, **options):

    with transaction.atomic():

      for ii in range(3):
        for jj in ['Projektowanie Webaplikacji', 'Analiza Matematyczna', 'Programowanie Obiektowe']:
          models.Course.objects.create(
            name = "{} {}".format(jj, ii)
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