from django.urls import path, include
from . import views

urlpatterns = [
    path('agregar', views.agregar_vehiculo, name="agregar"),
    path('buscar', views.busqueda, name="buscar"),
]