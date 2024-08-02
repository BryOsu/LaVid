from django.urls import path
from .views import *


urlpatterns = [
    path('', registro_cliente),
    path('',inicio),
    path('',buscar_cliente),
    path('registro-exitoso',lambda request: HttpResponse('Registro exitoso'),name='registro-exitoso')
]

