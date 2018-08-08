from django.contrib import admin
from .models import Autor, Editor, Libro
# Register your models here.
@admin.register(Autor)
class AdminAutor(admin.ModelAdmin):
    list_display=('id','nombre',)
    list_filter=('nombre',)
    search_fields=('nombre','apellidos',)

@admin.register(Editor)
class AdminEditor(admin.ModelAdmin):
    list_display=('id','nombre',)
    list_filter=('estado',)

@admin.register(Libro)
class AdminLibro(admin.ModelAdmin):
    list_display=('titulo','editor','fecha_publicacion')
    #te pone los mejoes filtros que tiene
    list_filter=('fecha_publicacion',)
    #te ofrece palabras de filtro de tiempo
    date_hierarchy='fecha_publicacion'
    #se puede pasar el ordering sin necesidad de hacerlo con su metodo meta
    ordering=('-fecha_publicacion',)
    #fields=('titulo','autores','editor')
    #filtra autores con dos combos para pasar datos
    filter_horizontal=('autores',)
    raw_id_fields=('editor',)
