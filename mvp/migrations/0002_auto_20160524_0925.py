# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-24 09:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mvp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Newsletter',
            new_name='SignUp',
        ),
    ]
