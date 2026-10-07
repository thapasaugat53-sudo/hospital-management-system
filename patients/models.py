from django.contrib.auth.models import User
from django.db import models


class Patient(models.Model):

    GENDER_CHOICES = [
        ("MALE", "Male"),
        ("FEMALE", "Female"),
        ("OTHER", "Other"),
    ]

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="patient"
    )

    date_of_birth = models.DateField()

    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES
    )

    phone = models.CharField(max_length=20)

    address = models.TextField()

    emergency_contact = models.CharField(
        max_length=100
    )

    def __str__(self):
        return self.user.get_full_name() or self.user.username