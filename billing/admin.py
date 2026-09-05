from django.contrib import admin
from .models import Bill


@admin.register(Bill)
class BillAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "patient",
        "doctor",
        "appointment",
        "consultation_fee",
        "lab_charges",
        "medicine_charges",
        "total_amount",
        "payment_status",
        "created_at",
    )

    list_filter = (
        "payment_status",
        "created_at",
    )

    search_fields = (
        "patient__user__username",
        "doctor__user__username",
    )