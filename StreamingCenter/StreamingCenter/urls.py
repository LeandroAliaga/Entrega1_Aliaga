
from django.contrib import admin
from django.urls import path, include
from clientes.views import Inicio, login_request, register_request
from django.contrib.auth.views import LogoutView



urlpatterns = [
    path('admin/', admin.site.urls), 
    path("streamingCenter/", include('clientes.urls')),
    path('', Inicio.as_view(), name ="inicio"),
    #---------------------------------------------------------------------------------------------------------------------
    path('login/', login_request, name='login'),
    path('register/', register_request, name='registro'),
    path('logout/', LogoutView.as_view(template_name='clientes/logout.html'), name='logout'),
]
