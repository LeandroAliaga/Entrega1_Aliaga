
from django.urls import path, include
from clientes import views

urlpatterns = [
    path("clientes/", views.clientes_formulario, name ="agregarCliente"),
    path("empleados/", views.empleados_formulario, name ="agregarEmpleado"),
    path("servicios/", views.servicios_formulario, name ="agregarServicio"),
    path("mostrar/", views.mostrarDatos, name ="mostrarDatos"),
    
]