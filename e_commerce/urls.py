
from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('store/', views.say_hello)
]
