# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-02 01:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import registry.models.service


class Migration(migrations.Migration):

    dependencies = [
        ('registry', '0041_auto_20170601_2131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='registration_status',
            field=models.ForeignKey(default=registry.models.service.Service.get_default_registration_status, on_delete=django.db.models.deletion.CASCADE, related_name='services', to='registry.RegistrationStatusCategory', verbose_name='registration status'),
        ),
    ]
