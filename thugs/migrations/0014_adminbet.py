# Generated by Django 3.0.8 on 2020-08-26 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thugs', '0013_delete_adminbet'),
    ]

    operations = [
        migrations.CreateModel(
            name='adminbet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('club1', models.CharField(max_length=20)),
                ('club2', models.CharField(max_length=20)),
                ('odds1', models.DecimalField(decimal_places=2, max_digits=5)),
                ('odds2', models.DecimalField(decimal_places=2, max_digits=5)),
                ('lrange', models.IntegerField()),
                ('uprange', models.IntegerField()),
            ],
        ),
    ]
