# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_auto_20150205_1815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='expire',
            field=models.DateTimeField(),
            preserve_default=True,
        ),
    ]
