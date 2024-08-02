from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .form import *

# Create your views here.

def inicio(request):
    return render(request, 'index.html')


def registro_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            email = form.cleaned_data['email']
            Cliente.objects.create(nombre=nombre, apellido=apellido, email=email)
            Cliente.save()
            return render(request, 'index.html', {'form': form})
    else: 
        form = ClienteForm()
    return render(request, 'index.html', {'form': form})


def buscar_cliente(request):
    if request.method == 'POST':
        form = BuscarForm(request.POST)
        if form.is_valid():
            email= form.cleaned_data['email']
#busqueda de cliente por mail
            resultados = Cliente.objects.filter(email=email).first
            if Cliente:
                return render(request, 'index.html', {'cliente': Cliente})
            else:
                form.add_error(None, "Cliente no encontrado.")
    
    return render(request, 'buscar_cliente.html', {'form': form, 'resultados': resultados})