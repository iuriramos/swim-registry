# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-07 23:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0020_auto_20170607_2048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='organization',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='community.Participant', verbose_name='organization'),
        ),
    ]
