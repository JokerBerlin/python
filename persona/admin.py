from django.contrib import admin
from .models import Libro
# Register your models here.


@admin.register(Libro)
class AdminLibro(admin.ModelAdmin):
    list_display = ('id',)
