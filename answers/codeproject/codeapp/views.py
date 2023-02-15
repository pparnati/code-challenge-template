from django.shortcuts import render
from django.template import context
from rest_framework.decorators import api_view
from sqlparse.filters import output
from django.core.paginator import Paginator
from .serializers import WeatherDataSerializer
from rest_framework.response import Response
from . models import WeatherData
from django.http import HttpResponse
from django.db import transaction
from django.db import connection
from django.http import HttpResponse

def weather(request):
    weatherData1 = WeatherData.objects.raw("Select * from codeapp_weatherdata")
    p=Paginator(weatherData1,20)
    page_num =request.GET.get('page',1)
    page2 =p.page(page_num)
    context ={'weatherDatas' : page2}
    return render(request, 'output.html', context)


# @api_view(['GET'])
# def getData(request):
#     with transaction.atomic(): # Here
#         with connection.cursor() as cursor:
#             cursor.execute('''select avg(maxtempofday) , theyear , weatherstation from codeapp_weatherdata group by theyear , weatherstation;''')
#
#             for row in cursor.fetchall():
#                 print(row)
#
#     return HttpResponse("Test")

@api_view(['GET'])
def stats(request):
    statsData = WeatherData.objects.raw("select id ,  avg(maxtempofday) ,weatherdate ,weatherstation as 'averagetemp' from codeapp_weatherdata where maxtempofday != -9999 group by weatherdate , weatherstation")
    p = Paginator(statsData, 20)
    page_num = request.GET.get('page', 1)
    page2 = p.page(page_num)
    context = {'statsDatas': page2}
    return render(request, 'stats.html', context)
