
from django.urls import path
from clientes.views import mostrar_datos_empleados, MostrarDatosClientes, MostrarDatosServicios, BuscarCliente
from clientes import views
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views









urlpatterns = [
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
    path("buscarcliente/", BuscarCliente.as_view(), name ="buscarCliente"),
    #--------DATA-------------------------------------------------------------------------------------------------------------
    path('clientesdata/', MostrarDatosClientes.as_view(), name='mostrarDatosClientes'),
    path('empleadosdata/', mostrar_datos_empleados.as_view(), name='mostrarDatosEmpleados'),
    path('serviciosdata/', MostrarDatosServicios.as_view(), name='mostrarDatosServicios'),
    
    
]