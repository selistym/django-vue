# Generated by Django 2.1.5 on 2019-06-05 14:24

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hike', '0061_update_3d_triggers'),
    ]

    operations = [
        migrations.AddField(
            model_name='trailstep',
            name='lat',
            field=models.DecimalField(decimal_places=16, default=Decimal('0'), max_digits=19),
        ),
        migrations.AddField(
            model_name='trailstep',
            name='lng',
            field=models.DecimalField(decimal_places=16, default=Decimal('0'), max_digits=19),
        ),
    ]
