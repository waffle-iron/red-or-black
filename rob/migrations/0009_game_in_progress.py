# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-04 12:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rob', '0008_selection_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='in_progress',
            field=models.BooleanField(default=True),
        ),
    ]