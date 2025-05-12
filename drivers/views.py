from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from .forms import DriverForm
from .models import Driver


def driver_registration(request):
    if request.method == 'POST':
        driver_id = request.POST.get('driver_id')
        if driver_id:
            driver = Driver.objects.get(id=driver_id)
            form = DriverForm(request.POST, request.FILES, instance=driver)
        else:
            form = DriverForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            messages.success(request, "Driver registration successful!")
            return redirect('registration_success')
    else:
        form = DriverForm()

    return render(request, 'drivers/registration.html', {'form': form})


def registration_success(request):
    return render(request, 'drivers/success.html')


@csrf_exempt
def save_step_one(request):
    if request.method == 'POST':
        phone = request.POST.get('phone_number')
        city = request.POST.get('city')
        status = request.POST.get('status')

        if not phone or not city or not status:
            return JsonResponse({'success': False, 'error': 'Missing required fields'}, status=400)

        driver = Driver.objects.create(
            phone_number=phone,
            city=city,
            status=status
        )

        return JsonResponse({'success': True, 'driver_id': driver.id})
    
    return JsonResponse({'success': False}, status=400)
