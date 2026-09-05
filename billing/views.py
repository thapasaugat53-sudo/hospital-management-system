from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from appointments.models import Appointment
from .forms import BillForm
from .models import Bill


@login_required
def create_bill(request, appointment_id):

    appointment = get_object_or_404(
        Appointment,
        id=appointment_id
    )

    if request.method == "POST":

        form = BillForm(request.POST)

        if form.is_valid():

            bill = form.save(commit=False)

            bill.patient = appointment.patient
            bill.doctor = appointment.doctor
            bill.appointment = appointment

            bill.save()

            return redirect("bill_detail", bill.id)

    else:

        form = BillForm()

    return render(
        request,
        "billing/create_bill.html",
        {
            "form": form,
            "appointment": appointment,
        }
    )

@login_required
def bill_detail(request, bill_id):

    bill = get_object_or_404(
        Bill,
        id=bill_id
    )

    return render(
        request,
        "billing/bill_detail.html",
        {
            "bill": bill,
        }
    )

@login_required
def patient_bills(request):

    bills = Bill.objects.filter(
        patient=request.user.patient
    ).select_related(
        "doctor__user",
        "appointment"
    ).order_by("-created_at")

    return render(
        request,
        "billing/patient_bills.html",
        {
            "bills": bills,
        }
    )