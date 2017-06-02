# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-01 14:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registry', '0035_remove_workflow_approved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workflow',
            name='previous_node',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='registry.Workflow', verbose_name='previous node'),
        ),
    ]
