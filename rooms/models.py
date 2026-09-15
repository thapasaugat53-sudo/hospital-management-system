from django.db import models
from patients.models import Patient


class Room(models.Model):
    ROOM_TYPE_CHOICES = [
        ("GENERAL", "General"),
        ("PRIVATE", "Private"),
        ("ICU", "ICU"),
    ]

    room_number = models.CharField(max_length=20, unique=True)
    room_type = models.CharField(
        max_length=20,
        choices=ROOM_TYPE_CHOICES
    )
    floor = models.PositiveIntegerField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"Room {self.room_number}"


class Bed(models.Model):
    bed_number = models.CharField(max_length=20, unique=True)
    room = models.ForeignKey(
        Room,
        on_delete=models.CASCADE,
        related_name="beds"
    )
    patient = models.OneToOneField(
        Patient,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="bed"
    )
    is_occupied = models.BooleanField(default=False)

    def __str__(self):
        return f"Bed {self.bed_number}"