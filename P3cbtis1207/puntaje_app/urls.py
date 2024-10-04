from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path("contactos/", views.contactos, name="contactos"),
    path("empleado/", views.empleado, name="empleado"),
    path("sucursal/", views.sucursal, name="sucursal"),
    path("clientes/", views.clientes, name="clientes"),
    path("distribuidor/", views.distribuidor, name="distribuidor"),
    path("compra/", views.compra, name="compra")
]
