from django.urls import path
from .views import *


urlpatterns = [
    path('', registro_cliente),
    path('buscar',buscar_cliente,name="Resultado_Busqueda"),
]

