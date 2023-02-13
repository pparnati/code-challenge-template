from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from . models import WeatherData
from rest_framework.response import Response

class weather(APIView):
    def get(self,request):
        weatherData1=WeatherData.maxtempofday
        return Response(weatherData1)