from django.shortcuts import render
from django.http import HttpResponse
from .models import Libro
# Create your views here.
def formulario_buscar(request):
    template = 'buscar/formulario_buscar.html'
    return render(request,template)

def buscar(request):
    error = False
    if 'q' in request.GET:
        q=request.GET['q']
        if not q:
            error = True
        else:
            #mensaje = 'Estas buscando: %r'%request.GET['q']
            libros = Libro.objects.filter(titulo__icontains=q)
            #icontains para que no sea cadena vacia

            context = {
                'libros':libros,
                'query':q
            }
            return render(request,'buscar/resultados.html',context)

    return render(request,'buscar/formulario_buscar.html',{'error':error})
