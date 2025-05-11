from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Driver
from unfold.admin import ModelAdmin


@admin.register(Driver)
class DriverAdmin(ModelAdmin):
    # Fields to display in the list view
    list_display = ('phone_number', 'city', 'status', 'created_at')

    # Fields for searching
    search_fields = ['phone_number', 'city']

    # Filters in the right sidebar
    list_filter = ('status', 'city', 'created_at')

    # Fields organized into fieldsets for better form layout
    fieldsets = (
        ('Basic Information', {
            'fields': ('phone_number', 'city', 'status')
        }),
        ('Required Documents', {
            'fields': ('id_document', 'car_info_document', 'car_video', 'personal_photo')
        }),
        ('Additional Documents', {
            'fields': ('additional_document',)
        }),
    )

    # Readonly fields for viewing record history
    readonly_fields = ('created_at', 'updated_at')

    # Date hierarchy for navigating by created date
    date_hierarchy = 'created_at'