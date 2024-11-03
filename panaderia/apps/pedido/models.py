from ..proveedores.models import Proveedor
from ..inventario.models import Insumo
from ..usuario.models import Usuario
from django.db import models

# Create your models here.
class Pedido(models.Model):
    ESTADO_PEDIDO = [
        ('PENDIENTE','PENDIENTE'),
        ('RECIBIDO','RECIBIDO'),
    ]

    numero_pedido = models.IntegerField()
    fecha_realizado = models.DateField(auto_now_add=True)
    observacion = models.CharField(max_length=150,null=True,blank=True)
    id_proveedor = models.ForeignKey(Proveedor,on_delete=models.SET_NULL,null=True,related_name='Proveedor')
    estado = models.CharField(max_length=25,choices=ESTADO_PEDIDO,default='PENDIENTE')

class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido,on_delete = models.SET_NULL,null= True)
    insumo = models.ForeignKey(Insumo,on_delete=models.SET_NULL,null = True)
    cantidad_pedida = models.IntegerField(null=False,blank=False)
    cantidad_recibida = models.IntegerField(default=0)

class RecepcionPedido(models.Model):
    empleado = models.ForeignKey(Usuario,on_delete=models.CASCADE)
    proveedor = models.ForeignKey(Proveedor,on_delete=models.CASCADE)
    fecha_recepcion = models.DateField(auto_now=True)
    numero_comprobante = models.IntegerField(blank=True)
    observaciones = models.TextField(blank=True,null=True)
    pedido = models.ForeignKey(Pedido,on_delete=models.CASCADE)
    total_pedido = models.DecimalField(decimal_places=2,max_digits=10)