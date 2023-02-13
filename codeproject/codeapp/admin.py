from django.contrib import admin

# Register your models here.
from . models import WeatherData
from . models import YieldData

admin.site.register(WeatherData)
admin.site.register(YieldData)