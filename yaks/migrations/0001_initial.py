# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('message_id', models.TextField()),
                ('comment_id', models.TextField(serialize=False, primary_key=True)),
                ('comment', models.TextField()),
                ('time', models.TextField()),
                ('likes', models.IntegerField()),
                ('poster_id', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Yak',
            fields=[
                ('poster_id', models.TextField()),
                ('hide_pin', models.BooleanField()),
                ('message_id', models.TextField(serialize=False, primary_key=True)),
                ('delivery_id', models.TextField(blank=True)),
                ('comments', models.IntegerField()),
                ('time', models.TextField()),
                ('longitude', models.FloatField()),
                ('latitude', models.FloatField()),
                ('likes', models.IntegerField()),
                ('message', models.TextField()),
                ('reyaked', models.BooleanField()),
                ('handle', models.TextField(blank=True)),
                ('type', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='YakLocation',
            fields=[
                ('name', models.TextField(serialize=False, primary_key=True)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
            ],
        ),
        migrations.AddField(
            model_name='yak',
            name='yaklocation',
            field=models.ForeignKey(to='yaks.YakLocation'),
        ),
    ]
