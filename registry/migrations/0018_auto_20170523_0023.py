# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-23 03:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registry', '0017_auto_20170523_0015'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicationdocument',
            name='external_link',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='applicationfile',
            name='external_link',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='dataexchangeformatapplicationdocument',
            name='external_link',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='dataexchangeformatservicedocument',
            name='external_link',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='infrastructuredescriptiondocument',
            name='external_link',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='infrastructurereferencedocument',
            name='external_link',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='participantdocument',
            name='external_link',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='referencedocument',
            name='external_link',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='servicedocument',
            name='external_link',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='technicalinterfacedocument',
            name='external_link',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='applicationdocument',
            name='document',
            field=models.FileField(blank=True, upload_to='applications/documents/'),
        ),
        migrations.AlterField(
            model_name='dataexchangeformatapplicationdocument',
            name='document',
            field=models.FileField(blank=True, upload_to='infrastructure/documents/data_exchange_formats/applications/'),
        ),
        migrations.AlterField(
            model_name='dataexchangeformatservicedocument',
            name='document',
            field=models.FileField(blank=True, upload_to='infrastructure/data_exchange_formats/documents/services/'),
        ),
        migrations.AlterField(
            model_name='infrastructuredescriptiondocument',
            name='document',
            field=models.FileField(blank=True, upload_to='infrastructure/documents/infrastructure_description/'),
        ),
        migrations.AlterField(
            model_name='infrastructurereferencedocument',
            name='document',
            field=models.FileField(blank=True, upload_to='infrastructure/reference_documents/'),
        ),
        migrations.AlterField(
            model_name='participantdocument',
            name='document',
            field=models.FileField(blank=True, upload_to='participants/documents/'),
        ),
        migrations.AlterField(
            model_name='referencedocument',
            name='document',
            field=models.FileField(blank=True, upload_to='swim/reference_documents/'),
        ),
        migrations.AlterField(
            model_name='servicedocument',
            name='document',
            field=models.FileField(blank=True, upload_to='services/documents/'),
        ),
        migrations.AlterField(
            model_name='technicalinterfacedocument',
            name='document',
            field=models.FileField(blank=True, upload_to='services/technical_interfaces/documents/'),
        ),
    ]