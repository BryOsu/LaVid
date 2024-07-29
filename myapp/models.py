from django.db import models
from django.contrib.auth import get_user_model

user= get_user_model

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()


class Bodegas(models.Model):
    nombre = models.CharField(max_length=40)
    cantidad = models.IntegerField()

class Stock(models.Model):
    nombre = models.CharField(max_length=40)
    disponible = models.BooleanField()