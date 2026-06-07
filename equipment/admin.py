from django.contrib import admin
from .models import Equipment, Failure


@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ("name", "inventory_number", "manufacturer", "location")


@admin.register(Failure)
class FailureAdmin(admin.ModelAdmin):
    list_display = ("equipment", "title", "failure_date", "status")
    list_filter = ("status", "equipment")