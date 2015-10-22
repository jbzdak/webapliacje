# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zaj2_schema_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='course',
            table='course',
        ),
        migrations.AlterModelTable(
            name='mark',
            table='mark',
        ),
        migrations.AlterModelTable(
            name='student',
            table='student',
        ),
    ]
