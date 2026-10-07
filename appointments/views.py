from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Max
from accounts.decorators import doctor_required
from .forms import AppointmentForm
from .models import Appointment
from accounts.decorators import receptionist_required, patient_required
from datetime import datetime, timedelta
from django.utils import timezone

@login_required
def book_appointment(request):

    if request.method == "POST":
        form = AppointmentForm(request.POST)

        if form.is_valid():

            appointment = form.save(commit=False)
            appointment.patient = request.user.patient

            # Combine appointment date and time
            appointment_datetime = timezone.make_aware(
                datetime.combine(
                    appointment.appointment_date,
                    appointment.appointment_time
                )
            )

            
            if appointment_datetime <= timezone.now():

                form.add_error(
                    None,
                    "You cannot book an appointment in the past. "
                    "Please choose a future date and time."
                )

            else:

                
                new_start = appointment_datetime

                
                existing_appointments = Appointment.objects.filter(
                    doctor=appointment.doctor,
                    appointment_date=appointment.appointment_date,
                    status__in=["PENDING", "CONFIRMED"]
                )

                conflict = False

                for existing in existing_appointments:

                    existing_start = timezone.make_aware(
                        datetime.combine(
                            existing.appointment_date,
                            existing.appointment_time
                        )
                    )

                    time_difference = abs(
                        new_start - existing_start
                    )

                    if time_difference < timedelta(minutes=45):
                        conflict = True
                        break

                if conflict:

                    form.add_error(
                        None,
                        "This doctor is already booked around this time. "
                        "There must be at least 45 minutes between appointments."
                    )

                else:

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

@patient_required
def my_appointments(request):
    appointments = request.user.patient.appointments.all().order_by(
        "appointment_date",
        "appointment_time"
    )

    return render(
        request,
        "appointments/my_appointments.html",
        {"appointments": appointments}
    )

@doctor_required
def doctor_appointments(request):
    appointments = request.user.doctor.appointments.select_related(
        "patient__user"
    ).order_by("appointment_date", "appointment_time")

    return render(
        request,
        "appointments/doctor_appointments.html",
        {"appointments": appointments}
    )

@doctor_required
def confirm_appointment(request, appointment_id):

    appointment = get_object_or_404(
        Appointment,
        id=appointment_id
    )

    
    if appointment.doctor.user != request.user:
        return redirect("doctor_appointments")

    appointment.status = "CONFIRMED"
    appointment.save()

    return redirect("doctor_appointments")


@doctor_required
def cancel_appointment(request, appointment_id):

    appointment = get_object_or_404(
        Appointment,
        id=appointment_id
    )

    
    if appointment.doctor.user != request.user:
        return redirect("doctor_appointments")

    appointment.status = "CANCELLED"
    appointment.save()

    return redirect("doctor_appointments")

@receptionist_required
def appointment_list(request):
    appointments = Appointment.objects.all().order_by(
        "appointment_date",
        "appointment_time"
    )

    return render(
        request,
        "appointments/appointment_list.html",
        {"appointments": appointments}
    )