from django.urls import path
from . import views
urlpatterns = [
    path(r'', views.hola, name="hola"),
	path(r'ultimos_libros/', views.ultimos_libros, name="ultimos_libros")
]
