# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zaj2_schema_app', '0002_auto_20151008_1010'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseInstance',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('year', models.PositiveIntegerField()),
                ('time_from', models.TimeField()),
                ('time_to', models.TimeField()),
                ('course', models.ForeignKey(to='zaj2_schema_app.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Lecturer',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('room_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='courseinstance',
            name='lecturer',
            field=models.ForeignKey(to='zaj2_schema_app.Lecturer'),
        ),
        migrations.AddField(
            model_name='courseinstance',
            name='room',
            field=models.ForeignKey(to='zaj2_schema_app.Room'),
        ),
        migrations.AddField(
            model_name='course',
            name='lecturers',
            field=models.ManyToManyField(to='zaj2_schema_app.Course', through='zaj2_schema_app.CourseInstance', related_name='courses'),
        ),
        migrations.AddField(
            model_name='course',
            name='rooms',
            field=models.ManyToManyField(to='zaj2_schema_app.Room', through='zaj2_schema_app.CourseInstance', related_name='rooms'),
        ),
    ]
