from django.shortcuts import render
from .models import Libro
from django.http import HttpResponse, Http404
import datetime
from django.template import loader, Context

# Create your views here.

def hola(request):
    return HttpResponse("Hola mundo")

def fecha_actual(request):
    ahora = datetime.datetime.now()
    template = loader.get_template('tiempo/hora.html')
    context = {
        'fecha_actual':ahora
    }
    return HttpResponse(template.render(context,request))
    #primera linea
    #return render(request, 'hora.html', context)

def ultimos_libros(request):
    lista_libros = Libro.objects.order_by('-fecha')[:10]
    return render(request,'libro/ultimos_libros.html', {'lista_libros': lista_libros} )

def horas_adelante(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now()+datetime.timedelta(hours=offset)
    html = "<html><body><h1>En %s hora(s), seran:</h1> <h3>%s</h3></body></html>" % (offset, dt)
    return HttpResponse(html)
