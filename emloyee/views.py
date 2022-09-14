from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated

from .models import Employee
from .serializers import EmployeeSerializer


class EmployeesViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve', 'create', 'update', 'destroy']:
            return EmployeeSerializer
