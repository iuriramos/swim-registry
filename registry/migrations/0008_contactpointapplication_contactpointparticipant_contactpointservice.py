# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-21 20:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0009_auto_20170521_1401'),
        ('registry', '0007_auto_20170521_1401'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactPointApplication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(null=True)),
                ('telephone', models.CharField(max_length=50, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('image', models.ImageField(default='services/contact_points/images/none/default.jpg', null=True, upload_to='services/contact_points/images/')),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contact_points', to='registry.Service')),
            ],
            options={
                'verbose_name': 'application contact point',
            },
        ),
        migrations.CreateModel(
            name='ContactPointParticipant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(null=True)),
                ('telephone', models.CharField(max_length=50, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('image', models.ImageField(default='services/contact_points/images/none/default.jpg', null=True, upload_to='services/contact_points/images/')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contact_points', to='community.Participant')),
            ],
            options={
                'verbose_name': 'participant contact point',
            },
        ),
        migrations.CreateModel(
            name='ContactPointService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(null=True)),
                ('telephone', models.CharField(max_length=50, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('image', models.ImageField(default='services/contact_points/images/none/default.jpg', null=True, upload_to='services/contact_points/images/')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contact_points', to='registry.Service')),
            ],
            options={
                'verbose_name': 'service contact point',
            },
        ),
    ]
