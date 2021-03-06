# Generated by Django 3.2 on 2021-05-05 08:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bus',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('bus_no', models.TextField(max_length=60)),
                ('description', models.TextField(max_length=600)),
            ],
            options={
                'db_table': 'Bus',
            },
        ),
        migrations.CreateModel(
            name='Journey',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('j_type', models.BooleanField(default=1)),
                ('date', models.TextField()),
                ('start', models.TextField(default=0)),
                ('end', models.TextField(default=0)),
                ('gps', models.TextField()),
                ('last_update', models.TextField()),
                ('bus_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='driver.bus')),
            ],
            options={
                'db_table': 'Journey',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('gps', models.TextField()),
                ('time', models.TextField()),
                ('j_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='driver.journey')),
            ],
            options={
                'db_table': 'Location',
            },
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
                ('contact', models.CharField(max_length=15)),
                ('password', models.CharField(max_length=128)),
                ('token', models.TextField()),
                ('expires', models.TextField()),
                ('active_ride_j_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='driver.journey')),
                ('bus_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='driver.bus')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.user')),
            ],
            options={
                'db_table': 'Driver',
            },
        ),
    ]
