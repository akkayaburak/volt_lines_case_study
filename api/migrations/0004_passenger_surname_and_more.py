# Generated by Django 4.0.5 on 2022-06-14 21:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_passenger_trip_estimated_end_time_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='passenger',
            name='surname',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='passenger_trip',
            name='estimated_end_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 14, 21, 35, 41, 644087)),
        ),
    ]
