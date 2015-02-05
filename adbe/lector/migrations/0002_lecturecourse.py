# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
        ('lector', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LectureCourse',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('course', models.ForeignKey(to='course.Course')),
                ('lecture', models.ForeignKey(to='lector.Lecture')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
