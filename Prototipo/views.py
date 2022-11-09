from django.shortcuts import render
from django.conf import settings

def barra(request):
    return render(request,"barra.html")

def login(request):
    return render(request,"login.html")

def login2(request):
    return render(request,"login2.html")

def inicio(request):
    return render(request,"inicio.html")
    
def barra2(request):
    return render(request,"barra2.html")

def barra3(request):
    return render(request,"barra3.html")

def ejemplo(request):
    return render(request,"ejemplo.html")

def perfil(request):
    return render(request,"perfil.html")

def perfil_inicial(request):
    return render(request,"perfil_inicial.html")

def registro(request):
    return render(request,"registro.html")

def contactanos(request):
    return render(request,"contactanos.html")

