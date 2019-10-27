from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .models import Vehiculo
from .forms import VehiculoForm

from django.contrib import messages

# Create your views here.
def agregar_vehiculo(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()            
            modelo = form.cleaned_data.get('modelo')
            messages.success(request, f'Vehiculo Modelo: {modelo} Agregado!')
            return redirect('/producto/agregar')
    else:
        form = VehiculoForm()
    return render(request, 'producto/agregar_vehiculo.html', {'form': form})