from django.db import models
from doctors.models import Doctor
from patients.models import Patient
from appointments.models import Appointment


class Prescription(models.Model):

    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name="prescriptions"
    )

    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.CASCADE,
        related_name="prescriptions"
    )

    appointment = models.ForeignKey(
        Appointment,
        on_delete=models.CASCADE,
        related_name="prescriptions",
        null=True,
        blank=True
    )

    medicine = models.CharField(
        max_length=200
    )

    dosage = models.CharField(
        max_length=100
    )

    instructions = models.TextField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return (
            f"{self.patient} - "
            f"{self.medicine}"
        )