# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('street_address', models.CharField(verbose_name='Street address', max_length=100)),
                ('street_no', models.CharField(verbose_name='Street number', max_length=100)),
                ('zip_code', models.CharField(verbose_name='zip-code', max_length=10)),
                ('city', models.CharField(verbose_name='City', max_length=100)),
                ('voivoidship', models.CharField(verbose_name='Voivoidshio', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('pesel', models.CharField(max_length=100)),
            ],
        ),
    ]
