# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-01 18:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registry', '0037_reviewrequestservice'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reviewrequestservice',
            name='author',
        ),
        migrations.AddField(
            model_name='reviewrequestservice',
            name='workflow',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='review_requests', to='registry.Workflow', verbose_name='workflow'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='workflow',
            name='displayable',
            field=models.BooleanField(default=False),
        ),
    ]
