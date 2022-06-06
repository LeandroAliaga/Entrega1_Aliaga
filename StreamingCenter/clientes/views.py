from django.http import HttpResponse
from django.shortcuts import render
from clientes.models import Cuenta, Cliente
from django.template import loader
from clientes.forms import NetflixFormulario

# Create your views here.
def clientela(request):
    lista_cuentas = Cuenta.objects.all()
    return render(request, "clientes.html", {"cuentas" : lista_cuentas})

def cuentas(request):
    lista_clientes = Cliente.objects.all()
    return render(request, "cuentas.html", {"clientes" : lista_clientes} )

def inicio(self):
    plantilla = loader.get_template('inicio.html')
    documento = plantilla.render()
    return HttpResponse(documento)

def netflix(request):
    return render(request, 'netflix.html')

def netflixFormulario(request):
    if request.method == 'POST':
        formulario = NetflixFormulario(request.POST)
        
        print(formulario)
        
        if formulario.is_valid:
            informacion = formulario.cleaned_data
           
        
            cliente = Cliente (nombre=informacion['nombre'], apellido=informacion['apellido'])
            
            cliente.save()
    
           
            return render(request, '/clientes/inicio.html')
        
    else:
        formulario = NetflixFormulario()
    return render(request, 'clientes/netflix.html', {'netflixformulario' : formulario})

def amazon(request):
    return render(request, 'amazon.html')

def spotify(request):
    return render(request, 'spotify.html')

def disney(request):
    return render(request, 'disney.html')