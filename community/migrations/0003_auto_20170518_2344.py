# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-19 02:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0002_auto_20170518_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='image',
            field=models.ImageField(default='participants/profiles/images/none/default.jpg', upload_to='participants/profiles/images/'),
        ),
    ]
