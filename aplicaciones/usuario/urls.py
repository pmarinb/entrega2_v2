from django.urls import path, include
from . import views

urlpatterns = [
    path('registro', views.registro),
    path('base', views.base),
]