# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-01 12:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registry', '0032_auto_20170601_0937'),
    ]

    operations = [
        migrations.AddField(
            model_name='workflow',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]
