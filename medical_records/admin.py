from django.contrib import admin
from .models import MedicalRecord


@admin.register(MedicalRecord)
class MedicalRecordAdmin(admin.ModelAdmin):
    list_display = (
        "patient",
        "doctor",
        "diagnosis",
        "created_at",
    )

    list_filter = (
        "created_at",
    )

    search_fields = (
        "patient__user__username",
        "doctor__user__username",
        "diagnosis",
    )