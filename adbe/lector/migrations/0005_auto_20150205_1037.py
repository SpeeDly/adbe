# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lector', '0004_auto_20150205_1033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecture',
            name='lector',
            field=models.ForeignKey(to='lector.Lector'),
            preserve_default=True,
        ),
    ]
