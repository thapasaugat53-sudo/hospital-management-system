from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.db import models
from django.utils import timezone
from datetime import timedelta
from .models import Medicine, MedicineSale
from .forms import MedicineForm, StockForm, MedicineSaleForm


@login_required
def medicine_list(request):

    medicines = Medicine.objects.all().order_by("name")

    return render(
        request,
        "pharmacy/medicine_list.html",
        {"medicines": medicines}
    )


@login_required
def add_medicine(request):

    if request.method == "POST":

        form = MedicineForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect("medicine_list")

    else:
        form = MedicineForm()

    return render(
        request,
        "pharmacy/add_medicine.html",
        {"form": form}
    )

@login_required
def edit_medicine(request, medicine_id):

    medicine = Medicine.objects.get(id=medicine_id)

    if request.method == "POST":

        form = MedicineForm(
            request.POST,
            instance=medicine
        )

        if form.is_valid():
            form.save()

            return redirect("medicine_list")

    else:
        form = MedicineForm(instance=medicine)

    return render(
        request,
        "pharmacy/edit_medicine.html",
        {"form": form, "medicine": medicine}
    )


@login_required
def delete_medicine(request, medicine_id):

    medicine = Medicine.objects.get(id=medicine_id)

    if request.method == "POST":
        medicine.delete()

        return redirect("medicine_list")

    return render(
        request,
        "pharmacy/delete_medicine.html",
        {"medicine": medicine}
    )

@login_required
def medicine_list(request):

    medicines = Medicine.objects.all().order_by("name")

    today = timezone.now().date()
    expiry_warning_date = today + timedelta(days=30)

    low_stock_medicines = medicines.filter(
        quantity__lte=models.F("low_stock_threshold")
    )

    expired_medicines = medicines.filter(
        expiry_date__lt=today
    )

    expiring_soon_medicines = medicines.filter(
        expiry_date__gte=today,
        expiry_date__lte=expiry_warning_date
    )

    return render(
        request,
        "pharmacy/medicine_list.html",
        {
            "medicines": medicines,
            "low_stock_medicines": low_stock_medicines,
            "expired_medicines": expired_medicines,
            "expiring_soon_medicines": expiring_soon_medicines,
        }
    )

@login_required
def pharmacy_dashboard(request):

    medicines = Medicine.objects.all()

    today = timezone.now().date()
    expiry_warning_date = today + timedelta(days=30)

    total_medicines = medicines.count()

    low_stock_medicines = medicines.filter(
        quantity__lte=models.F("low_stock_threshold")
    ).count()

    expired_medicines = medicines.filter(
        expiry_date__lt=today
    ).count()

    expiring_soon_medicines = medicines.filter(
        expiry_date__gte=today,
        expiry_date__lte=expiry_warning_date
    ).count()

    return render(
        request,
        "pharmacy/dashboard.html",
        {
            "total_medicines": total_medicines,
            "low_stock_medicines": low_stock_medicines,
            "expired_medicines": expired_medicines,
            "expiring_soon_medicines": expiring_soon_medicines,
        }
    )

@login_required
def increase_stock(request, medicine_id):

    medicine = Medicine.objects.get(id=medicine_id)

    if request.method == "POST":

        form = StockForm(request.POST)

        if form.is_valid():

            quantity = form.cleaned_data["quantity"]

            medicine.quantity += quantity
            medicine.save()

            return redirect("medicine_list")

    else:
        form = StockForm()

    return render(
        request,
        "pharmacy/stock.html",
        {
            "form": form,
            "medicine": medicine,
            "action": "Increase",
        }
    )

@login_required
def decrease_stock(request, medicine_id):

    medicine = Medicine.objects.get(id=medicine_id)

    if request.method == "POST":

        form = StockForm(request.POST)

        if form.is_valid():

            quantity = form.cleaned_data["quantity"]

            if quantity <= medicine.quantity:

                medicine.quantity -= quantity
                medicine.save()

                return redirect("medicine_list")

            form.add_error(
                "quantity",
                "Stock cannot be less than 0."
            )

    else:
        form = StockForm()

    return render(
        request,
        "pharmacy/stock.html",
        {
            "form": form,
            "medicine": medicine,
            "action": "Decrease",
        }
    )

@login_required
def dispense_medicine(request, medicine_id):

    medicine = Medicine.objects.get(id=medicine_id)

    if request.method == "POST":

        form = MedicineSaleForm(request.POST)

        if form.is_valid():

            patient = form.cleaned_data["patient"]
            quantity = form.cleaned_data["quantity"]

            if quantity > medicine.quantity:

                form.add_error(
                    "quantity",
                    "Not enough medicine in stock."
                )

            else:

                total_price = medicine.price * quantity

                MedicineSale.objects.create(
                    patient=patient,
                    medicine=medicine,
                    quantity=quantity,
                    total_price=total_price,
                )

                medicine.quantity -= quantity
                medicine.save()

                return redirect("medicine_list")

    else:
        form = MedicineSaleForm()

    return render(
        request,
        "pharmacy/dispense_medicine.html",
        {
            "form": form,
            "medicine": medicine,
        }
    )