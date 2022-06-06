from django.contrib import admin
from django.urls import path, include
from clientes import views

urlpatterns = [
    path("netflix/", views.netflix, name ="netflix"),
    path("amazon/", views.amazon, name ="amazon"),
    path("spotify/", views.spotify, name ="spotify"),
    path("disney/", views.disney, name ="disney"),
    path("inicio/", views.inicio, name ="inicio"),
    path("cuentas/", views.cuentas, name ="cuentas"),
]