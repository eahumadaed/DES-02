from django.db import models

class Tarea(models.Model):
    descripcion = models.CharField(max_length=255)
    eliminada = models.CharField(max_length=100)

    def __str__(self):
        return self.descripcion

class SubTarea(models.Model):
    descripcion = models.CharField(max_length=255)
    eliminada = models.CharField(max_length=100)
    tarea = models.ForeignKey(Tarea, related_name='subtareas', on_delete=models.CASCADE)

    def __str__(self):
        return self.descripcion
