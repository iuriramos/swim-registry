# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-23 03:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registry', '0016_auto_20170522_2352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicationdocument',
            name='description',
            field=models.TextField(blank=True, default=None),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='applicationdocument',
            name='version',
            field=models.CharField(blank=True, default=None, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='applicationfile',
            name='description',
            field=models.TextField(blank=True, default=None),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='applicationfile',
            name='version',
            field=models.CharField(blank=True, default=None, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dataexchangeformatapplicationdocument',
            name='description',
            field=models.TextField(blank=True, default=None),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dataexchangeformatapplicationdocument',
            name='version',
            field=models.CharField(blank=True, default=None, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dataexchangeformatservicedocument',
            name='description',
            field=models.TextField(blank=True, default=None),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dataexchangeformatservicedocument',
            name='version',
            field=models.CharField(blank=True, default=None, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='infrastructuredescriptiondocument',
            name='description',
            field=models.TextField(blank=True, default=None),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='infrastructuredescriptiondocument',
            name='version',
            field=models.CharField(blank=True, default=None, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='infrastructurereferencedocument',
            name='description',
            field=models.TextField(blank=True, default=None),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='infrastructurereferencedocument',
            name='version',
            field=models.CharField(blank=True, default=None, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='participantdocument',
            name='description',
            field=models.TextField(blank=True, default=None),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='participantdocument',
            name='version',
            field=models.CharField(blank=True, default=None, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='referencedocument',
            name='description',
            field=models.TextField(blank=True, default=None),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='referencedocument',
            name='version',
            field=models.CharField(blank=True, default=None, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='servicedocument',
            name='description',
            field=models.TextField(blank=True, default=None),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='servicedocument',
            name='version',
            field=models.CharField(blank=True, default=None, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='technicalinterfacedocument',
            name='description',
            field=models.TextField(blank=True, default=None),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='technicalinterfacedocument',
            name='version',
            field=models.CharField(blank=True, default=None, max_length=50),
            preserve_default=False,
        ),
    ]
