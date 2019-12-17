# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-09-13 17:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Howarts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('house', models.CharField(max_length=45)),
                ('pet', models.CharField(max_length=45)),
                ('year', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='users2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email_address', models.CharField(max_length=255)),
                ('age', models.IntegerField(default=2)),
                ('created_at', models.DateField(default='2019-01-01')),
                ('updated_at', models.DateField(default='2019-01-01')),
            ],
        ),
    ]
