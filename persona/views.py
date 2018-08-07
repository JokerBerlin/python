from django.shortcuts import render
from .models import Libro
from django.http import HttpResponse
# Create your views here.

def hola(request):
    return HttpResponse("Hola mundo")

def ultimos_libros(request):
    lista_libros = Libro.objects.order_by('-fecha')[:10]
    return render(request,'ultimos_libros.html', {'lista_libros': lista_libros} )
