# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-19 20:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0006_auto_20170519_1731'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='displayable',
            field=models.BooleanField(default=False),
        ),
    ]
