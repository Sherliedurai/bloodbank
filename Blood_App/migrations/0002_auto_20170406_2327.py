# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-06 17:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blood_App', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bloodpouch',
            name='chlorestrol_level',
            field=models.FloatField(default=9),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='request',
            name='quantity_needed',
            field=models.FloatField(default=500),
            preserve_default=False,
        ),
    ]
