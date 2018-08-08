from django.shortcuts import render, render_to_response
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
    lista_libros = Libro.objects.order_by('nombre')[:10]
    template = loader.get_template("libro/ultimos_libros.html")
    context = {
        'lista_libros': lista_libros
    }
    return HttpResponse(template.render(context,request))

def horas_adelante(request, horas):
    try:
        horas = int(horas)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now()+datetime.timedelta(hours=horas)
    template = loader.get_template('horaDelante/hora_delante.html')
    context = {
        'hora_siguiente' : dt,
        'horas': horas
    }
    return HttpResponse(template.render(context,request))
