from django.urls import path

from . import views

app_name = 'wateringApp'
urlpatterns = [
    path('', views.index, name='index'),
    path('statistics', views.statistics, name='statistics'),
    path('flowers', views.flowers, name='flowers'),
    path('settings', views.settings, name='settings'),
    path('api/data', views.get_data, name='api-data'),
    # do zrobienia później: logowanie, wylogowywanie
    # path('singIn', views.singIn, name='singIn'),
    # path('singOut', views.singOut, name='singOut'),
]
