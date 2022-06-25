from django.contrib import admin
from .models import Cliente, Servicios, Empleados, Avatar

# Register your models here.

admin.site.register(Servicios)
admin.site.register(Cliente)
admin.site.register(Empleados)
admin.site.register(Avatar)