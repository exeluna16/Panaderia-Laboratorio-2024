from idlelib.tree import TreeItem
from ..proveedores.models import Proveedor
from django.db import models

# Create your models here.
class Pedido(models.Model):
    numero = models.DecimalField()
    fecha_realizado = models.DateTimeField(auto_now_add=True)
    observacion = models.CharField(max_length=150,null=True)
    cuit_proveedor = models.ForeignKey(Proveedor,on_delete=models.SET_NULL,null=True,related_name='Proveedor')