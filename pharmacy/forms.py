from django import forms
from .models import Medicine
from patients.models import Patient


class MedicineForm(forms.ModelForm):

    class Meta:
        model = Medicine
        fields = [
            "name",
            "quantity",
            "price",
            "expiry_date",
            "low_stock_threshold",
        ]

        widgets = {
            "expiry_date": forms.DateInput(
                attrs={"type": "date"}
            ),
        }


class StockForm(forms.Form):

    quantity = forms.IntegerField(
        min_value=1,
        label="Quantity"
    )

class MedicineSaleForm(forms.Form):

    patient = forms.ModelChoiceField(
        queryset=Patient.objects.all()
    )

    quantity = forms.IntegerField(
        min_value=1
    )