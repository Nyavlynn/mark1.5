# forms.py
from django import forms
from .models import Driver

# Iraqi governorates with default placeholder
CITY_CHOICES = [
    ('', 'اختر المحافظة'),
    ('baghdad', 'بغداد'),
    ('basra', 'البصرة'),
    ('najaf', 'النجف'),
    ('karbala', 'كربلاء'),
    ('babel', 'بابل'),
    ('diyala', 'ديالى'),
]

class DriverForm(forms.ModelForm):
    # Checkbox for car ownership

    # Override city as a ChoiceField with placeholder
    city = forms.ChoiceField(
        choices=CITY_CHOICES,
        label="المحافظة",
        widget=forms.Select(attrs={'class': 'form-select'})
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
            'status': forms.Select(attrs={'class': 'form-select'}),
            'id_document': forms.FileInput(attrs={'class': 'form-control'}),
            'car_info_document': forms.FileInput(attrs={'class': 'form-control'}),
            'car_video': forms.FileInput(attrs={'class': 'form-control'}),
            'personal_photo': forms.FileInput(attrs={'class': 'form-control'}),
            'additional_document': forms.FileInput(attrs={'class': 'form-control'}),
        }
