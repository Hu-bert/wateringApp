from django.db import models
from django.contrib.auth.models import User

class Statistics(models.Model):
    sensor_choices = (
        ('temperature', 'temperature'),
        ('waterContent', 'water content'),
        ('lumen', 'lumen'),
    )

    sensor = models.CharField(
        max_length=15,
        choices=sensor_choices,
        default='temperature')
    value = models.CharField(max_length=20)
    dataPub = models.DateField(auto_now_add=True)

    class Meta:  # ustawienia dodatkowe
        ordering = ['dataPub']  # domyślne porządkowanie danych

    def __str__(self):
        return self.sensor
