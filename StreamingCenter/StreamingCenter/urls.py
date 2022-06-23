
from django.contrib import admin
from django.urls import path, include
from clientes import views
from clientes.views import Inicio, registro 
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('admin/', admin.site.urls), 
    path("streamingCenter/", include('clientes.urls')),
    path('', login_required(Inicio.as_view()), name ="inicio"),
    #---------------------------------------------------------------------------------------------------------------------
    path('login/', views.login_request, name='login'),
    path('register/', registro.as_view(), name='registro'),
    path('logout/', LogoutView.as_view(template_name='clientes/logout.html'), name='logout'),
]
