from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from appointments.models import Appointment
from .forms import PrescriptionForm
from .models import Prescription


@login_required
def create_prescription(request, appointment_id):

    appointment = get_object_or_404(
        Appointment,
        id=appointment_id
    )

   
    if appointment.doctor.user != request.user:
        return redirect("doctor_appointments")

    
    if appointment.status != "COMPLETED":
        return redirect("doctor_appointments")

    if request.method == "POST":

        form = PrescriptionForm(request.POST)

        if form.is_valid():

            prescription = form.save(commit=False)

            prescription.patient = appointment.patient
            prescription.doctor = appointment.doctor
            prescription.appointment = appointment

            prescription.save()

            return redirect(
                "doctor_appointments"
            )

    else:
        form = PrescriptionForm()

    return render(
        request,
        "prescriptions/create_prescription.html",
        {
            "form": form,
            "appointment": appointment,
        }
    )

@login_required
def prescription_history(request):
    prescriptions = request.user.patient.prescriptions.select_related(
        "doctor__user",
        "appointment"
    ).order_by("-created_at")

    return render(
        request,
        "prescriptions/prescription_history.html",
        {"prescriptions": prescriptions}
    )

@login_required
def print_prescription(request, prescription_id):

    prescription = Prescription.objects.get(
        id=prescription_id
    )

    if prescription.patient.user != request.user:
        return redirect("prescription_history")

    return render(
        request,
        "prescriptions/print_prescription.html",
        {"prescription": prescription}
    )