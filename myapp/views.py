from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.

def inicio(request):
    return render(request, 'index.html')

def LaVid(request):
    return HttpResponse(request,"Bienvenidos a LaVid, creamos experiencias")

def lista_Vinos(request):
    vino=Bodegas.objects.all().order_by('nombre')
    return render(request,'bodegas.lista.html')


def lista_Clientes(request):
    vino=Cliente.objects.all().order_by('nombre')
    return render(request,'cliente.lista.html')