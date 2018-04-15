from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login

from django.contrib.auth import login, logout
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import messages
from wateringApp.models import Statistics

def index(request):
    """Strona główna aplikacji."""
    # return HttpResponse("Witaj w aplikacji!")
    return render(request, 'wateringApp/index.html')

def singIn(request):
    """Logowanie"""
    from django.contrib.auth.forms import authentication
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            messages.success(request,"Zostałeś zalogowany!")
            return redirect(reverse('wateringApp:index'))
        
    context = {'form': AuthenticationForm()}
    return render(request,'wateringApp/singIn.html', context)

def singOut(request):
    """Wylogowywanie"""
    logout(request)
    messages.info(request,"Zostałeś wylogowany!")
    return redirect(reverse('wateringApp:index'))

def readOut(request):
    """Odczyty"""
    sensors = Statistics.objects.all()
    context = {'sensors': sensors}
    return render(request, 'wateringApp/readOut.html', context)