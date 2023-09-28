from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from .validators import validate_start_time
from datetime import datetime    


class Coach(models.Model):
    name = models.CharField(max_length=120, unique=True)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Coaches"


class Student(models.Model):
    name = models.CharField(max_length=120, unique=True)

    def __str__(self):
        return self.name


class TimeSlot(models.Model):
    start_time = models.DateTimeField(null=False, blank=False, default=datetime.now, validators=[validate_start_time])
    coach = models.ForeignKey(Coach, on_delete=models.CASCADE, null=False, blank=False, related_name='time_slots')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True, blank=True, related_name='booked_appts')
    is_completed = models.BooleanField(default=False)
    student_satisfaction = models.IntegerField(null=True, blank=True, validators=[MaxValueValidator(5), MinValueValidator(1)])
    coach_notes = models.TextField(default='', blank=True)

    def __str__(self):
        return str(self.start_time)




