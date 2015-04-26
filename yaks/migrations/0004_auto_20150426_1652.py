# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yaks', '0003_auto_20150426_1625'),
    ]

    operations = [
        migrations.AddField(
            model_name='yaklocation',
            name='timezone',
            field=models.TextField(default=5),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='time',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='yak',
            name='time',
            field=models.DateTimeField(),
        ),
    ]
