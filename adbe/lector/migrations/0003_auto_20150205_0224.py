# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_auto_20150205_0224'),
        ('lector', '0002_lecturecourse'),
    ]

    operations = [
        migrations.CreateModel(
            name='LectorCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('course', models.ForeignKey(to='course.Course')),
                ('lector', models.ForeignKey(to='lector.Lector')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='semester',
            field=models.IntegerField(choices=[(1, 'I'), (2, 'II'), (3, 'III'), (4, 'IV'), (5, 'V'), (6, 'VI'), (7, 'VII'), (8, 'VIII')]),
            preserve_default=True,
        ),
    ]
