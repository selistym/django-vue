# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-12-05 20:19
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0012_auto_20161202_1736'),
    ]

    operations = [
        migrations.AddField(
            model_name='locationlimbo',
            name='is_modified',
            field=models.BooleanField(default=False),
        ),
    ]
