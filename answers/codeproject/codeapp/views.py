from django.shortcuts import render
from . models import WeatherData
from django.http import HttpResponse
from django.db import transaction
from django.db import connection
from django.http import HttpResponse

def weather(request):
    weatherData1=WeatherData.maxtempofday
    return HttpResponse(weatherData1)



def test(request):
    with transaction.atomic(): # Here
        with connection.cursor() as cursor:
            cursor.execute('''select avg(maxtempofday) , theyear , weatherstation from codeapp_weatherdata group by theyear , weatherstation;''')

            for row in cursor.fetchall():
                print(row)

    return HttpResponse("Test")