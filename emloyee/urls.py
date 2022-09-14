from django.contrib import admin
from django.urls import path, include
from .views import EmployeesViewSet

urlpatterns = [
    path('employees/', EmployeesViewSet.as_view({'get': 'list',
                                         'post': 'create'})),
    path('employees/<int:pk>/', EmployeesViewSet.as_view({'get': 'retrieve',
                                                  'delete': 'destroy',
                                                  'put': 'update'})),
]