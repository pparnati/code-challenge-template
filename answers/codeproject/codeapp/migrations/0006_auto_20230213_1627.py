# Generated by Django 3.2.17 on 2023-02-13 21:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('codeapp', '0005_maxaveragetemp_minaveragetemp_totalprecipitation'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MaxAverageTemp',
        ),
        migrations.DeleteModel(
            name='MinAverageTemp',
        ),
        migrations.DeleteModel(
            name='Totalprecipitation',
        ),
    ]