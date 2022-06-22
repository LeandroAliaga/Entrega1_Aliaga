
from django.urls import path, include
from clientes import views
from clientes.views import Cliente_list, Cliente_create, Cliente_update, Cliente_delete, Cliente_detail, login_request, register_request
from django.contrib.auth.views import LogoutView







urlpatterns = [
    
    path("clientes/", views.clientes_formulario, name ="agregarCliente"),
    path("empleados/", views.empleados_formulario, name ="agregarEmpleado"),
    path("servicios/", views.servicios_formulario, name ="agregarServicio"),
    path("eliminar/<id>", views.eliminar_cliente, name ="eliminarCliente"),
    path("eliminar_empleado/<id>", views.eliminar_empleado, name ="eliminarEmpleado"),
    path("eliminar_servicio/<id>", views.eliminar_servicio, name ="eliminarServicio"),
    path("editar_servicio/<id>", views.editar_servicio, name ="editarServicio"),
    path("editar_empleado/<id>", views.editar_empleado, name ="editarEmpleado"),
    path("editar_cliente/<id>", views.editar_cliente, name ="editarCliente"),
    #---------------------------------------------------------------------------------------------------------------------
    path('mostrar/listar/', Cliente_list.as_view(), name='listar_clientes'),
    path('mostrar/crear/', Cliente_create.as_view(), name='crear_clientes'),
    path('mostrar/editar/<pk>/', Cliente_update.as_view(), name='editar_clientes'),
    path('mostrar/eliminar/<pk>/', Cliente_delete.as_view(), name='eliminar_clientes'),
    path('mostrar/<pk>/', Cliente_detail.as_view(), name='detalle_clientes'),
    
    #---------------------------------------------------------------------------------------------------------------------
    path('clientesdata/', views.mostrarDatosClientes, name='mostrarDatosClientes'),
    path('empleadosdata/', views.mostrarDatosEmpleados, name='mostrarDatosEmpleados'),
    path('serviciosdata/', views.mostrarDatosServicios, name='mostrarDatosServicios'),
    
    
]