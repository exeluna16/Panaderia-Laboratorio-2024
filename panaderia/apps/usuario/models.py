from django.db import models
# Create your models here.

'''Se define al usuario'''
class Usuario(models.Model):
    nombre = models.CharField(max_length=150)

    def __str__(self):
        return f'{self.nombre}'

#Como existen muchas personas en el sistema se opto por una clase abstracta
class Persona(models.Model):
    nombre = models.CharField(max_length=150)
    mail = models.EmailField(max_length=150)
    tipo_persona = models.CharField(max_length=20)
    estado = models.BooleanField(default=True)
    calle=models.CharField(max_length=150)
    localidad = models.CharField(max_length=150)
    numero_calle = models.IntegerField(null=True)

    class Meta:
        abstract = True

