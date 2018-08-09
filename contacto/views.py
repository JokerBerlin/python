from django.http import HttpResponseRedirect, HttpResponse
from django.core.mail import send_mail
from django.shortcuts import render
from contacto.forms import FormularioContactos

from django.template import loader
# Create your views here.

def contactos(request):
    #form=FormularioContactos()
    if request.method == 'POST':
        form=FormularioContactos(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['asunto'],
                cd['mensaje'],
                cd.get('email', 'noreply@example.com'),['siteowner@example.com'],
            )
            return HttpResponseRedirect('/contactos/gracias/')
    else:
        form = FormularioContactos(initial={'asunto':'adoro!'})
    template = loader.get_template('contactos/formulario_contactos.html')
    #return render(request, 'contactos/formulario_contactos.html', {'form': form})
    return HttpResponse(template.render({'form': form}, request))
