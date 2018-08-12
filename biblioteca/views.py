import json
from django.shortcuts import render, get_object_or_404, render_to_response
from django.template import loader

from django.http import HttpResponse, HttpResponseRedirect
from .models import Libro
from .models import Autor, Editor
from .forms import AutorForm, EditorForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy

#import json
#from django.views.decorators.csrf import csrf_exempt
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

class listar_editor(ListView):
    model = Editor
    template_name = 'editor/listar_editor.html'
    paginate_by = 4



'''
def filtrar_editor(request):
    errors = []
    if 'q' in request.GET:
        q=request.GET['q']
        if not q:
            errors.append('Por favor introduce un terminoo de busquedas')
        elif len(q)>20:
            errors.append('Introduce un numero de busqueda menor a 20 caracteres')
        else:
            #mensaje = 'Estas buscando: %r'%request.GET['q']
            object_list = Editor.objects.filter(nombre__icontains=q)
            #icontains para que no sea cadena vacia

            context = {
                'object_list':object_list,
                'query':q
            }
            return render(request,'editor/listar_editor.html',context)

    return render(request,'editor/listar_editor.html',{'errors':errors})
'''
class buscar_editor(TemplateView):
    template_name = 'editor/listar_editor.html'
    def post(self, request, *args, **kwargs):
        buscar = request.POST['busca']
        object_list = Editor.objects.filter(nombre__icontains=buscar)|Editor.objects.filter(ciudad__icontains=buscar)
        print(object_list)
        return render(request,'editor/listar_editor.html',{'object_list':object_list})


def algo_buscar(request):
    if request.is_ajax():
        search=request.GET.get('start','')

        ed = Editor.objects.filter(nombre__icontains = search)
        r = []
        for i in ed:
            ed_json={}
            ed_json['nombre']=i.nombre
            r.append(ed_json)
        data_json = json.dumps(ed_json)
    else:
        data_json = 'fail'
    mimetype="application/json"
    return HttpResponse(data_json, mimetype)

def filtrar_editor(request):

    if request.is_ajax():
        query = request.GET.get("term", "")
        editores = Editor.objects.filter(nombre__icontains=query)
        results = []
        for editor in editores:
            editor_json['id'] = editor.id
            editor_json['label'] = editor.nombre
            editor_json['value'] = editor.nombre
            results.append(editor_json)
        data = json.dumps(results)
    else:
        data = 'fail'
        mimetype = 'application/json'
    mimetype = "application/json"
    return HttpResponse(data, mimetype)

def quince(request):
    if request.method == 'GET' and 's' in request.GET:
        quer = request.GET['s']
        if quer is not None:
            results = Editor.objects.filter(nombre__icontains=quer)
            json_list = []
            for re in results:
                json_list.append(re.nombre)
            return HttpResponse(json.dumps(json_list,ensure_ascii=False))


'''
@csrf_exempt
def buscarEditorNuevo(request):
    if request.method == 'POST':
        datos = json.loads(request.body)
        # usuario= BuscarUsuario(Datos["idUsuario"])

        nombre = datos["nombreEditor"]
        jsonfinal = {}
        jsonfinal["editores"] = []
        try:
            object_list = Editor.objects.filter(nombre__icontains=nombreEditor)
            for oEditor in object_list:
                jsonEditor = {}
                jsonEditor["id"] = oEditor.id
                jsonEditor["nombre"] = oEditor.nombre
                jsonEditor["domicilio"] = oEditor.domicilio
                jsonEditor["ciudad"] = oEditor.ciudad
                jsonfinal["editores"].append(jsonEditor)

            return HttpResponse(json.dumps(jsonfinal), content_type="application/json")
        except Exception as e:
            return HttpResponse(json.dumps({'exito':0}), content_type="application/json")
'''


class crear_editor(CreateView):
    model = Editor
    template_name = 'editor/crear_editor.html'
    form_class = EditorForm
    success_url = reverse_lazy('biblioteca:listar_editor')

    def get_context_data(self, **kwargs):
        context = super(crear_editor, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        if form.is_valid():
            Editor = form.save()
            Editor.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form = form))


class modificar_editor(UpdateView):
    model = Editor
    template_name = 'editor/crear_editor.html'
    form_class = EditorForm
    success_url = reverse_lazy('biblioteca:listar_editor')

    def get_context_data(self, **kwargs):
        context = super(modificar_editor, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk',0)
        editor = self.model.objects.get(id=pk)
        if 'form' not in context:
            context['form'] = self.form_class()
        context['id'] = pk
        return context
    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        id_editor = kwargs['pk']
        editor = self.model.objects.get(id=id_editor)
        form = self.form_class(request.POST, instance = editor)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return HttpResponseRedirect(self.get_success_url())

class eliminar_editor(DeleteView):
	model = Editor
	template_name = 'editor/eliminar_editor.html'
	success_url = reverse_lazy('biblioteca:listar_editor')
