from django.db import models
from doctors.models import Doctor
from patients.models import Patient
from appointments.models import Appointment


class LabTest(models.Model):

    STATUS_CHOICES = [
        ("REQUESTED", "Requested"),
        ("COMPLETED", "Completed"),
    ]

    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name="lab_tests"
    )

    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.CASCADE,
        related_name="lab_tests"
    )

    appointment = models.ForeignKey(
        Appointment,
        on_delete=models.CASCADE,
        related_name="lab_tests"
    )

    test_name = models.CharField(
        max_length=200
    )

    result = models.TextField(
        blank=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="REQUESTED"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return (
            f"{self.patient} - "
            f"{self.test_name}"
        )