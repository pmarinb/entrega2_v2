from django.shortcuts import render, redirect
from .forms import RegistroForm

# Create your views here.


def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home')
    else:
        form = RegistroForm()
    
    return render(request, 'usuario/registro.html', {'form': form})

def base(request):
    return render(request, 'base/base.html',{})

    