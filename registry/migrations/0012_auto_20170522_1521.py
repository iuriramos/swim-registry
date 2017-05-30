# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-22 18:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registry', '0011_auto_20170522_1342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='image',
            field=models.ImageField(default='applications/profiles/images/none/default.jpg', upload_to='applications/profiles/images/'),
        ),
        migrations.AlterField(
            model_name='applicationdocument',
            name='image',
            field=models.ImageField(blank=True, default='applications/documents/images/none/default.svg', upload_to='applications/documents/images/'),
        ),
        migrations.AlterField(
            model_name='contactpointapplication',
            name='description',
            field=models.TextField(blank=True, default=None),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contactpointapplication',
            name='email',
            field=models.EmailField(blank=True, default=None, max_length=254),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contactpointapplication',
            name='image',
            field=models.ImageField(blank=True, default='services/contact_points/images/none/default.svg', upload_to='services/contact_points/images/'),
        ),
        migrations.AlterField(
            model_name='contactpointapplication',
            name='telephone',
            field=models.CharField(blank=True, default=None, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contactpointparticipant',
            name='description',
            field=models.TextField(blank=True, default=None),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contactpointparticipant',
            name='email',
            field=models.EmailField(blank=True, default=None, max_length=254),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contactpointparticipant',
            name='image',
            field=models.ImageField(blank=True, default='services/contact_points/images/none/default.svg', upload_to='services/contact_points/images/'),
        ),
        migrations.AlterField(
            model_name='contactpointparticipant',
            name='telephone',
            field=models.CharField(blank=True, default=None, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contactpointservice',
            name='description',
            field=models.TextField(blank=True, default=None),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contactpointservice',
            name='email',
            field=models.EmailField(blank=True, default=None, max_length=254),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contactpointservice',
            name='image',
            field=models.ImageField(blank=True, default='services/contact_points/images/none/default.svg', upload_to='services/contact_points/images/'),
        ),
        migrations.AlterField(
            model_name='contactpointservice',
            name='telephone',
            field=models.CharField(blank=True, default=None, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dataexchangeformatapplication',
            name='description',
            field=models.TextField(blank=True, default=None),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dataexchangeformatapplication',
            name='image',
            field=models.ImageField(default='infrastructure/data_exchange_formats/profiles/images/none/default.svg', upload_to='infrastructure/data_exchange_formats/profiles/images/'),
        ),
        migrations.AlterField(
            model_name='dataexchangeformatapplication',
            name='version',
            field=models.CharField(blank=True, default=None, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dataexchangeformatapplicationdocument',
            name='document',
            field=models.FileField(upload_to='infrastructure/documents/data_exchange_formats/applications/'),
        ),
        migrations.AlterField(
            model_name='dataexchangeformatapplicationdocument',
            name='image',
            field=models.ImageField(blank=True, default='infrastructure/documents/data_exchange_formats/applications/images/none/default.svg', upload_to='infrastructure/documents/data_exchange_formats/applications/images/'),
        ),
        migrations.AlterField(
            model_name='dataexchangeformatservice',
            name='description',
            field=models.TextField(blank=True, default=None),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dataexchangeformatservice',
            name='image',
            field=models.ImageField(default='infrastructure/data_exchange_formats/profiles/images/none/default.svg', upload_to='infrastructure/data_exchange_formats/profiles/images/'),
        ),
        migrations.AlterField(
            model_name='dataexchangeformatservice',
            name='version',
            field=models.CharField(blank=True, default=None, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dataexchangeformatservicedocument',
            name='document',
            field=models.FileField(upload_to='infrastructure/data_exchange_formats/documents/services/'),
        ),
        migrations.AlterField(
            model_name='dataexchangeformatservicedocument',
            name='image',
            field=models.ImageField(blank=True, default='infrastructure/data_exchange_formats/documents/services/images/none/applications/default.svg', upload_to='infrastructure/data_exchange_formats/documents/services/images/'),
        ),
        migrations.AlterField(
            model_name='datastandard',
            name='description',
            field=models.TextField(blank=True, default=None),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='datastandard',
            name='image',
            field=models.ImageField(default='infrastructure/data_standards/profiles/images/none/default.svg', upload_to='infrastructure/data_standards/profiles/images/'),
        ),
        migrations.AlterField(
            model_name='datastandard',
            name='version',
            field=models.CharField(blank=True, default=None, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='endpoint',
            name='address',
            field=models.URLField(blank=True, default=None, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='endpoint',
            name='description',
            field=models.TextField(blank=True, default=None),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='endpoint',
            name='image',
            field=models.ImageField(default='services/end_points/images/none/default.svg', upload_to='services/end_points/images/'),
        ),
        migrations.AlterField(
            model_name='infrastructuredescription',
            name='description',
            field=models.TextField(blank=True, default=None),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='infrastructuredescription',
            name='image',
            field=models.ImageField(default='infrastructure/infrastructure_description/images/none/default.svg', upload_to='infrastructure/infrastructure_description/images/'),
        ),
        migrations.AlterField(
            model_name='infrastructuredescription',
            name='version',
            field=models.CharField(blank=True, default=None, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='infrastructuredescriptiondocument',
            name='image',
            field=models.ImageField(blank=True, default='infrastructure/infrastructure_description/documents/images/none/default.svg', upload_to='infrastructure/infrastructure_description/documents/images/'),
        ),
        migrations.AlterField(
            model_name='infrastructureprofile',
            name='description',
            field=models.TextField(blank=True, default=None),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='infrastructureprofile',
            name='image',
            field=models.ImageField(default='infrastructure/profiles/images/none/default.svg', upload_to='infrastructure/profiles/images/'),
        ),
        migrations.AlterField(
            model_name='infrastructureprofile',
            name='version',
            field=models.CharField(blank=True, default=None, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='infrastructurereferencedocument',
            name='image',
            field=models.ImageField(blank=True, default='infrastructure/reference_documents/images/none/default.svg', upload_to='infrastructure/reference_documents/images/'),
        ),
        migrations.AlterField(
            model_name='participantdocument',
            name='image',
            field=models.ImageField(blank=True, default='participants/documents/images/none/default.svg', upload_to='participants/documents/images/'),
        ),
        migrations.AlterField(
            model_name='referencedocument',
            name='image',
            field=models.ImageField(blank=True, default='swim/reference_documents/images/none/default.svg', upload_to='swim/reference_documents/images/'),
        ),
        migrations.AlterField(
            model_name='service',
            name='image',
            field=models.ImageField(default='services/profiles/images/none/default.svg', upload_to='services/profiles/images/'),
        ),
        migrations.AlterField(
            model_name='servicedocument',
            name='image',
            field=models.ImageField(blank=True, default='services/documents/images/none/default.svg', upload_to='services/documents/images/'),
        ),
        migrations.AlterField(
            model_name='technicalinterface',
            name='image',
            field=models.ImageField(default='services/technical_interfaces/images/none/default.svg', upload_to='services/technical_interfaces/images/'),
        ),
        migrations.AlterField(
            model_name='technicalinterfacebindingdescription',
            name='description',
            field=models.TextField(blank=True, default=None),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='technicalinterfacebindingdescription',
            name='image',
            field=models.ImageField(default='infrastructure/technical_interface_bindings/images/none/default.svg', upload_to='infrastructure/technical_interface_bindings/images/'),
        ),
        migrations.AlterField(
            model_name='technicalinterfacebindingprofile',
            name='description',
            field=models.TextField(blank=True, default=None),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='technicalinterfacebindingprofile',
            name='image',
            field=models.ImageField(default='infrastructure/technical_interface_bindings/images/none/default.svg', upload_to='infrastructure/technical_interface_bindings/images/'),
        ),
        migrations.AlterField(
            model_name='technicalinterfacedocument',
            name='image',
            field=models.ImageField(blank=True, default='services/technical_interfaces/documents/images/none/default.svg', upload_to='services/technical_interfaces/documents/images/'),
        ),
        migrations.AlterField(
            model_name='workflow',
            name='description',
            field=models.TextField(blank=True, default=None),
            preserve_default=False,
        ),
    ]