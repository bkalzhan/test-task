from django.contrib import admin
from .models import Employee
# Register your models here.

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'position', 'joined_at', 'salary', 'parent_id']
    list_filter = ['id', 'first_name', 'last_name', 'position', 'joined_at', 'salary', 'parent_id']
    search_fields = ['id', 'first_name', 'last_name', 'position', 'joined_at', 'salary', 'parent_id']
    list_editable = ['first_name', 'last_name', 'position', 'joined_at', 'salary', 'parent_id']
    ordering = ['id', 'first_name', 'last_name', 'position', 'joined_at', 'salary', 'parent_id']