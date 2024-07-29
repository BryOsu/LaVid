from django.urls import path
from myapp.views import *


urlpatterns = [
    path('home', LaVid),
    path("stock", Stock),
    path("Bodegas", Bodegas),
    path("Cliente", Cliente),
]