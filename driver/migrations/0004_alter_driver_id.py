# Generated by Django 3.2 on 2021-04-14 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0003_auto_20210407_1004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]