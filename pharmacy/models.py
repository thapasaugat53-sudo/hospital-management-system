from django.db import models
from patients.models import Patient


class Medicine(models.Model):

    name = models.CharField(
        max_length=200
    )

    quantity = models.PositiveIntegerField(
        default=0
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    expiry_date = models.DateField()

    low_stock_threshold = models.PositiveIntegerField(
        default=10
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name

class MedicineSale(models.Model):

    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name="medicine_sales"
    )

    medicine = models.ForeignKey(
        Medicine,
        on_delete=models.CASCADE,
        related_name="sales"
    )

    quantity = models.PositiveIntegerField()

    total_price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return (
            f"{self.patient} - "
            f"{self.medicine.name} - "
            f"{self.quantity}"
        )