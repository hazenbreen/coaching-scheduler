# Generated by Django 4.2.5 on 2023-09-19 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0002_timeslot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeslot',
            name='time',
            field=models.DurationField(),
        ),
    ]
