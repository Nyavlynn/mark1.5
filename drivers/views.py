from django.shortcuts import render

# Create your views here.
# views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import DriverForm


def driver_registration(request):
    if request.method == 'POST':
        form = DriverForm(request.POST, request.FILES)
        if form.is_valid():
            # Remove car_not_owned as it's not part of the model
            driver = form.save(commit=False)
            driver.save()
            messages.success(request, "Driver registration successful!")
            return redirect('registration_success')
    else:
        form = DriverForm()

    return render(request, 'drivers/registration.html', {'form': form})


def registration_success(request):
    return render(request, 'drivers/success.html')
