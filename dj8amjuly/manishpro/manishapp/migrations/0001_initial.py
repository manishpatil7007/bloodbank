# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-08-20 14:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empdata1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ename', models.CharField(max_length=100)),
                ('salary', models.IntegerField()),
                ('mobile', models.BigIntegerField()),
                ('email', models.EmailField(max_length=100)),
                ('location', models.CharField(max_length=100)),
            ],
        ),
    ]
