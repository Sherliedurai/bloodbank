# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-04 14:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blood_App', '0002_auto_20170404_1653'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='pin',
        ),
        migrations.RemoveField(
            model_name='registereduser',
            name='contact',
        ),
        migrations.AddField(
            model_name='registereduser',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=None),
            preserve_default=False,
        ),
    ]
