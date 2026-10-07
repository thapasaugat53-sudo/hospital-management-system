from django import forms
from .models import Bed
from patients.models import Patient


class AdmissionForm(forms.Form):
    patient = forms.ModelChoiceField(
        queryset=Patient.objects.all(),
        label="Patient"
    )

    bed = forms.ModelChoiceField(
        queryset=Bed.objects.filter(is_occupied=False),
        label="Available Bed"
    )