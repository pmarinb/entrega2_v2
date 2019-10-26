from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .models import Vehiculo
from .forms import VehiculoForm

# Create your views here.
def agregar_carrera(request):
    if request.method == "POST":
        form = VehiculoForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.save()
            return redirect('/usuarios/base')
    else:
        form = VehiculoForm()
        return render(request, 'producto/agregar_vehiculo.html',
                      {'form': form})
