from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

'''Se define al usuario'''
class Usuario(AbstractUser):
    nombre = models.CharField(max_length=150)
    cuit = models.CharField(unique=True,max_length=11,default='01234567890')

    def __str__(self):
        return f'{self.nombre}'

#Como existen muchas personas en el sistema se opto por una clase abstracta
class Persona(models.Model):
    TIPO_PERSONA=[
        ('FISICA','FISICA'),
        ('JURIDICA','JURIDICA')
    ]

    nombre = models.CharField(max_length=150)
    mail = models.EmailField(max_length=150,null=True,default='ejemplo@ejemplo.com')
    tipo_persona = models.CharField(max_length=20,choices=TIPO_PERSONA)
    estado = models.BooleanField(default=True)
    calle=models.CharField(max_length=150)
    localidad = models.CharField(max_length=150)
    numero_calle = models.IntegerField(null=True)
    fecha_nacido = models.DateField()

    class Meta:
        abstract = True

    def __str__(self):
        return f'{self.nombre}'

