# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-02-09 16:30
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0015_auto_20170127_1422'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='deletion_pending',
            field=models.BooleanField(default=False),
        ),
    ]
