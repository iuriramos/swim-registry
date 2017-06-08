# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-07 23:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0018_auto_20170607_2047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='following_services',
            field=models.ManyToManyField(blank=True, related_name='followers', to='registry.Service', verbose_name='following services'),
        ),
    ]
