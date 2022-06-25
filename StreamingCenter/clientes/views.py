from django.http import Http404, HttpResponse
from django.shortcuts import redirect, render
from django.template import loader
from .forms import Cliente_formulario , Empleado_formulario, Servicio_formulario, UserRegistrationForm, UserEditForm
from .models import Cliente, Servicios, Empleados, Avatar
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView, View
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required



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
#EDITAR PERFIL

@login_required
def editarPerfil(request):
    usuario = request.user
    
    if request.method == 'POST':
        formulario = UserEditForm(request.POST, instance=usuario)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.save()
            return render(request, 'clientes/inicio.html', {'mensaje': 'Perfil editado correctamente'})
    else:
        formulario = UserEditForm(instance=usuario)
    return render(request, 'clientes/editar_perfil.html', {'usuario':usuario.username,'formulario': formulario})










class registro(View):
    form_class = UserRegistrationForm
    initial = {'key': 'value'}
    template_name = 'clientes/register.html'
    
    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save()
            return render(request, 'clientes/inicio.html', {'mensaje': f'USUARIO {username} CREADO'})
        else:
            return render(request, 'clientes/inicio.html', {'mensaje': 'ERROR NO SE PUDO CREAR EL USUARIO'})
        
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('inicio')
        return super(registro, self).dispatch(request, *args, **kwargs)
    
#---------------------------------------------------------------------------------------------------------------------
#avatar

def avatar(request):
        avatar = Avatar.objects.filter(user=request.user.id)
        return render(request, 'clientes/inicio.html', {"imagen":avatar[0].imagen.url})
    






#---------------------------------------------------------------------------------------------------------------------
#inicio

class Inicio(LoginRequiredMixin,TemplateView):
    template_name = 'clientes/inicio.html'
    
    


#---------------------------------------------------------------------------------------------------------------------
#MOSTRAR DATOS CLIENTES CBV


class MostrarDatosClientes(LoginRequiredMixin, ListView):
    model = Cliente
    template_name = 'clientes/mostrar_datos_clientes.html'
    
    def get(self, request):
        clientes = Cliente.objects.all().order_by('-nombre')
        return render(request, self.template_name, {'clientes': clientes})
    
    


    
    

#---------------------------------------------------------------------------------------------------------------------
#MOSTRAR DATOS EMPLEADOS CBV

class mostrar_datos_empleados(LoginRequiredMixin, ListView):
    model = Empleados
    template_name = 'clientes/mostrar_datos_empleados.html'
    
    def get(self, request):
        empleados = Empleados.objects.all()
        return render(request, 'clientes/mostrar_datos_empleados.html', {'empleados': empleados})
#---------------------------------------------------------------------------------------------------------------------
#MOSTRAR DATOS SERVICIOS CBV


class MostrarDatosServicios(LoginRequiredMixin, ListView):
    model = Servicios
    template_name = 'clientes/mostrar_datos_servicios.html'
    
    def get(self, request):
        servicios = Servicios.objects.all()
        return render(request, 'clientes/mostrar_datos_servicios.html', {'servicios': servicios})




#---------------------------------------------------------------------------------------------------------------------
#clientes

@login_required
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


@login_required
def eliminar_cliente(request, id):
    cliente = Cliente.objects.get(id=id)
    cliente.delete()
    
    clientes = Cliente.objects.all()
    contexto = {'clientes': clientes}
    return render(request, 'mostrar_datos_clientes.html', contexto)


@login_required
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
            
            return render(request, 'clientes/inicio.html' , {'mensaje': 'CLIENTE EDITADO'})
    else:
        formulario_cliente = Cliente_formulario(initial={'nombre': cliente.nombre, 'apellido': cliente.apellido, 'fechaVencimiento': cliente.fechaVencimiento, 'email': cliente.email, 'contraseña': cliente.contraseña, 'servicio': cliente.servicio})
    return render(request, 'clientes/clientes_template.html', {'formulario_clientes': formulario_cliente})

class BuscarCliente(TemplateView):
    
    
    def post(self, request):
        buscar = request.POST['buscar_cliente']
        clientes = Cliente.objects.filter(nombre__icontains = buscar)
        return render(request, 'clientes/buscar_cliente.html', {'clientes': clientes})
    
    def get(self, request, *args, **kwargs):
        return render(request, 'clientes/buscar_cliente.html')
   
    



#---------------------------------------------------------------------------------------------------------------------
#Empleados

    



@login_required
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

@login_required
def eliminar_empleado(request, id):
    empleado = Empleados.objects.get(id=id)
    empleado.delete()
    
    empleados = Empleados.objects.all()
    contexto = {'empleados': empleados}
    return render(request, 'clientes/mostrar_datos_empleados.html', contexto)

@login_required
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
#Servicios
@login_required
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

@login_required
def eliminar_servicio(request, id):
    servicio = Servicios.objects.get(id=id)
    servicio.delete()
    
    servicios = Servicios.objects.all()
    contexto = {'servicios': servicios}
    return render(request, 'clientes/mostrar_datos_servicios.html', contexto)

@login_required
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





class Error404View(TemplateView):
    template_name = 'clientes/error404.html'
    