# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-23 14:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registry', '0022_auto_20170523_1111'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='technicalinterface',
            name='infrastructure_description',
        ),
        migrations.AddField(
            model_name='infrastructuredescription',
            name='technical_interface',
            field=models.OneToOneField(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, related_name='infrastructure_description', to='registry.InfrastructureDescription'),
            preserve_default=False,
        ),
    ]
