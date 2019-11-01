from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('agregar', views.agregar_vehiculo, name="agregar"),
    path('buscar', views.busqueda, name="buscar"),
    path('editar_vehiculo/<int:vehiculo_id>', views.editar_vehiculo, name="modificar"),
    path('eliminar_vehiculo/<int:vehiculo_id>', views.eliminar, name="eliminar"),
    path('info/<int:vehiculo_id>', views.vehiculo_info, name="info"),
    path('comprar_vehiculo/<int:vehiculo_id>', views.comprar_vehiculo, name="comprar"),
]