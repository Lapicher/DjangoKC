# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-26 00:14
from __future__ import unicode_literals

from django.db import migrations, models
import photos.validators


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_auto_20160914_0055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='description',
            field=models.TextField(blank=True, null=True, validators=[photos.validators.badwords]),
        ),
    ]
