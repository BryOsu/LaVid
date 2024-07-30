from django.shortcuts import render
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
    else:    
        form = ClienteForm()

    return render(request, 'index.html', {'form': form})


def buscar_cliente(request):
    form = BuscarForm()
    resultados = []
    
    if request.method == 'POST':
        form = BuscarForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            resultados = Cliente.objects.filter(email__icontains=query)
    
    return render(request, 'index.html', {'form': form, 'resultados': resultados})