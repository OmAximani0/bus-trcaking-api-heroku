# Generated by Django 3.2.6 on 2021-08-13 05:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='busdriver',
            old_name='bus_id',
            new_name='Bus_id',
        ),
        migrations.RenameField(
            model_name='busdriver',
            old_name='driver_id',
            new_name='Driver_id',
        ),
        migrations.RenameField(
            model_name='buses',
            old_name='bus_id',
            new_name='Bus_id',
        ),
        migrations.RenameField(
            model_name='buses',
            old_name='bus_name',
            new_name='Bus_name',
        ),
        migrations.RenameField(
            model_name='buses',
            old_name='bus_number',
            new_name='Bus_number',
        ),
        migrations.RenameField(
            model_name='busroutetiming',
            old_name='bus_id',
            new_name='Bus_id',
        ),
        migrations.RenameField(
            model_name='busroutetiming',
            old_name='route_id',
            new_name='Route_id',
        ),
        migrations.RenameField(
            model_name='driver',
            old_name='driver_id',
            new_name='Driver_id',
        ),
        migrations.RenameField(
            model_name='driver',
            old_name='driver_name',
            new_name='Driver_name',
        ),
        migrations.RenameField(
            model_name='driver',
            old_name='driver_phone',
            new_name='Driver_phone',
        ),
        migrations.RenameField(
            model_name='location',
            old_name='bus_id',
            new_name='Bus_id',
        ),
        migrations.RenameField(
            model_name='location',
            old_name='lat',
            new_name='Lat',
        ),
        migrations.RenameField(
            model_name='location',
            old_name='location_id',
            new_name='Location_id',
        ),
        migrations.RenameField(
            model_name='location',
            old_name='long',
            new_name='Long',
        ),
        migrations.RenameField(
            model_name='routes',
            old_name='route_id',
            new_name='Route_id',
        ),
        migrations.RenameField(
            model_name='routes',
            old_name='route_name',
            new_name='Route_name',
        ),
        migrations.RemoveField(
            model_name='busroutetiming',
            name='timing',
        ),
        migrations.AddField(
            model_name='busroutetiming',
            name='Timing',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
