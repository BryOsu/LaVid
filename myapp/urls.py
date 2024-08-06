from django.urls import path
from .views import *


urlpatterns = [
    path('', registro_cliente,name="registro_cliente"),
    path('buscar',buscar_cliente,name="Buscar_cliente"),
]

