# Generated by Django 3.0.8 on 2020-08-24 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thugs', '0005_auto_20200824_0818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='raila',
            name='betrs',
            field=models.IntegerField(),
        ),
    ]