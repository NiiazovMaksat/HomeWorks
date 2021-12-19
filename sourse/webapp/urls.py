from django.contrib import admin
from django.urls import path

from webapp.views import calculete

urlpatterns = [
    path("", calculete)
]