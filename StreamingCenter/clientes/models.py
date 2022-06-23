from django.db import models
import uuid


class Cliente(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    fechaVencimiento = models.DateField()
    email = models.EmailField(max_length=254)
    contraseña = models.CharField(max_length=30)
    servicio = models.CharField(max_length=30)
    def __str__(self):
        return self.nombre + " " + self.apellido + " " + str(self.servicio)
    def datetime_string(self):
        return self.fechaVencimiento.strftime("%Y-%m-%d")
    
     
class Empleados(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    area = models.CharField(max_length=30)
    antiguedad_meses = models.IntegerField()
    def __str__(self):
        return self.nombre + " " + self.apellido + " " + self.area + " " + str(self.antiguedad_meses)
    
class Servicios(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=200)
    precio = models.IntegerField()
    def __str__(self):
        return self.nombre + " " + str(self.precio) + " " + self.descripcion