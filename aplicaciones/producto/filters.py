from .models import Vehiculo
import django_filters

class VehiculoFilter(django_filters.FilterSet):
    class Meta:
        model = Vehiculo
        fields = [ 'marca', 'year','modelo',]
        