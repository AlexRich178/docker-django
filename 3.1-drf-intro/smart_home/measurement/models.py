from django.db import models
from django.utils import timezone


class Sensor(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name


class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measure')
    temperature = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
