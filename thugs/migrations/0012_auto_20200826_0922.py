# Generated by Django 3.0.8 on 2020-08-26 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thugs', '0011_auto_20200826_0729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='raila',
            name='bet',
            field=models.CharField(blank=True, default=None, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='raila',
            name='betrs',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='raila',
            name='comment',
            field=models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='raila',
            name='commision',
            field=models.CharField(blank=True, default=None, max_length=20, null=True),
        ),
    ]
