from django.urls import path, re_path
from . import views
app_name='biblioteca'
urlpatterns = [
    #path(r'', views.hola, name="hola"),
	#path(r'ultimos_libros/', views.ultimos_libros, name="ultimos_libros"),
    #path(r'hora/',views.fecha_actual, name="hora"),
    #path(r'fechas/\d/', views.horas_adelante),
    #re_path(r'^formulario_buscar/$', views.formulario_buscar),
    re_path(r'^buscar/$', views.buscar),
    path('autor/new', views.insertar_autor,name="nuevo_autor"),
    path('autor/list', views.listar_autor, name = "listar_autor"),
    path('editor/listar', views.listar_editor.as_view(), name = "listar_editor"),
    #path('editor/buscar/', views.filtrar_editor, name ="buscar_editor"),
    path('editor/crear', views.crear_editor.as_view(), name = "crear_editor"),
    path('editor/modificar/<int:pk>', views.modificar_editor.as_view(), name = "modificar_editor"),
    path('editor/eliminar/<int:pk>', views.eliminar_editor.as_view(), name = "eliminar_editor"),
    path('editor/buscar/', views.buscar_editor.as_view(), name = "buscar_editor"),
    path('editor/filtrar/',views.filtrar_editor, name="filtrar_editor"),
    path('editor/algobuscar/',views.algo_buscar, name="algobuscar"),
    path('editor/search/',views.quince,name="search"),

    #path('editor/bsr',views.buscarEditorNuevo, name = "buscar_nuevo_editor")
    #re_path(r'^contactos/$', views.contactos),
]
