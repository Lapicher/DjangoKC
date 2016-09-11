# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-11 19:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('url', models.URLField()),
                ('description', models.TextField()),
                ('license', models.CharField(choices=[('RIG', 'Copyright'), ('LEF', 'Copyleft'), ('CC', 'Creative Commons')], max_length=3)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
