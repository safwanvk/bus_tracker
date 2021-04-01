# Generated by Django 3.1.7 on 2021-04-01 09:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('driver', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
                ('contact', models.IntegerField()),
                ('password', models.CharField(max_length=128)),
                ('email', models.CharField(max_length=64)),
                ('home_gps', models.CharField(max_length=64)),
            ],
            options={
                'db_table': 'Parent',
            },
        ),
        migrations.CreateModel(
            name='Kid',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=60, unique=True)),
                ('section', models.TextField(max_length=60)),
                ('photo', models.FileField(upload_to='')),
                ('bus_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='driver.bus')),
                ('parent_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parent.parent')),
            ],
            options={
                'db_table': 'Kid',
            },
        ),
    ]
