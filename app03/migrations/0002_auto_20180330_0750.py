# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-30 07:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app03', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='USER',
            new_name='USERS',
        ),
    ]
