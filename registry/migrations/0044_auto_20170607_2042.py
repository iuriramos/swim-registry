# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-07 23:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registry', '0043_auto_20170601_2304'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='workflow',
        ),
        migrations.RemoveField(
            model_name='service',
            name='technical_interface',
        ),
        migrations.RemoveField(
            model_name='service',
            name='workflow',
        ),
        migrations.RemoveField(
            model_name='technicalinterface',
            name='infrastructure_description',
        ),
        migrations.AddField(
            model_name='infrastructuredescription',
            name='technical_interface',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='infrastructure_description', to='registry.TechnicalInterface', verbose_name='technical interface'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='technicalinterface',
            name='service',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='technical_interface', to='registry.Service', verbose_name='service'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='workflow',
            name='service',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='workflow', to='registry.Service', verbose_name='service'),
            preserve_default=False,
        ),
    ]
