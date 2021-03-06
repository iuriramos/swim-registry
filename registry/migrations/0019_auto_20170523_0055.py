# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-23 03:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registry', '0018_auto_20170523_0023'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='technicalinterfacebindingdescription',
            options={'verbose_name': 'technical interface binding'},
        ),
        migrations.AlterModelOptions(
            name='technicalinterfacebindingprofile',
            options={'verbose_name': 'technical interface binding'},
        ),
        migrations.AlterField(
            model_name='technicalinterface',
            name='version',
            field=models.CharField(blank=True, default=None, max_length=50),
            preserve_default=False,
        ),
    ]
