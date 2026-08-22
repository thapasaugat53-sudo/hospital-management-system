from django.contrib import admin
from .models import Patient


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "date_of_birth",
        "gender",
        "phone",
        "emergency_contact",
    )

    search_fields = (
        "user__username",
        "phone",
    )

    list_filter = (
        "gender",
    )