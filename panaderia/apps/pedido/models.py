from ..proveedores.models import Proveedor
from ..inventario.models import Insumo
from django.db import models

# Create your models here.
class Pedido(models.Model):
    numero_pedido = models.IntegerField()
    fecha_realizado = models.DateTimeField(auto_now_add=True)
    observacion = models.CharField(max_length=150,null=True,blank=True)
    id_proveedor = models.ForeignKey(Proveedor,on_delete=models.SET_NULL,null=True,related_name='Proveedor')


class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido,on_delete = models.SET_NULL,null= True)
    insumo = models.ForeignKey(Insumo,on_delete=models.SET_NULL,null = True)
    cantidad = models.IntegerField(null=False,blank=False)


