# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-22 18:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0010_registrationrequest_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='description',
            field=models.TextField(blank=True, default=None),
            preserve_default=False,
        ),
    ]
