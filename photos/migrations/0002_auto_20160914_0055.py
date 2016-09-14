# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-14 00:55
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='photo',
            name='visibility',
            field=models.CharField(choices=[('PUB', 'Publica'), ('PRI', 'Privada')], default='PUB', max_length=3),
        ),
        migrations.AlterField(
            model_name='photo',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='photo',
            name='license',
            field=models.CharField(choices=[('RIG', 'Copyright'), ('LEF', 'Copyleft'), ('CC', 'Creative Commons')], default='CC', max_length=3),
        ),
    ]
