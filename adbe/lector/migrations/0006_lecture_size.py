# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lector', '0005_auto_20150205_1037'),
    ]

    operations = [
        migrations.AddField(
            model_name='lecture',
            name='size',
            field=models.CharField(max_length=255, default='30MB'),
            preserve_default=False,
        ),
    ]
