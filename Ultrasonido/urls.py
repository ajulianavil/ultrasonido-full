"""Ultrasonido URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Prototipo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('barra/', views.barra),
    path('login/', views.login),
    path('login2/', views.login2),
    path('inicio/', views.inicio),
    path('barra2/', views.barra2),
    path('barra3/', views.barra3),
    path('ejemplo/', views.ejemplo),
    path('perfil/', views.perfil),
    path('perfil_inicial/', views.perfil_inicial),
    path('registro/', views.registro),
    path('contactanos/', views.contactanos),

]
