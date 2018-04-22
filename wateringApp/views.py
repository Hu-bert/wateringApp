from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login

from django.contrib.auth import login, logout
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import messages
from wateringApp.models import Statistics

def index(request):
    """Strona główna aplikacji."""
    currentTemperature = Statistics.objects.filter(sensor='temperature').last()
    currentTemperature.value= int(int(currentTemperature.value)*2.5)
    currentWaterContent = Statistics.objects.filter(sensor='waterContent').last()
    currentLumen = Statistics.objects.filter(sensor='lumen').last()
    context = {'temperature': currentTemperature,'waterContent': currentWaterContent,'lumen': currentLumen}
    # return HttpResponse("Witaj w aplikacji!")
    return render(request, 'wateringApp/index.html', context)

# do zrobienia logowanie, wylogowywanie
# def singIn(request):
#     """Logowanie"""
#     from django.contrib.auth.forms import AuthenticationForm
#     if request.method == 'POST':
#         form = AuthenticationForm(request, request.POST)
#         if form.is_valid():
#             login(request, form.get_user())
#             messages.success(request,"Zostałeś zalogowany!")
#             return redirect(reverse('wateringApp:index'))
        
#     context = {'form': AuthenticationForm()}
#     return render(request,'wateringApp/singIn.html', context)

# def singOut(request):
#     """Wylogowywanie"""
#     logout(request)
#     messages.info(request,"Zostałeś wylogowany!")
#     return redirect(reverse('wateringApp:index'))

def statistics(request):
    """Odczyty"""
    temperature = Statistics.objects.filter(sensor='temperature')
    waterContent = Statistics.objects.filter(sensor='waterContent')
    lumen = Statistics.objects.filter(sensor='lumen')
    context = {'temperature': temperature,'waterContent': waterContent,'lumen': lumen}
    return render(request, 'wateringApp/statistics.html', context)

def settings(request):
    """Ustawienia"""
    sensors = Statistics.objects.all()
    context = {'sensors': sensors}
    return render(request, 'wateringApp/settings.html', context)   

def get_data(request):
    temperature = Statistics.objects.filter(sensor='temperature').values('value', 'dataPub')
    temperature_list = list(temperature)
    waterContent = Statistics.objects.filter(sensor='waterContent').values('value', 'dataPub')
    waterContent_list = list(waterContent)
    lumen = Statistics.objects.filter(sensor='lumen').values('value', 'dataPub')
    lumen_list = list(lumen)
    data ={
        'temperature': temperature_list,
        'waterContent': waterContent_list,
        'lumen': lumen_list,
    }
    return JsonResponse(data)

def flowers(request):
    """Kwiaty"""
    sensors = Statistics.objects.all()
    context = {'sensors': sensors}
    return render(request, 'wateringApp/flowers.html', context)