from django.urls import path

from . import views

app_name = 'wateringApp'
urlpatterns = [
    path('', views.index, name='index'),
    path('singIn', views.singIn, name='singIn'),
    path('singOut', views.singOut, name='singOut'),
    path('readOut', views.readOut, name='readOut')
]
