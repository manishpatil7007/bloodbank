# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-08-17 19:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Fakedataapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fakedata',
            old_name='First_name',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='fakedata',
            old_name='Last_name',
            new_name='last_name',
        ),
    ]
