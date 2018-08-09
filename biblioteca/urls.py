from django.urls import path, re_path
from . import views
urlpatterns = [
    #path(r'', views.hola, name="hola"),
	#path(r'ultimos_libros/', views.ultimos_libros, name="ultimos_libros"),
    #path(r'hora/',views.fecha_actual, name="hora"),
    #path(r'fechas/\d/', views.horas_adelante),
    #re_path(r'^formulario_buscar/$', views.formulario_buscar),
    re_path(r'^buscar/$', views.buscar),
    path('autor/new', views.insertar_autor,name="nuevo_autor"),
    path('autor/list', views.listar_autor, name = "listar_autor"),
    #re_path(r'^editor/list$', views.listar_editor, name = "listar_editor"),
    #re_path(r'^editor/create$', views.crear_editor, name = "crear_editor")
    #re_path(r'^contactos/$', views.contactos),
]
