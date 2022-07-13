from django.http import Http404, HttpResponse
from django.shortcuts import redirect, render
from django.template import loader
from .forms import Cliente_formulario , Empleado_formulario, Servicio_formulario, UserRegistrationForm, UserEditForm
from .models import Cliente, Servicios, Empleados
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView, View
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.db.models import Q


#---------------------------------------------------------------------------------------------------------------------
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
            usuario.imagen = informacion['imagen']
            usuario.save()
            return render(request, 'clientes/inicio.html', {'mensaje': 'Perfil editado correctamente'})
    else:
        formulario = UserEditForm(instance=usuario)
    return render(request, 'clientes/editar_perfil.html', {'usuario':usuario.username,'formulario': formulario})






#---------------------------------------------------------------------------------------------------------------------
#REGISTRARSE


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
#---------------------------------------------------------------------------------------------------------------------
#ABOUT ME 
        
    
class Aboutme(TemplateView):
    template_name: str = 'clientes/aboutme.html'




#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------
#inicio

class Inicio(TemplateView):
    template_name = 'clientes/inicio.html'
    
    
    
    
    
    
#---------------------------------------------------------------------------------------------------------------------    
#---------------------------------------------------------------------------------------------------------------------    
#---------------------------------------------------------------------------------------------------------------------    
#MOSTRAR DATOS

#---------------------------------------------------------------------------------------------------------------------
#MOSTRAR DATOS CLIENTES CBV


class MostrarDatosClientes(LoginRequiredMixin, ListView):
    model = Cliente
    template_name = 'clientes/mostrar_datos_clientes.html'
    
    def get(self, request):
        clientes = Cliente.objects.all().order_by('-nombre')
        return render(request, self.template_name, {'clientes': clientes})
        
    def post(self, request):
        query = request.POST['buscar_cliente']
        clientes = Cliente.objects.all
        if query:
            clientes = Cliente.objects.filter(Q(nombre__icontains=query) | Q(apellido__icontains=query) | Q(servicio__icontains=query))
            if not clientes:
                return render(request, self.template_name, {'clientes': clientes, 'mensaje': 'No se encontraron resultados'})
            return render(request, self.template_name, {'clientes': clientes})
        elif query == '':
            return render(request, self.template_name, {'clientes': clientes, 'mensaje': 'No se ha ingresado ningun cliente'})
            
        else:
            return render(request, self.template_name, {'clientes': clientes})

    

#---------------------------------------------------------------------------------------------------------------------
#MOSTRAR DATOS EMPLEADOS CBV

class mostrar_datos_empleados(LoginRequiredMixin, ListView):
    model = Empleados
    template_name = 'clientes/mostrar_datos_empleados.html'
    
    def get(self, request):
        empleados = Empleados.objects.all()
        return render(request, 'clientes/mostrar_datos_empleados.html', {'empleados': empleados})
    
    
    def post(self, request):
        query = request.POST['buscar_empleado']
        empleados = Empleados.objects.all
        if query:
            empleados = Empleados.objects.filter(Q(nombre__icontains=query) | Q(apellido__icontains=query) | Q(area__icontains=query))
            if not empleados:
                return render(request, self.template_name, {'mensaje': 'No se encontraron resultados'})
            return render(request, self.template_name, {'empleados': empleados})
        elif query == '':
            return render(request, self.template_name, {'empleados': empleados, 'mensaje': 'No se ha ingresado ningun empleado'})

#---------------------------------------------------------------------------------------------------------------------
#MOSTRAR DATOS SERVICIOS CBV


class MostrarDatosServicios(LoginRequiredMixin, ListView):
    model = Servicios
    template_name = 'clientes/mostrar_datos_servicios.html'
    
    def get(self, request):
        servicios = Servicios.objects.all()
        return render(request, 'clientes/mostrar_datos_servicios.html', {'servicios': servicios})
    
    def post(self, request):
        query = request.POST['buscar_servicio']
        servicios = Servicios.objects.all
        if query:
            servicios = Servicios.objects.filter(Q(nombre__icontains=query))
            if not servicios:
                return render(request, self.template_name, {'mensaje': 'No se encontraron resultados'})
            return render(request, self.template_name, {'servicios': servicios})
        elif query == '':
            return render(request, self.template_name, {'servicios': servicios, 'mensaje': 'No se ha ingresado ningun servicio'})
        else:
            return render(request, self.template_name, {'servicios': servicios, 'mensaje': 'NO HAY DATOS PARA MOSTRAR'})


#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------
#CLIENTES



#---------------------------------------------------------------------------------------------------------------------
#FORMULARIO CLIENTES

@login_required
def clientes_formulario(request):
    
    if request.method == 'POST':
        miFormulario = Cliente_formulario(request.POST)
        
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            
            cliente = Cliente(nombre = informacion['nombre'], apellido = informacion['apellido'], fechaVencimiento = informacion['fechaVencimiento'], email = informacion['email'], contraseña = informacion['contraseña'], servicio = informacion['servicio'])
            
            cliente.save()
            
            return render(request, 'clientes/inicio.html', {'mensaje': 'Cliente creado exitosamente'})
    else:
        miFormulario = Cliente_formulario()
            
    return render(request, 'clientes/clientes_template.html', {'formulario_clientes': miFormulario, })

#---------------------------------------------------------------------------------------------------------------------
#ELIMINAR CLIENTES 

@login_required
def eliminar_cliente(request, id):
    if request.method == 'GET':
        cliente = Cliente.objects.get(id=id)
        cliente.delete()
        
        clientes = Cliente.objects.all()
        contexto = {'clientes': clientes}
        return render(request, 'clientes/mostrar_datos_clientes.html', contexto, {'mensaje': 'Cliente eliminado exitosamente'})
    else :
        return render(request, 'clientes/inicio.html', {'mensaje': 'No se pudo eliminar el cliente'})
    

#---------------------------------------------------------------------------------------------------------------------
#EDITAR CLIENTES

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
            
            
            return render(request, 'clientes/inicio.html' , {'mensaje': 'CLIENTE EDITADO EXITOSAMENTE'})
    else:
        formulario_cliente = Cliente_formulario(initial={'nombre': cliente.nombre, 'apellido': cliente.apellido, 'fechaVencimiento': cliente.fechaVencimiento, 'email': cliente.email, 'contraseña': cliente.contraseña, 'servicio': cliente.servicio})
    return render(request, 'clientes/clientes_template.html', {'formulario_clientes': formulario_cliente})




#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------
#EMPLEADOS

    

#---------------------------------------------------------------------------------------------------------------------
#FORMULARIO EMPLEADOS

@login_required
def empleados_formulario(request):
    
    if request.method == 'POST':
        formulario_empleado = Empleado_formulario(request.POST)
        
        if formulario_empleado.is_valid():
            informacion = formulario_empleado.cleaned_data
            
            empleado = Empleados(nombre = informacion['nombre'], apellido = informacion['apellido'], area = informacion['area'], antiguedad_meses = informacion['antiguedad_meses'])
            
            empleado.save()
            
            return render(request, 'clientes/inicio.html', {'mensaje': 'Empleado creado exitosamente'})
    else:
        formulario_empleado = Empleado_formulario()
        
    return render(request, 'clientes/empleados_template.html', {'formulario_empleados': formulario_empleado})
#---------------------------------------------------------------------------------------------------------------------
#ELIMINAR EMPLEADOS

@login_required
def eliminar_empleado(request, id):
    empleado = Empleados.objects.get(id=id)
    empleado.delete()
    
    empleados = Empleados.objects.all()
    contexto = {'empleados': empleados}
    return render(request, 'clientes/mostrar_datos_empleados.html', contexto)
#---------------------------------------------------------------------------------------------------------------------
#EDITAR EMPLEADOS 

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
            
            return render(request, 'clientes/inicio.html', {'mensaje': 'Empleado editado exitosamente'})
    else:
        formulario_empleado = Empleado_formulario(initial={'nombre': empleado.nombre, 'apellido': empleado.apellido, 'area': empleado.area, 'antiguedad_meses': empleado.antiguedad_meses})
    return render(request, 'clientes/empleados_template.html', {'formulario_empleados': formulario_empleado})




#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------
#SERVICIOS


#---------------------------------------------------------------------------------------------------------------------
#FORMULARIO SERVICIOS

@login_required
def servicios_formulario(request):
    
    if request.method == 'POST':
        formulario_servicio = Servicio_formulario(request.POST)
        
        if formulario_servicio.is_valid():
            informacion = formulario_servicio.cleaned_data
            
            servicio = Servicios(nombre = informacion['nombre'], descripcion = informacion['descripcion'], precio = informacion['precio'])
            
            servicio.save()
            
            return render(request, 'clientes/inicio.html', {'mensaje': 'Servicio creado exitosamente'})
    else:
        formulario_servicio = Servicio_formulario()
        
    return render(request, 'clientes/servicios_template.html', {'formulario_servicios': formulario_servicio})
#---------------------------------------------------------------------------------------------------------------------
#ELIMINAR SERVICIO

@login_required
def eliminar_servicio(request, id):
    servicio = Servicios.objects.get(id=id)
    servicio.delete()
    
    servicios = Servicios.objects.all()
    contexto = {'servicios': servicios}
    return render(request, 'clientes/mostrar_datos_servicios.html', contexto)
#---------------------------------------------------------------------------------------------------------------------
#ADITAR SERVICIO

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
            
            return render(request, 'clientes/inicio.html', {'mensaje': 'Servicio editado exitosamente'})
    else:
        formulario_servicio = Servicio_formulario(initial={'nombre': servicio.nombre, 'descripcion': servicio.descripcion, 'precio': servicio.precio})
    return render(request, 'clientes/servicios_template.html', {'formulario_servicios': formulario_servicio})




#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------
#ERRORES

class Error404View(TemplateView):
    template_name = 'error404.html'
    
class Error505View(TemplateView):
    template_name = 'error500.html'
    
    @classmethod
    def as_error_view(cls):
        v = cls.as_view()
        def view(request):
            r = v(request)
            r.render()
            return r
        return view
    