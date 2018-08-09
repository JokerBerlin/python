from django.shortcuts import render, get_object_or_404
from django.template import loader

from django.http import HttpResponse, HttpResponseRedirect
from .models import Libro
from .models import Autor, Editor
from .forms import AutorForm, EditorForm
#from django.views.generic import ListView, CreateView

# Create your views here.
def formulario_buscar(request):
    template = 'buscar/formulario_buscar.html'
    return render(request,template)

def buscar(request):
    errors = []
    if 'q' in request.GET:
        q=request.GET['q']
        if not q:
            errors.append('Por favor introduce un terminoo de busquedas')
        elif len(q)>20:
            errors.append('Introduce un numero de busqueda menor a 20 caracteres')
        else:
            #mensaje = 'Estas buscando: %r'%request.GET['q']
            libros = Libro.objects.filter(titulo__icontains=q)
            #icontains para que no sea cadena vacia

            context = {
                'libros':libros,
                'query':q
            }
            return render(request,'buscar/resultados.html',context)

    return render(request,'buscar/formulario_buscar.html',{'errors':errors})

def insertar_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            autor = form.save()
            autor.save()
            return HttpResponseRedirect('/autor/list')
    else:
        form = AutorForm()

    template = loader.get_template('autor/insertar/insertar_autor.html')
    context = {
		'form': form
	}
    return HttpResponse(template.render(context, request))

def listar_autor(request):
    lista_autor = Autor.objects.order_by('-id')[:10]
    template = loader.get_template('autor/listar/buscar_autor.html')
    context = {
        'lista_autor': lista_autor
    }
    return HttpResponse(template.render(context,request))

def actualizar_autor(request, postid):
    autor = get_object_or_404(Autor, postid = postid)
    form = AutorForm(request.POST or none, instance = autor)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
    template = loader.get_template('autor/modificar/modifica_autor.html')
    context = {
        'form' : form
    }

    return HttpResponse(template.render(request,context))
'''
def listar_editor(ListView):
    model = Editor
    template_name = 'editor/listar/listar_editor.html'

def crear_editor(CreateView):
    model = Editor
    template_name = 'editor/crear/crear_editor.html'
    form_class = EditorForm
    succes_url = reverse_lazy('biblioteca:listar_autor')

    def get_context_data(Self, **kwargs):
        context = (EditorCreate, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        if form.is_valid():
            Editor = form.save()
            Editor.save()
            return HttpResponseRedirect(self.get_success.url())
        else:
            return self.render_to_response(self.get_context_data(form =form))
'''
