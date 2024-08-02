from django.urls import path
from .views import *


urlpatterns = [
    path('', registro_cliente),
    path('',inicio),
    path('buscar',buscar_cliente,name="Resultado_Busqueda"),
]

