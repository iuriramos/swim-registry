# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-08 00:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registry', '0044_auto_20170607_2042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workflow',
            name='service',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='workflow', to='registry.Service', verbose_name='service'),
        ),
    ]
