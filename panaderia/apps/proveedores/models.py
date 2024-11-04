from django.db import models
from ..usuario.models import Persona
# Create your models here.
class Proveedor(Persona):
    dias_de_pedido = models.TextField(max_length=150,blank=True)
    dias_de_reparto = models.TextField(max_length=150,blank=True)
    fecha_nacido = models.DateField()
