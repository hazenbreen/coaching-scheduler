import logging
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CoachSerializer, StudentSerializer, TimeSlotSerializer
from .models import Coach, Student, TimeSlot

logger = logging.getLogger('myLogger')


class CoachViewSet(viewsets.ModelViewSet):
    serializer_class = CoachSerializer
    queryset = Coach.objects.all()

    def list(self, request):
        serializer = CoachSerializer(self.queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()

    def list(self, request):
        serializer = StudentSerializer(self.queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TimeSlotViewSet(viewsets.ModelViewSet):
    serializer_class = TimeSlotSerializer
    queryset = TimeSlot.objects.all()

    def list(self, request):
        coachId = request.headers.get('Coach')
        logger.critical(coachId)
        serializer = TimeSlotSerializer(self.queryset.filter(coach=coachId), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def partial_update(self, request, pk=None):
        return Response(status=status.HTTP_200_OK)


