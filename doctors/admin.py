from django.contrib import admin
from .models import Doctor


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "specialization",
        "phone",
        "license_number",
        "department",
    )

    search_fields = (
        "user__username",
        "specialization",
        "license_number",
    )