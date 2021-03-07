from django.contrib import admin
from django.urls import path
from app.views import *
from django.contrib.staticfiles.urls import static
urlpatterns = [
    path("",index),
    path("404/",error)
]
