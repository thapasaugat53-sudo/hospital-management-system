from django.contrib.auth.models import User
from django.db import models

class Department(models.Model):

    name = models.CharField(
        max_length=100,
        unique=True
    )

    description = models.TextField(
        blank=True
    )

    def __str__(self):
        return self.name
    
class Doctor(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="doctor"
    )

    specialization = models.CharField(max_length=100)

    phone = models.CharField(max_length=20)

    license_number = models.CharField(
        max_length=50,
        unique=True
    )

    department = models.ForeignKey(
    Department,
    on_delete=models.SET_NULL,
    null=True,
    blank=True,
    related_name="doctors"
    )

    def __str__(self):
        return f"Dr. {self.user.get_full_name() or self.user.username}"