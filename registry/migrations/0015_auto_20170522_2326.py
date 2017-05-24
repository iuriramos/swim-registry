# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-23 02:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registry', '0014_auto_20170522_2200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='technicalinterface',
            name='infrastructure_reference_documents',
            field=models.ManyToManyField(null=True, related_name='technical_interfaces', to='registry.InfrastructureReferenceDocument'),
        ),
    ]
