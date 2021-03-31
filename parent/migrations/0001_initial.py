# Generated by Django 3.1.7 on 2021-03-31 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
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
    ]
