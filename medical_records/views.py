from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from appointments.models import Appointment
from .forms import MedicalRecordForm
from accounts.decorators import patient_required
from .models import MedicalRecord

@login_required
def consultation(request, appointment_id):

    appointment = get_object_or_404(
        Appointment,
        id=appointment_id
    )


    if appointment.doctor.user != request.user:
        return redirect("doctor_appointments")

    if request.method == "POST":
        form = MedicalRecordForm(request.POST)

        if form.is_valid():

            medical_record = form.save(commit=False)

            medical_record.patient = appointment.patient
            medical_record.doctor = appointment.doctor

            medical_record.save()
            
            appointment.status = "COMPLETED"
            appointment.save()

            return redirect("doctor_appointments")

    else:
        form = MedicalRecordForm()

    return render(
        request,
        "medical_records/consultation.html",
        {
            "form": form,
            "appointment": appointment,
        }
    )

@patient_required
def my_medical_history(request):

    records = MedicalRecord.objects.filter(
        patient=request.user.patient
    ).select_related(
        "doctor__user",
        "appointment"
    ).order_by("-created_at")

    return render(
        request,
        "medical_records/my_medical_history.html",
        {
            "records": records
        }
    )