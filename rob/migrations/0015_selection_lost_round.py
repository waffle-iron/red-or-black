# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-05 18:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rob', '0014_game_previous_colours'),
    ]

    operations = [
        migrations.AddField(
            model_name='selection',
            name='lost_round',
            field=models.IntegerField(blank=True, default=True),
        ),
    ]
