from django.shortcuts import render
from .models import Doctor
from accounts.decorators import admin_required


@admin_required
def doctor_list(request):
    doctors = Doctor.objects.all()

    return render(
        request,
        "doctors/doctor_list.html",
        {
            "doctors": doctors
        }
    )