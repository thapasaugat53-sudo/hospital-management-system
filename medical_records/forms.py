from django import forms
from .models import MedicalRecord


class MedicalRecordForm(forms.ModelForm):

    class Meta:
        model = MedicalRecord
        fields = [
            "diagnosis",
            "symptoms",
            "treatment",
            "notes",
        ]

        widgets = {
            "diagnosis": forms.Textarea(attrs={
                "rows": 3,
                "placeholder": "Enter diagnosis"
            }),

            "symptoms": forms.Textarea(attrs={
                "rows": 3,
                "placeholder": "Enter symptoms"
            }),

            "treatment": forms.Textarea(attrs={
                "rows": 3,
                "placeholder": "Enter treatment"
            }),

            "notes": forms.Textarea(attrs={
                "rows": 3,
                "placeholder": "Additional notes"
            }),
        }