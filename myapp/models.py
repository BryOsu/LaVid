from django.db import models
from django.contrib.auth import get_user_model

user= get_user_model

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField(unique=True)
    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    @classmethod
    def buscar_por_email(cls, email):
        return cls.objects.filter(email=email).first()
    

class Bodegas(models.Model):
    nombre = models.CharField(max_length=40)
    cantidad = models.IntegerField()
    anio = models.CharField(max_length=4)

class Stock(models.Model):
    nombre = models.CharField(max_length=40)
    disponible = models.BooleanField()

