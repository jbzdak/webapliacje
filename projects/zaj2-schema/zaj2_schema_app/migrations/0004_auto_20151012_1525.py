# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zaj2_schema_app', '0003_auto_20151012_1417'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='courseinstance',
            table='course_instance',
        ),
        migrations.AlterModelTable(
            name='lecturer',
            table='lecturer',
        ),
        migrations.AlterModelTable(
            name='room',
            table='room',
        ),
    ]
