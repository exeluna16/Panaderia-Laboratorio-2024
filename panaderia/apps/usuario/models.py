from django.db import models
# Create your models here.

'''Se define al usuario'''
class Usuario(models.Model):
    nombre = models.CharField(max_length=150)

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
    fecha_nacido = models.DateTimeField()

    class Meta:
        abstract = True


