from django.http import HttpResponse
from django.shortcuts import render
from clientes.models import Cuenta, Cliente
from django.template import loader

# Create your views here.
def cuentas(request):
    lista_cuentas = Cuenta.objects.all()
    return render(request, "clientes.html", {"cuentas" : lista_cuentas})

def clientela(request):
    lista_clientes = Cliente.objects.all()
    return render(request, "login.html", {"clientes" : lista_clientes} )

def inicio(self):
    plantilla = loader.get_template('index.html')
    documento = plantilla.render()
    return HttpResponse(documento)