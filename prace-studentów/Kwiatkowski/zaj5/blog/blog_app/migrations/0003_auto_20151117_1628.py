# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0002_auto_20151117_1623'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Posts',
            new_name='BlogPost',
        ),
        migrations.AlterModelTable(
            name='blogpost',
            table='blog_post',
        ),
    ]
