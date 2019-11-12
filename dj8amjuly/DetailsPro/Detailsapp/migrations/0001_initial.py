# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-08-04 17:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cours',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=100)),
                ('cost', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='stud',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='cours',
            name='abcd',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Detailsapp.stud'),
        ),
    ]
