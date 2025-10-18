from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('contacto/', views.contacto, name="contacto"),
    path('musica/', views.musica, name="musica")
]
