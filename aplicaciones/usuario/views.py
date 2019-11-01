from django.shortcuts import render, redirect
from .forms import RegistroForm
from django.contrib import messages

# Create your views here.


def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            usuario = form.cleaned_data.get('username')
            messages.success(request, f'Usuario: {usuario} Creado Exitosamente!')
            return redirect('home')
    else:
        form = RegistroForm()
    
    return render(request, 'usuario/registro.html', {'form': form})


    