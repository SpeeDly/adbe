# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lector', '0006_lecture_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='lectorcourse',
            name='approver',
            field=models.ForeignKey(null=True, related_name='approver', to='lector.Lector', blank=True),
            preserve_default=True,
        ),
    ]
