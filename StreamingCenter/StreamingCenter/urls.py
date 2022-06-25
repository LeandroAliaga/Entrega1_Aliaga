
from django.contrib import admin
from django.urls import path, include
from clientes import views
from clientes.views import Inicio, registro, Error404View
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404

urlpatterns = [
    path('admin/', admin.site.urls), 
    path("streamingCenter/", include('clientes.urls')),
    path('', login_required(Inicio.as_view()), name ="inicio"),
    #---------------------------------------------------------------------------------------------------------------------
    path('login/', views.login_request, name='login'),
    path('register/', registro.as_view(), name='registro'),
    path('logout/', LogoutView.as_view(template_name='clientes/logout.html'), name='logout'),
    path('editarPerfil/', views.editarPerfil, name='editarPerfil'),
]
handler404=Error404View.as_view()

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)