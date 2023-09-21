# Generated by Django 4.2.5 on 2023-09-19 02:47

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0003_alter_timeslot_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='timeslot',
            name='coach_notes',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='timeslot',
            name='is_completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='timeslot',
            name='student',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='booked_appts', to='scheduler.student'),
        ),
        migrations.AddField(
            model_name='timeslot',
            name='student_satisfaction',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='timeslot',
            name='coach',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='time_slots', to='scheduler.coach'),
        ),
        migrations.AlterField(
            model_name='timeslot',
            name='time',
            field=models.DateTimeField(),
        ),
    ]