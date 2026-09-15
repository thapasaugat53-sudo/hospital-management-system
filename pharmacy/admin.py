from django.contrib import admin
from .models import Medicine, MedicineSale


@admin.register(Medicine)
class MedicineAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "quantity",
        "price",
        "expiry_date",
        "low_stock_threshold",
    )

    search_fields = (
        "name",
    )

    list_filter = (
        "expiry_date",
    )

@admin.register(MedicineSale)
class MedicineSaleAdmin(admin.ModelAdmin):

    list_display = (
        "patient",
        "medicine",
        "quantity",
        "total_price",
        "created_at",
    )

    list_filter = (
        "medicine",
        "created_at",
    )