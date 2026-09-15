from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Patient
from accounts.decorators import receptionist_required

@receptionist_required
def patient_list(request):
    patients = Patient.objects.all()
    return render(
        request,
        "patients/patient_list.html",
        {"patients": patients}
    )