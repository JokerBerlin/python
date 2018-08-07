from django.urls import path, re_path
from . import views
urlpatterns = [
    path(r'', views.hola, name="hola"),
	path(r'ultimos_libros/', views.ultimos_libros, name="ultimos_libros"),
    path(r'hora/',views.fecha_actual, name="hora"),
    #path(r'fechas/\d/', views.horas_adelante),
    re_path(r'fecha/(\d{1,2})/$', views.horas_adelante),
]
