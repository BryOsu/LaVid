from django.urls import path
from .views import *


urlpatterns = [
    path('', inicio),
    path('',registro_cliente),
    path('',buscar_cliente),
]

