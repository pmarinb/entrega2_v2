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
        labels = {
            'marca' :'Marca',
            'year':'Año Produccion',
            'modelo':'Modelo',
            'motor':'Motor',
            'precio':'Precio',            
            'imgFront':'Imagen Frontal',
            'imgSide':'Imagen Lateral',
            'imgBack':'Imagen Trasera',
            'imgInside':'Imagen Interior',
        }