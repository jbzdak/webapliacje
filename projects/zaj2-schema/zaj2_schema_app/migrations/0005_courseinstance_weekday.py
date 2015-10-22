# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zaj2_schema_app', '0004_auto_20151012_1525'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseinstance',
            name='weekday',
            field=models.PositiveSmallIntegerField(default=0),
            preserve_default=False,
        ),
    ]
