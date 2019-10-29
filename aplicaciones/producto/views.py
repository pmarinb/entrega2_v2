from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .models import Vehiculo
from .forms import VehiculoForm
from .filters import VehiculoFilter

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
    return render(request, 'producto/agregar_vehiculo.html', {'form': form, 'titulo': 'Agregar'})

def editar_vehiculo(request, vehiculo_id):
    instancia= Vehiculo.objects.get(id=vehiculo_id)
    form=  VehiculoForm(instance=instancia)
    if request.method=="POST":
        form= VehiculoForm(request.POST, request.FILES, instance=instancia)
        if form.is_valid():
            instancia= form.save(commit=False)
            instancia.save()
            modelo = form.cleaned_data.get('modelo')
            messages.success(request, f'Vehiculo Modelo: {modelo} Modificado!')
            return redirect('/producto/buscar')
    return render(request, "producto/agregar_vehiculo.html",{'form': form, 'titulo': 'Modificar'})  

def busqueda(request):
    vehiculo_list = Vehiculo.objects.all()
    vehiculo_filter = VehiculoFilter(request.GET, queryset=vehiculo_list)
    return render(request, 'producto/busqueda_vehiculo.html', {'filter': vehiculo_filter})

