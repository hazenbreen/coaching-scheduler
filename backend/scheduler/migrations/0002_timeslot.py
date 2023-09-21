# Generated by Django 4.2.5 on 2023-09-18 23:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimeSlot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField()),
                ('coach', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scheduler.coach')),
            ],
        ),
    ]