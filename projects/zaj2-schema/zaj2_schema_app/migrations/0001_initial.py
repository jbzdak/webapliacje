# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Mark',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('mark', models.PositiveSmallIntegerField()),
                ('course', models.ForeignKey(to='zaj2_schema_app.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('courses', models.ManyToManyField(db_table='student_course', to='zaj2_schema_app.Course')),
            ],
        ),
        migrations.AddField(
            model_name='mark',
            name='student',
            field=models.ForeignKey(to='zaj2_schema_app.Student'),
        ),
    ]
