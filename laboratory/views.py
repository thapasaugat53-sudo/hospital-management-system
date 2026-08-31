from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from appointments.models import Appointment
from .forms import LabTestForm, LabResultForm
from .models import LabTest


@login_required
def request_lab_test(request, appointment_id):

    appointment = get_object_or_404(
        Appointment,
        id=appointment_id
    )

    if appointment.doctor.user != request.user:
        return redirect("doctor_appointments")

    if request.method == "POST":

        form = LabTestForm(request.POST)

        if form.is_valid():

            lab_test = form.save(commit=False)

            lab_test.patient = appointment.patient
            lab_test.doctor = appointment.doctor
            lab_test.appointment = appointment

            lab_test.save()

            return redirect("doctor_appointments")

    else:
        form = LabTestForm()

    return render(
        request,
        "laboratory/request_lab_test.html",
        {
            "form": form,
            "appointment": appointment,
        }
    )

@login_required
def lab_tests(request):

    tests = LabTest.objects.select_related(
        "patient__user",
        "doctor__user"
    ).order_by("-created_at")

    return render(
        request,
        "laboratory/lab_tests.html",
        {"tests": tests}
    )

@login_required
def enter_lab_result(request, test_id):

    lab_test = get_object_or_404(
        LabTest,
        id=test_id
    )

    if request.method == "POST":

        form = LabResultForm(
            request.POST,
            instance=lab_test
        )

        if form.is_valid():

            lab_test = form.save(commit=False)

            lab_test.status = "COMPLETED"

            lab_test.save()

            return redirect("lab_tests")

    else:

        form = LabResultForm(
            instance=lab_test
        )

    return render(
        request,
        "laboratory/enter_lab_result.html",
        {
            "form": form,
            "lab_test": lab_test,
        }
    )