from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import RegistrationForm
from patients.models import Patient
from doctors.models import Doctor
from appointments.models import Appointment
from rooms.models import Bed
from billing.models import Bill
from pharmacy.models import Medicine
from django.db import models
from django.utils import timezone
from .decorators import (
    doctor_required,
    patient_required,
    admin_required,
    receptionist_required,
)

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("login")

    else:
        form = RegistrationForm()

    return render(
        request,
        "accounts/register.html",
        {"form": form}
    )


def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)

            if user.is_superuser:
                return redirect("admin_dashboard")

            role = user.profile.role

            if role == "ADMIN":
                return redirect("admin_dashboard")

            elif role == "DOCTOR":
                return redirect("doctor_dashboard")

            elif role == "RECEPTIONIST":
                return redirect("receptionist_dashboard")

            elif role == "PATIENT":
                return redirect("patient_dashboard")
                

        return render(
            request,
            "accounts/login.html",
            {"error": "Invalid username or password."}
        )

    return render(request, "accounts/login.html")

def user_logout(request):
    logout(request)
    return redirect("login")

@login_required
def admin_dashboard(request):
    return redirect("dashboard")


@doctor_required
def doctor_dashboard(request):
    return render(
        request,
        "accounts/doctor_dashboard.html"
    )

@receptionist_required
def receptionist_dashboard(request):
    return render(
        request,
        "accounts/receptionist_dashboard.html"
    )

@patient_required
def patient_dashboard(request):
    return render(
        request,
        "accounts/patient_dashboard.html"
    )

@admin_required
def dashboard(request):
    total_patients = Patient.objects.count()
    total_doctors = Doctor.objects.count()

    today_appointments = Appointment.objects.filter(
        appointment_date=timezone.now().date()
    ).count()

    total_beds = Bed.objects.count()

    available_beds = Bed.objects.filter(
        is_occupied=False
    ).count()

    occupied_beds = Bed.objects.filter(
        is_occupied=True
    ).count()

    total_revenue = sum(
        bill.total_amount
        for bill in Bill.objects.filter(payment_status="PAID")
    )

    low_stock_medicines = Medicine.objects.filter(
        quantity__lte=models.F("low_stock_threshold")
    ).count()

    return render(
        request,
        "accounts/dashboard.html",
        {
            "total_patients": total_patients,
            "total_doctors": total_doctors,
            "today_appointments": today_appointments,
            "total_beds": total_beds,
            "available_beds": available_beds,
            "occupied_beds": occupied_beds,
            "total_revenue": total_revenue,
            "low_stock_medicines": low_stock_medicines,
        }
    )

@admin_required
def reports(request):
    total_patients = Patient.objects.count()
    total_doctors = Doctor.objects.count()

    total_appointments = Appointment.objects.count()
    completed_appointments = Appointment.objects.filter(
        status="COMPLETED"
    ).count()
    cancelled_appointments = Appointment.objects.filter(
        status="CANCELLED"
    ).count()

    total_beds = Bed.objects.count()
    occupied_beds = Bed.objects.filter(
        is_occupied=True
    ).count()
    available_beds = Bed.objects.filter(
        is_occupied=False
    ).count()

    total_bills = Bill.objects.count()
    paid_bills = Bill.objects.filter(
        payment_status="PAID"
    ).count()
    pending_bills = Bill.objects.filter(
        payment_status="PENDING"
    ).count()

    total_revenue = sum(
        bill.total_amount
        for bill in Bill.objects.filter(
            payment_status="PAID"
        )
    )

    total_medicines = Medicine.objects.count()
    low_stock_medicines = Medicine.objects.filter(
        quantity__lte=models.F("low_stock_threshold")
    ).count()

    return render(
        request,
        "accounts/reports.html",
        {
            "total_patients": total_patients,
            "total_doctors": total_doctors,
            "total_appointments": total_appointments,
            "completed_appointments": completed_appointments,
            "cancelled_appointments": cancelled_appointments,
            "total_beds": total_beds,
            "occupied_beds": occupied_beds,
            "available_beds": available_beds,
            "total_bills": total_bills,
            "paid_bills": paid_bills,
            "pending_bills": pending_bills,
            "total_revenue": total_revenue,
            "total_medicines": total_medicines,
            "low_stock_medicines": low_stock_medicines,
        }
    )