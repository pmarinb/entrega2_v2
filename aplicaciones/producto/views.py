from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .models import Vehiculo
from .forms import VehiculoForm
from .filters import VehiculoFilter

from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.
@staff_member_required(login_url='home')
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

@staff_member_required(login_url='home')
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

#busqueda o listar, cumplen la misma funcion
@staff_member_required(login_url='home')
def busqueda(request):
    vehiculo_list = Vehiculo.objects.all()
    vehiculo_filter = VehiculoFilter(request.GET, queryset=vehiculo_list)
    return render(request, 'producto/busqueda_vehiculo.html', {'filter': vehiculo_filter})

@staff_member_required(login_url='home')
def eliminar(request, vehiculo_id):
    instacia= Vehiculo.objects.get(id=vehiculo_id)
    instacia.delete()
    messages.warning(request, f'Vehiculo de Marca: {instacia.marca}, Modelo: {instacia.modelo} Eliminado!')
    return redirect('/producto/buscar')

def home(request):
    productos = Vehiculo.objects.all()
    return render(request, 'producto/home/home.html', {'productos': productos})

def vehiculo_info(request, vehiculo_id):
    producto= Vehiculo.objects.get(id=vehiculo_id)
    return render(request, 'producto/home/vehiculo_info.html', {'producto': producto})

def comprar_vehiculo(request, vehiculo_id):
    producto= Vehiculo.objects.get(id=vehiculo_id)
    producto.vendido = True
    producto.save()
    messages.success(request, f'Vehiculo de Marca: {producto.marca}, Modelo: {producto.modelo} Comprado!')
    return redirect('/')