# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-23 01:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registry', '0047_auto_20170619_1813'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reviewrequestservice',
            name='service',
        ),
        migrations.RemoveField(
            model_name='reviewrequestservice',
            name='workflow',
        ),
        migrations.RemoveField(
            model_name='workflow',
            name='author',
        ),
        migrations.RemoveField(
            model_name='workflow',
            name='new_state',
        ),
        migrations.RemoveField(
            model_name='workflow',
            name='old_state',
        ),
        migrations.RemoveField(
            model_name='workflow',
            name='previous_node',
        ),
        migrations.RemoveField(
            model_name='workflow',
            name='service',
        ),
        migrations.DeleteModel(
            name='ReviewRequestService',
        ),
        migrations.DeleteModel(
            name='Workflow',
        ),
    ]
