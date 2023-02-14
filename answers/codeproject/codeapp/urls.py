from django.contrib import admin
from django.urls import path
from rest_framework import request

from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('weather/', views.test),

]
