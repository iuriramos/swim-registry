# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-24 02:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registry', '0029_auto_20170523_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataexchangeformatapplication',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='dataexchangeformatservice',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='endpoint',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='technicalinterfacebindingdescription',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='technicalinterfacebindingprofile',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
