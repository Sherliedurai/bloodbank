# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-08 17:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blood_App', '0006_auto_20170408_2311'),
    ]

    operations = [
        migrations.AddField(
            model_name='bloodpouch',
            name='is_requested',
            field=models.IntegerField(default=0),
        ),
    ]