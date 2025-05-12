from django.db import models

class Driver(models.Model):
    # Status choices
    STATUS_CHOICES = [
        ('NEW', 'تسجيل جديد'),
        ('INFO_CHANGE', 'تغيير معلومات'),
    ]

    # Basic information
    phone_number = models.CharField(max_length=15)
    city = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    # File fields with structured upload paths
    id_document = models.FileField(upload_to='drivers/id_documents/%Y/%m/')
    car_info_document = models.FileField(upload_to='drivers/car_info/%Y/%m/')
    car_video = models.FileField(upload_to='drivers/car_videos/%Y/%m/')
    personal_photo = models.ImageField(upload_to='drivers/personal_photos/%Y/%m/')
    additional_document = models.FileField(upload_to='drivers/additional_docs/%Y/%m/', null=True, blank=True)

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Driver: {self.phone_number} ({self.get_status_display()})"
