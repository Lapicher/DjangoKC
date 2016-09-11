from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def hello(request):
    nombre= request.GET.get('nombre')
    apellido=request.GET.get('apellido')
    return HttpResponse("Hello <strong>World</strong>. <br><br> Bienvenido: {0} {1}".format(nombre,apellido))
