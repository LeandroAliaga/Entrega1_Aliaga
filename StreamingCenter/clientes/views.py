from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .forms import Cliente_formulario , Empleado_formulario, Servicio_formulario
from .models import Cliente, Servicios, Empleados

def inicio(request):
    return render(request, 'clientes/inicio.html')
def mostrarDatos(request):
    clientes = Cliente.objects.all()
    empleados = Empleados.objects.all()
    servicios = Servicios.objects.all()
    
    
    return render(request, 'clientes/mostrar_datos.html', {'clientes': clientes, 'empleados': empleados, 'servicios': servicios})

def clientes_formulario(request):
    
    if request.method == 'POST':
        miFormulario = Cliente_formulario(request.POST)
        
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            
            cliente = Cliente(nombre = informacion['nombre'], apellido = informacion['apellido'], fechaVencimiento = informacion['fechaVencimiento'], email = informacion['email'], contraseña = informacion['contraseña'], servicio = informacion['servicio'])
            
            cliente.save()
            
            return render(request, 'clientes/clientes_template.html')
    else:
        miFormulario = Cliente_formulario()
            
    return render(request, 'clientes/clientes_template.html', {'formulario': miFormulario})
        



def empleados_formulario(request):
    
    if request.method == 'POST':
        formulario_empleado = Empleado_formulario(request.POST)
        
        if formulario_empleado.is_valid():
            informacion = formulario_empleado.cleaned_data
            
            empleado = Empleados(nombre = informacion['nombre'], apellido = informacion['apellido'], area = informacion['area'], antiguedad_meses = informacion['antiguedad_meses'])
            
            empleado.save()
            
            return render(request, 'clientes/inicio.html')
    else:
        formulario_empleado = Empleado_formulario()
        
    return render(request, 'clientes/empleados_template.html', {'formulario_empleados': formulario_empleado})


def servicios_formulario(request):
    
    if request.method == 'POST':
        formulario_servicio = Servicio_formulario(request.POST)
        
        if formulario_servicio.is_valid():
            informacion = formulario_servicio.cleaned_data
            
            servicio = Servicios(nombre = informacion['nombre'], descripcion = informacion['descripcion'], precio = informacion['precio'])
            
            servicio.save()
            
            return render(request, 'clientes/inicio.html')
    else:
        formulario_servicio = Servicio_formulario()
        
    return render(request, 'clientes/servicios_template.html', {'formulario_servicios': formulario_servicio})