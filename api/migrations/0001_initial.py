# Generated by Django 3.2.6 on 2021-08-13 02:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Buses',
            fields=[
                ('bus_id', models.AutoField(primary_key=True, serialize=False)),
                ('bus_number', models.CharField(max_length=20, unique=True)),
                ('bus_name', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'buses',
            },
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('driver_id', models.AutoField(primary_key=True, serialize=False)),
                ('driver_name', models.CharField(max_length=100)),
                ('driver_phone', models.CharField(max_length=10, unique=True)),
            ],
            options={
                'verbose_name_plural': 'drivers',
                'db_table': 'driver',
            },
        ),
        migrations.CreateModel(
            name='Routes',
            fields=[
                ('route_id', models.AutoField(primary_key=True, serialize=False)),
                ('route_name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'routes',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('location_id', models.AutoField(primary_key=True, serialize=False)),
                ('lat', models.CharField(max_length=50)),
                ('long', models.CharField(max_length=50)),
                ('bus_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.buses')),
            ],
            options={
                'db_table': 'location',
            },
        ),
        migrations.CreateModel(
            name='BusRouteTiming',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timing', models.TimeField(auto_now=False)),
                ('bus_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.buses')),
                ('route_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.routes')),
            ],
            options={
                'db_table': 'bus_route_timing',
            },
        ),
        migrations.CreateModel(
            name='BusDriver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bus_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.buses')),
                ('driver_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.driver')),
            ],
            options={
                'db_table': 'bus_driver',
            },
        ),
    ]
