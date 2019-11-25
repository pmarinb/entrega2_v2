from rest_framework import viewsets
from aplicaciones.producto.models import Vehiculo
from .serializer import VehiculoSerializer
from .permissions import IsAdminUserOrReadOnly

class VehiculoViewSet(viewsets.ModelViewSet):
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoSerializer
    permission_classes = [IsAdminUserOrReadOnly]