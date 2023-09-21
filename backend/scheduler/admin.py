from django.contrib import admin
from .models import Coach, Student, TimeSlot

class CoachAdmin(admin.ModelAdmin):
    list_display = ('name',)

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name',)  

class TimeSlotAdmin(admin.ModelAdmin):
    list_display = ('start_time', 'coach', 'student', 'is_completed', 'student_satisfaction', 'coach_notes',)


admin.site.register(Coach, CoachAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(TimeSlot, TimeSlotAdmin)
