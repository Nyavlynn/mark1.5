from django.db import models

# Create your models here.

from django.db import models


class Driver(models.Model):
    # Status choices
    STATUS_CHOICES = [
        ('NEW', 'New Driver'),
        ('INFO_CHANGE', 'Information Change'),
    ]

    # Basic information
    phone_number = models.CharField(max_length=15)
    city = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    # Required file fields
    id_document = models.FileField(upload_to='drivers/id_documents/')
    car_info_document = models.FileField(upload_to='drivers/car_info/')
    car_video = models.FileField(upload_to='drivers/car_videos/')
    personal_photo = models.ImageField(upload_to='drivers/personal_photos/')

    # Optional file field
    additional_document = models.FileField(upload_to='drivers/additional_docs/', null=True, blank=True)

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Driver: {self.phone_number} ({self.get_status_display()})"