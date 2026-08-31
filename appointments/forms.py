from django import forms
from .models import Appointment


class AppointmentForm(forms.ModelForm):

    class Meta:
        model = Appointment

        fields = [
            "doctor",
            "appointment_date",
            "appointment_time",
            "reason",
        ]

        widgets = {
            "appointment_date": forms.DateInput(
                attrs={"type": "date"}
            ),

            "appointment_time": forms.TimeInput(
                attrs={"type": "time"}
            ),

            "reason": forms.Textarea(
                attrs={
                    "rows": 4,
                    "placeholder": "Reason for appointment"
                }
            ),
        }