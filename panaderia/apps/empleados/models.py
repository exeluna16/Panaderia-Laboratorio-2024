from django.db import models
from ..usuario.models import Persona

##Modelo de los diferentes cargos de la panaderia
class Cargo(models.Model):
    descripcion = models.CharField(max_length=30)

    def __str__(self):
        return(self.descripcion)
# Create your models here.
class Empleado(Persona):
    cargo = models.ForeignKey(Cargo,on_delete=models.CASCADE,related_name='cargo')
    fecha_ingreso = models.DateField(auto_now_add=True)
    fecha_nacido = models.DateField()



