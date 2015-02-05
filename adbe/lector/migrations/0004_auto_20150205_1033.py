# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_auto_20150205_0224'),
        ('lector', '0003_auto_20150205_0224'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lecturecourse',
            name='course',
        ),
        migrations.RemoveField(
            model_name='lecturecourse',
            name='lecture',
        ),
        migrations.DeleteModel(
            name='LectureCourse',
        ),
        migrations.RemoveField(
            model_name='lecture',
            name='resource',
        ),
        migrations.RemoveField(
            model_name='lecture',
            name='semester',
        ),
        migrations.AddField(
            model_name='lecture',
            name='course',
            field=models.ForeignKey(to='course.Course', default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lecture',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 2, 5, 10, 32, 43, 778981, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lecture',
            name='name',
            field=models.CharField(max_length=255, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lecture',
            name='path',
            field=models.CharField(max_length=255, default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='lecture',
            name='lector',
            field=models.ForeignKey(unique=True, to='lector.Lector'),
            preserve_default=True,
        ),
    ]
