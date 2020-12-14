# Generated by Django 3.0.8 on 2020-08-24 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
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
            ],
        ),
        migrations.CreateModel(
            name='raila',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bet', models.CharField(max_length=20)),
                ('betrs', models.IntegerField()),
                ('comment', models.CharField(max_length=20)),
                ('author', models.CharField(max_length=20)),
                ('coi', models.IntegerField(blank=True, default=None, null=True)),
                ('commision', models.IntegerField(blank=True, default=None, null=True)),
            ],
            options={
                'db_table': 'xtreme_raila',
            },
        ),
    ]