from django.contrib import admin
from .models import Prescription


@admin.register(Prescription)
class PrescriptionAdmin(admin.ModelAdmin):

    list_display = (
        "patient",
        "doctor",
        "appointment",
        "medicine",
        "dosage",
        "created_at",
    )

    list_filter = (
        "doctor",
        "created_at",
    )

    search_fields = (
        "patient__user__username",
        "doctor__user__username",
        "medicine",
    )