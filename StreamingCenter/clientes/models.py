from django.db import models
import uuid


class Cuenta(models.Model):
    id = models.CharField(default=uuid.uuid4(), primary_key = True, max_length=100)
    email = models.EmailField()
    contraseña = models.CharField(max_length=10)
    servicios_elegir = [
        ('NETFLIX', 'NETFLIX'),
        ('AMAZON', 'AMAZON'),
        ('DISNEY', 'DISNEY'),
    ]
    servicio = models.CharField(max_length=30, choices=servicios_elegir, blank=True, null=True)
    def __str__(self):
        return self.email + " " + str(self.contraseña)
    
    
class Cliente(models.Model):
    id = models.CharField(default=uuid.uuid4(), primary_key = True, max_length=100)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    fechaVencimiento = models.DateField()
    cuenta = models.ForeignKey(Cuenta, null=True, on_delete=models.CASCADE)
    servicios_elegir = [
        ('NETFLIX', 'NETFLIX'),
        ('AMAZON', 'AMAZON'),
        ('DISNEY', 'DISNEY'),
    ]
    servicio = models.CharField(max_length=30, choices=servicios_elegir, blank=True, null=True)
    def __str__(self):
        return self.nombre + " " + self.apellido + " " + str(self.servicio)
    
     