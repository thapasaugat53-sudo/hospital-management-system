from django import forms
from .models import Bill


class BillForm(forms.ModelForm):

    class Meta:
        model = Bill

        fields = [
            "consultation_fee",
            "lab_charges",
            "medicine_charges",
            "payment_status",
        ]

        widgets = {
            "consultation_fee": forms.NumberInput(
                attrs={
                    "placeholder": "Enter consultation fee",
                    "step": "0.01"
                }
            ),

            "lab_charges": forms.NumberInput(
                attrs={
                    "placeholder": "Enter lab charges",
                    "step": "0.01"
                }
            ),

            "medicine_charges": forms.NumberInput(
                attrs={
                    "placeholder": "Enter medicine charges",
                    "step": "0.01"
                }
            ),
        }