from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render

def saludo(request):
    return HttpResponse("Hola Django como te va?")

def mostrar_html(request):
    return HttpResponse("<button> este es mi boton </button> <br><h1>Hola pescadito</h1>")

def diaDeHoy(request):
    dia=datetime.now()
    documentoDeTexto=f"La hora actual es: <br> {dia}</br>"
    return HttpResponse(documentoDeTexto)

def mi_nombre(request,nombre):

    return HttpResponse(f"Hola <b>{nombre}</b> como te va?")

def show_html(request):
    return render(request,"template1.html")