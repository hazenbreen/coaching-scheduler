from rest_framework import serializers
from datetime import timedelta
from .models import Coach, Student, TimeSlot

class CoachSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Coach
        fields = ('id', 'name',)


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ('id', 'name')


class TimeSlotSerializer(serializers.ModelSerializer):
    endDate = serializers.SerializerMethodField()
    startDate = serializers.DateTimeField(source='start_time')

    class Meta:
        model = TimeSlot
        fields = ('startDate', 'endDate', )

    def get_endDate(self, obj):
        return (obj.start_time + timedelta(hours=2))



    

