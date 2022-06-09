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





def buscar(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        cliente = Cliente.objects.filter(nombre__icontains=nombre)
        
        return render(request, 'clientes/mostrar_datos.html', {'clientes': cliente})
    else:
        respuesta = "No se encontraron resultados"
        
    return HttpResponse(respuesta)












def clientes_formulario(request):
    
    if request.method == 'POST':
        miFormulario = Cliente_formulario(request.POST)
        
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            
            cliente = Cliente(nombre = informacion['nombre'], apellido = informacion['apellido'], fechaVencimiento = informacion['fechaVencimiento'], email = informacion['email'], contraseña = informacion['contraseña'], servicio = informacion['servicio'])
            
            cliente.save()
            
            return render(request, 'clientes/inicio.html')
    else:
        miFormulario = Cliente_formulario()
            
    return render(request, 'clientes/clientes_template.html', {'formulario': miFormulario})

def eliminar_cliente(request, id):
    cliente = Cliente.objects.get(id=id)
    cliente.delete()
    
    clientes = Cliente.objects.all()
    contexto = {'clientes': clientes}
    return render(request, 'clientes/inicio.html')

def editar_cliente(request, id):
    cliente = Cliente.objects.get(id=id)
    
    if request.method == 'POST':
        formulario_cliente = Cliente_formulario(request.POST)
        
        if formulario_cliente.is_valid():
            informacion = formulario_cliente.cleaned_data
            
            cliente.nombre = informacion['nombre']
            cliente.apellido = informacion['apellido']
            cliente.fechaVencimiento = informacion['fechaVencimiento']
            cliente.email = informacion['email']
            cliente.contraseña = informacion['contraseña']
            cliente.servicio = informacion['servicio']
            
            cliente.save()
            
            return render(request, 'clientes/inicio.html')
    else:
        formulario_cliente = Cliente_formulario(initial={'nombre': cliente.nombre, 'apellido': cliente.apellido, 'fechaVencimiento': cliente.fechaVencimiento, 'email': cliente.email, 'contraseña': cliente.contraseña, 'servicio': cliente.servicio})
    return render(request, 'clientes/clientes_template.html', {'formulario_clientes': formulario_cliente})













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


def eliminar_empleado(request, id):
    empleado = Empleados.objects.get(id=id)
    empleado.delete()
    
    empleados = Empleados.objects.all()
    contexto = {'empleados': empleados}
    return render(request, 'clientes/inicio.html')

def editar_empleado(request, id):
    empleado = Empleados.objects.get(id=id)
    
    if request.method == 'POST':
        formulario_empleado = Empleado_formulario(request.POST)
        
        if formulario_empleado.is_valid():
            informacion = formulario_empleado.cleaned_data
            
            empleado.nombre = informacion['nombre']
            empleado.apellido = informacion['apellido']
            empleado.area = informacion['area']
            empleado.antiguedad_meses = informacion['antiguedad_meses']
            
            empleado.save()
            
            return render(request, 'clientes/inicio.html')
    else:
        formulario_empleado = Empleado_formulario(initial={'nombre': empleado.nombre, 'apellido': empleado.apellido, 'area': empleado.area, 'antiguedad_meses': empleado.antiguedad_meses})
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


def eliminar_servicio(request, id):
    servicio = Servicios.objects.get(id=id)
    servicio.delete()
    
    servicios = Servicios.objects.all()
    contexto = {'servicios': servicios}
    return render(request, 'clientes/inicio.html')

def editar_servicio(request, id):
    servicio = Servicios.objects.get(id=id)
    
    if request.method == 'POST':
        formulario_servicio = Servicio_formulario(request.POST)
        
        if formulario_servicio.is_valid():
            informacion = formulario_servicio.cleaned_data
            
            servicio.nombre = informacion['nombre']
            servicio.descripcion = informacion['descripcion']
            servicio.precio = informacion['precio']
            
            servicio.save()
            
            return render(request, 'clientes/inicio.html')
    else:
        formulario_servicio = Servicio_formulario(initial={'nombre': servicio.nombre, 'descripcion': servicio.descripcion, 'precio': servicio.precio})
    return render(request, 'clientes/servicios_template.html', {'formulario_servicios': formulario_servicio})