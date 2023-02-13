# Generated by Django 3.2.17 on 2023-02-12 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WeatherData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weatherdate', models.CharField(max_length=8)),
                ('maxtempofday', models.IntegerField(max_length=8)),
                ('mintempofday', models.IntegerField(max_length=8)),
                ('precipofday', models.IntegerField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='YieldData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=4)),
                ('yieldoftheyear', models.IntegerField(max_length=8)),
            ],
        ),
    ]
