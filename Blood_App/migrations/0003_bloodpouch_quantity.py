# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-08 15:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blood_App', '0002_auto_20170406_2327'),
    ]

    operations = [
        migrations.AddField(
            model_name='bloodpouch',
            name='quantity',
            field=models.IntegerField(default=500),
            preserve_default=False,
        ),
    ]