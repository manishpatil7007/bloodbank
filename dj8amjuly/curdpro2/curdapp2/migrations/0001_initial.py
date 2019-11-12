# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-08-29 11:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.IntegerField()),
                ('product_name', models.CharField(max_length=100)),
                ('product_class', models.CharField(max_length=10)),
                ('product_color', models.CharField(max_length=100)),
                ('product_cost', models.IntegerField()),
            ],
        ),
    ]
