from rest_framework import viewsets
from aplicaciones.producto.models import Vehiculo
from .serializer import VehiculoSerializer

class VehiculoViewSet(viewsets.ModelViewSet):
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoSerializer