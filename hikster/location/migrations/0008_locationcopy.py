# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-12-01 17:50
import django.contrib.gis.db.models.fields
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('utils', '0003_merge_20161201_1437'),
        ('location', '0007_location_exploitation_periods'),
    ]

    operations = [
        migrations.CreateModel(
            name='LocationCopy',
            fields=[
                ('objectid', models.IntegerField(blank=True, null=True, unique=True)),
                ('location_id', models.AutoField(primary_key=True, serialize=False)),
                ('shape', django.contrib.gis.db.models.fields.GeometryField(blank=True, null=True, srid=4326)),
                ('name', models.CharField(max_length=250, null=True)),
                ('type', models.IntegerField(blank=True, choices=[(7, 'Parc'), (8, 'Municipalité'), (9, 'Mont'), (10, 'Région touristique'), (11, 'Réseau')], null=True)),
                ('parking', models.IntegerField(blank=True, null=True)),
                ('network', models.CharField(blank=True, max_length=100, null=True)),
                ('dog_allowed', models.BooleanField()),
                ('living_rules', models.TextField(blank=True, null=True)),
                ('fare_note', models.TextField(blank=True, null=True)),
                ('transport', models.TextField(blank=True, null=True)),
                ('schedule', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('network_length', models.FloatField(blank=True, null=True)),
                ('exploitation_periods', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='utils.Address')),
                ('contact', models.ManyToManyField(blank=True, to='utils.Contact')),
                ('images', models.ManyToManyField(blank=True, to='utils.Image')),
                ('original', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='location.Location')),
            ],
            managers=[
                ('objects_with_eager_loading', django.db.models.manager.Manager()),
                ('objects', django.db.models.manager.Manager()),
            ],
        ),
    ]
