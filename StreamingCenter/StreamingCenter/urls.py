
from django.contrib import admin
from django.urls import path, include
from clientes.views import Inicio



urlpatterns = [
    path('admin/', admin.site.urls), 
    path("streamingCenter/", include('clientes.urls')),
    path('', Inicio.as_view(), name ="inicio"),
    
]
