from django.contrib import admin
from .models import *


@admin.register(Status, PositionJob)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_editable = ('name',)
    search_fields = ('name',)


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name',
        'patronymic',
        'PositionJob',
        'login',
        'password',
        'photo'
    )
    list_editable = (
        'first_name',
        'last_name',
        'patronymic',
        'PositionJob',
        'login',
        'password',
        'photo'
    )
    list_filter = ('first_name', 'PositionJob')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'table', 'time', 'cost', 'status', 'Employee')
    list_editable = ('table', 'time', 'cost', 'status', 'Employee')

    list_filter = ('table', 'cost', 'status')