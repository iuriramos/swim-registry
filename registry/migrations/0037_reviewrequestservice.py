# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-01 16:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0014_auto_20170601_1040'),
        ('registry', '0036_auto_20170601_1156'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReviewRequestService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modified')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('approved', models.BooleanField(default=False, verbose_name='approved')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review_requests', to='community.Profile', verbose_name='author')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review_requests', to='registry.Service', verbose_name='service')),
            ],
            options={
                'verbose_name': 'service review request',
            },
        ),
    ]