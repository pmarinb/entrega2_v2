from django import forms
from .models import Vehiculo

class VehiculoForm(forms.ModelForm):
    class Meta:
        model=Vehiculo
        fields=[
            'marca',
            'year',
            'modelo',
            'motor',
            'precio',            
            'imgFront',
            'imgSide',
            'imgBack',
            'imgInside',
        ]