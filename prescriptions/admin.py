from django.contrib import admin
from .models import Prescription


@admin.register(Prescription)
class PrescriptionAdmin(admin.ModelAdmin):
    list_display = (
        "patient",
        "doctor",
        "medicine",
        "dosage",
        "frequency",
        "duration",
        "created_at",
    )

    list_filter = (
        "frequency",
        "created_at",
    )

    search_fields = (
        "patient__user__username",
        "doctor__user__username",
        "medicine",
    )