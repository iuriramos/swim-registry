# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-19 21:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registry', '0046_auto_20170619_1801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='implementation_maturity',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='services', to='registry.ImplementationMaturityCategory', verbose_name='implementation maturity'),
        ),
        migrations.AlterField(
            model_name='service',
            name='implementation_status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='services', to='registry.ImplementationStatusCategory', verbose_name='implementation status'),
        ),
        migrations.AlterField(
            model_name='service',
            name='version_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='services', to='registry.VersionCategory', verbose_name='version category'),
        ),
    ]
