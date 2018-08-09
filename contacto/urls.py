from django.urls import path, re_path
from . import views
urlpatterns = [
    #path('', vi),
    re_path(r'^contactos/$',views.contactos),
]
