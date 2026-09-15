from django import forms
from .models import LabTest


class LabTestForm(forms.ModelForm):

    class Meta:
        model = LabTest

        fields = [
            "test_name",
        ]

        widgets = {
            "test_name": forms.TextInput(
                attrs={
                    "placeholder": "Enter lab test name"
                }
            ),
        }


class LabResultForm(forms.ModelForm):

    class Meta:
        model = LabTest

        fields = [
            "result",
        ]

        widgets = {
            "result": forms.Textarea(
                attrs={
                    "placeholder": "Enter laboratory result",
                    "rows": 5
                }
            ),
        }