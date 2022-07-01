
from django.contrib import admin
from django.urls import path, include
from clientes import views
from clientes.views import Inicio, registro, Error404View, Error505View
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls import handler404, handler500
from clientes.views import mostrar_datos_empleados, MostrarDatosClientes, MostrarDatosServicios, Aboutme

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('', Inicio.as_view(), name ="inicio"),
    #USER---------------------------------------------------------------------------------------------------------------------
    path('login/', views.login_request, name='login'),
    path('register/', registro.as_view(), name='registro'),
    path('logout/', LogoutView.as_view(template_name='clientes/logout.html'), name='logout'),
    path('editarPerfil/', views.editarPerfil, name='editarPerfil'),
        #--------CRUD-------------------------------------------------------------------------------------------------------------
    path("clientes/", views.clientes_formulario, name ="agregarCliente"),
    path("empleados/", views.empleados_formulario, name ="agregarEmpleado"),
    path("servicios/", views.servicios_formulario, name ="agregarServicio"),
    path("eliminar/<id>", views.eliminar_cliente, name ="eliminarCliente"),
    path("eliminar_empleado/<id>", views.eliminar_empleado, name ="eliminarEmpleado"),
    path("eliminar_servicio/<id>", views.eliminar_servicio, name ="eliminarServicio"),
    path("editar_servicio/<id>", views.editar_servicio, name ="editarServicio"),
    path("editar_empleado/<id>", views.editar_empleado, name ="editarEmpleado"),
    path("editar_cliente/<id>", views.editar_cliente, name ="editarCliente"),
    #--------DATA-------------------------------------------------------------------------------------------------------------
    path('clientesdata/', MostrarDatosClientes.as_view(), name='mostrarDatosClientes'),
    path('empleadosdata/', mostrar_datos_empleados.as_view(), name='mostrarDatosEmpleados'),
    path('serviciosdata/', MostrarDatosServicios.as_view(), name='mostrarDatosServicios'),
    #--------ME-------------------------------------------------------------------------------------------------------------
    path('about/', Aboutme.as_view(), name='aboutme'),

]
handler404=Error404View.as_view()


handler500 = Error505View.as_error_view()