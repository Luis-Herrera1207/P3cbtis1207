from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,"index.html")

def contactos(request):
    return render(request,"contactos.html")

def empleado(request):
    return render(request,"empleado.html")

def sucursal(request):
    return render(request,"sucursal.html")

def clientes(request):
    return render(request,"clientes.html")

def distribuidor(request):
    return render(request,"distribuidor.html")

def compra(request):
    return render(request,"compra.html")