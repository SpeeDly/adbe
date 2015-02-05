# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
        ('lector', '0002_lecturecourse'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('description', models.TextField()),
                ('created', models.DateTimeField(auto_now=True, auto_now_add=True)),
                ('expired', models.DateTimeField(auto_now=True)),
                ('course', models.ForeignKey(to='course.Course')),
                ('lector', models.ForeignKey(to='lector.Lector')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
