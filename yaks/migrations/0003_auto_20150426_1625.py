# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yaks', '0002_auto_20150426_0224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='time',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='yak',
            name='time',
            field=models.TimeField(),
        ),
    ]
