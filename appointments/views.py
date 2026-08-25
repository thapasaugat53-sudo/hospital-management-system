from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.db.models import Max
from .forms import AppointmentForm
from .models import Appointment


@login_required
def book_appointment(request):

    if request.method == "POST":
        form = AppointmentForm(request.POST)

        if form.is_valid():

            appointment = form.save(commit=False)

            appointment.patient = request.user.patient

            last_token = Appointment.objects.filter(
                appointment_date=appointment.appointment_date
            ).aggregate(
                Max("token_number")
            )["token_number__max"]

            appointment.token_number = (
                1 if last_token is None else last_token + 1
            )

            appointment.save()

            return redirect("my_appointments")

    else:
        form = AppointmentForm()

    return render(
        request,
        "appointments/book_appointment.html",
        {"form": form}
    )
@login_required
def my_appointments(request):

    appointments = request.user.patient.appointments.all()

    return render(
        request,
        "appointments/my_appointments.html",
        {"appointments": appointments}
    )

@login_required
def doctor_appointments(request):

    appointments = request.user.doctor.appointments.select_related(
        "patient__user"
    ).order_by(
        "appointment_date",
        "appointment_time"
    )

    return render(
        request,
        "appointments/doctor_appointments.html",
        {"appointments": appointments}
    )

@login_required
def confirm_appointment(request, appointment_id):

    appointment = Appointment.objects.get(id=appointment_id)

    # Make sure this appointment belongs to the logged-in doctor
    if appointment.doctor.user != request.user:
        return redirect("doctor_appointments")

    appointment.status = "CONFIRMED"
    appointment.save()

    return redirect("doctor_appointments")


@login_required
def cancel_appointment(request, appointment_id):

    appointment = Appointment.objects.get(id=appointment_id)

    # Make sure this appointment belongs to the logged-in doctor
    if appointment.doctor.user != request.user:
        return redirect("doctor_appointments")

    appointment.status = "CANCELLED"
    appointment.save()

    return redirect("doctor_appointments")