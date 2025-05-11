# forms.py
from django import forms
from .models import Driver


class DriverForm(forms.ModelForm):
    # Add a checkbox for car ownership
    car_not_owned = forms.BooleanField(
        required=False,
        label="The car isn't owned by me"
    )

    class Meta:
        model = Driver
        fields = [
            'phone_number', 'city', 'status',
            'id_document', 'car_info_document', 'car_video', 'personal_photo',
            'additional_document'
        ]
        widgets = {
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'id_document': forms.FileInput(attrs={'class': 'form-control'}),
            'car_info_document': forms.FileInput(attrs={'class': 'form-control'}),
            'car_video': forms.FileInput(attrs={'class': 'form-control'}),
            'personal_photo': forms.FileInput(attrs={'class': 'form-control'}),
            'additional_document': forms.FileInput(attrs={'class': 'form-control'}),
        }
