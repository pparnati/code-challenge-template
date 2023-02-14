from django.db import models


# Create your models here.
class WeatherData(models.Model):
    weatherdate=models.CharField(max_length=8)
    weatherstation = models.CharField(max_length=16, default=None, blank=True, null=True)
    maxtempofday=models.IntegerField(default=None, blank=True, null=True)
    mintempofday = models.IntegerField(default=None, blank=True, null=True)
    precipofday = models.IntegerField(default=None, blank=True, null=True)
    theyear = models.IntegerField(default=None, blank=True, null=True)

class YieldData(models.Model):
        year = models.CharField(max_length=4)
        yieldoftheyear = models.IntegerField(default=None, blank=True, null=True)

