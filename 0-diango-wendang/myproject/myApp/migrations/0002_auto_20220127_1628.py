# Generated by Django 3.0.11 on 2022-01-27 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentsubject',
            name='total_points',
            field=models.DecimalField(decimal_places=1, max_digits=4),
        ),
    ]