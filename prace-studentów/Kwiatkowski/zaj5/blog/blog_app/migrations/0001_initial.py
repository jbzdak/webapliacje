# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('text', models.TextField()),
                ('posted_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'posts',
            },
        ),
    ]
