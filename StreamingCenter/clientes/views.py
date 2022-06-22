from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.template import loader
from .forms import Cliente_formulario , Empleado_formulario, Servicio_formulario, UserRegistrationForm
from .models import Cliente, Servicios, Empleados
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate


#---------------------------------------------------------------------------------------------------------------------
#LOGIN

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            clave = form.cleaned_data.get('password')
            #autenticacion
            user = authenticate(username=usuario, password=clave)
            if user is not None:
                login(request, user)
                return render(request, 'clientes/inicio.html', {'mensaje': f'Bienvenido {usuario}'})
            else:
                return render(request, 'clientes/inicio.html', {'mensaje': 'Usuario o contraseña incorrectos'})
        else:
            return render(request, 'clientes/inicio.html', {'mensaje': 'Usuario o contraseña incorrectos'})
    else:
        form = AuthenticationForm()
        return render(request, 'clientes/login.html', {'form': form, 'usuario': request.user})
        
#---------------------------------------------------------------------------------------------------------------------
#REGISTER

def register_request(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save()
            return render(request, 'clientes/inicio.html', {'mensaje': f'USUARIO {username} CREADO'})
        else:
            return render(request, 'clientes/inicio.html', {'mensaje': 'ERROR NO SE PUDO CREAR EL USUARIO'})
    else:
        form = UserRegistrationForm()
        return render(request, 'clientes/register.html', {'form': form})
            








#---------------------------------------------------------------------------------------------------------------------
#inicio

class Inicio(TemplateView):
    template_name = 'clientes/inicio.html'

#---------------------------------------------------------------------------------------------------------------------
#MOSTRAR DATOS CLIENTES

def mostrarDatosClientes(request):
    clientes = Cliente.objects.all()
    
    return render(request, 'clientes/mostrar_datos_clientes.html', {'clientes': clientes})

#---------------------------------------------------------------------------------------------------------------------
#MOSTRAR DATOS EMPLEADOS

def mostrarDatosEmpleados(request):
    empleados = Empleados.objects.all()
    
    return render(request, 'clientes/mostrar_datos_empleados.html', {'empleados': empleados})

#---------------------------------------------------------------------------------------------------------------------
#MOSTRAR DATOS SERVICIOS

def mostrarDatosServicios(request):
    servicios = Servicios.objects.all()
    return render(request, 'clientes/mostrar_datos_servicios.html', {'servicios': servicios})






#---------------------------------------------------------------------------------------------------------------------
#clientes


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
            
    return render(request, 'clientes/clientes_template.html', {'formulario_clientes': miFormulario})

def eliminar_cliente(request, id):
    cliente = Cliente.objects.get(id=id)
    cliente.delete()
    
    clientes = Cliente.objects.all()
    contexto = {'clientes': clientes}
    return render(request, 'mostrar_datos_clientes.html', contexto)

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



#---------------------------------------------------------------------------------------------------------------------
#clientes

def editar_empleado(request, id):
    empleado = Empleados.objects.get(id=id)
    




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
    return render(request, 'clientes/mostrar_datos_empleados.html', contexto)

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
            
            return render(request, 'clientes/mostrar_datos_empleados.html' )
    else:
        formulario_empleado = Empleado_formulario(initial={'nombre': empleado.nombre, 'apellido': empleado.apellido, 'area': empleado.area, 'antiguedad_meses': empleado.antiguedad_meses})
    return render(request, 'clientes/empleados_template.html', {'formulario_empleados': formulario_empleado})


#---------------------------------------------------------------------------------------------------------------------
#servicios

def servicios_formulario(request):
    
    if request.method == 'POST':
        formulario_servicio = Servicio_formulario(request.POST)
        
        if formulario_servicio.is_valid():
            informacion = formulario_servicio.cleaned_data
            
            servicio = Servicios(nombre = informacion['nombre'], descripcion = informacion['descripcion'], precio = informacion['precio'])
            
            servicio.save()
            
            return render(request, 'clientes/mostrar_datos_servicios.html')
    else:
        formulario_servicio = Servicio_formulario()
        
    return render(request, 'clientes/servicios_template.html', {'formulario_servicios': formulario_servicio})


def eliminar_servicio(request, id):
    servicio = Servicios.objects.get(id=id)
    servicio.delete()
    
    servicios = Servicios.objects.all()
    contexto = {'servicios': servicios}
    return render(request, 'clientes/mostrar_datos_servicios.html', contexto)

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



#---------------------------------------------------------------------------------------------------------------------
#CLASES BASADAS EN VISTAS 

class Cliente_list(ListView):
    model = Cliente
    template_name = 'clientes/mostrar.html'
    
    def __str__(self):
        return self.nombre + " " + self.apellido + " " + str(self.servicio) + " " + str(self.fechaVencimiento) + " " + self.email + " " + self.contraseña
    
class Cliente_detail(DetailView):
    model = Cliente
    template_name = 'clientes/detalle.html'


class Cliente_create(CreateView):
    model = Cliente
    success_url = reverse_lazy('mostrar')
    fields = ['nombre', 'apellido', 'servicio', 'fechaVencimiento', 'email', 'contraseña']
    
class Cliente_update(UpdateView):
    model = Cliente
    success_url = reverse_lazy('mostrar')
    fields = ['nombre', 'apellido', 'servicio', 'fechaVencimiento', 'email', 'contraseña']
    
class Cliente_delete(DeleteView):
    model = Cliente
    success_url = reverse_lazy('mostrar')