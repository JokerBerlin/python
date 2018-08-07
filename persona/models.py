from django.db import models
'''Las tareas de la base de datos'''

class Libro(models.Model):
    """docstring for Libro."""
    nombre = models.CharField(max_length=50)
    fecha = models.DateField()
