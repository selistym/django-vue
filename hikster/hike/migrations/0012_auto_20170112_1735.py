# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-01-12 17:35
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hike', '0011_auto_20161221_1714'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trail',
            name='activity',
        ),
        migrations.AddField(
            model_name='trail',
            name='activity',
            field=models.ManyToManyField(blank=True, to='hike.Activity'),
        ),
    ]
