# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-07 21:28
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hike', '0019_auto_20170220_1629'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trail',
            name='updated',
        ),
        migrations.AddField(
            model_name='trail',
            name='last_modified',
            field=models.DateField(auto_now=True),
        ),
    ]
