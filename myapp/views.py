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
            user_exists = Cliente.objects.filter(email=form.cleaned_data['email']).exists()
            if user_exists:
                return HttpResponse("El usuario ya está registrado.")
            else:
                guardado=Cliente.objects.create(nombre=nombre, apellido=apellido, email=email)
                Cliente.save(guardado)
            return redirect('registro_cliente')
    else: 
        form = ClienteForm()
    return render(request, 'Index.html', {'form': form})


def buscar_cliente(request):
    if request.method == 'POST':
        form = BuscarForm(request.POST)
        if form.is_valid():
            email= form.cleaned_data['email']
#busqueda de cliente por mail
            cliente = Cliente.objects.filter(email=email).first
            if cliente:
                return render(request, 'Resultado_Busqueda.html', {'cliente': cliente})
            else:
                form.add_error(None, "Cliente no encontrado.")
    else:
        form=BuscarForm()
    
    return render(request, 'Index_Busqueda.html', {'form': form})