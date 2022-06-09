
from django.urls import path, include
from clientes import views

urlpatterns = [
    path("", views.inicio, name ="inicio"),
    path("clientes/", views.clientes_formulario, name ="agregarCliente"),
    path("empleados/", views.empleados_formulario, name ="agregarEmpleado"),
    path("servicios/", views.servicios_formulario, name ="agregarServicio"),
    path("mostrar/", views.mostrarDatos, name ="mostrarDatos"),
    path("eliminar/<id>", views.eliminar_cliente, name ="eliminarCliente"),
    path("eliminar_empleado/<id>", views.eliminar_empleado, name ="eliminarEmpleado"),
    path("eliminar_servicio/<id>", views.eliminar_servicio, name ="eliminarServicio"),
    path("editar_servicio/<id>", views.editar_servicio, name ="editarServicio"),
    path("editar_empleado/<id>", views.editar_empleado, name ="editarEmpleado"),
    path("editar_cliente/<id>", views.editar_cliente, name ="editarCliente"),
    
]