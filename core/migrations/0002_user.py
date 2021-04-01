# Generated by Django 3.1.7 on 2021-04-01 10:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=15)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=500)),
                ('is_active', models.BooleanField()),
                ('role_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.usertype')),
            ],
            options={
                'db_table': 'User',
            },
        ),
    ]