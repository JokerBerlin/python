from django.db import models

# Create your models here.
class Editor(models.Model):
    nombre = models.CharField(max_length=30)
    domicilio = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=60)
    estado = models.CharField(max_length=30)
    pais = models.CharField(max_length=50)
    website = models.URLField()

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.nombre

class Autor(models.Model):
    nombre = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=40)
    email = models.EmailField('e-mail',blank=True)

    def __str__(self):
        return self.nombre

    class Meta:
        ordering =('id',)

class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    autores = models.ManyToManyField(Autor)
    editor = models.ForeignKey(Editor, on_delete = models.PROTECT)
    fecha_publicacion = models.DateField(blank=True, null=True)
    portada = models.ImageField()
    num_paginas = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.titulo
