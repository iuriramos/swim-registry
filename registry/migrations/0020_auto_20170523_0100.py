# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-23 04:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registry', '0019_auto_20170523_0055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='technicalinterface',
            name='description',
            field=models.TextField(blank=True, default=None),
            preserve_default=False,
        ),
    ]
