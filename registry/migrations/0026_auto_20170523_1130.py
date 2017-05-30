# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-23 14:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registry', '0025_auto_20170523_1129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='technical_interface',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='service', to='registry.TechnicalInterface'),
        ),
        migrations.AlterField(
            model_name='service',
            name='workflow',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='service', to='registry.Workflow'),
        ),
    ]