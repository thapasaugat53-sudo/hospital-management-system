from django.contrib import admin
from .models import LabTest


@admin.register(LabTest)
class LabTestAdmin(admin.ModelAdmin):

    list_display = (
        "patient",
        "doctor",
        "test_name",
        "status",
        "created_at",
    )

    list_filter = (
        "status",
        "test_name",
    )

    search_fields = (
        "patient__user__username",
        "doctor__user__username",
        "test_name",
    )