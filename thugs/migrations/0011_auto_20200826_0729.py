# Generated by Django 3.0.8 on 2020-08-26 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thugs', '0010_auto_20200824_1211'),
    ]

    operations = [
        migrations.AddField(
            model_name='adminbet',
            name='lrange',
            field=models.IntegerField(default=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='adminbet',
            name='uprange',
            field=models.IntegerField(default=50),
            preserve_default=False,
        ),
    ]
