from django.db import models
from ..inventario.models import Producto
# Create your models here.
'''Esta es la version de prueba de la venta, hay datos que deben ser claves foraneas para poder
hacer referencia a modelos que se encuentran en otras apps'''
class Venta(models.Model):
    codigo = models.IntegerField(unique=True)
    empleado = models.IntegerField() # debe llevar una clave foranea
    fecha_venta = models.DateTimeField(auto_now_add=True) # esto guarda la fheca actual de la venta
    forma_de_pago= models.CharField(max_length=20) #debe ser clave foranea
    tipo_comprobante = models.CharField(max_length=20) #debe ser clave foranea
    comprador = models.CharField(max_length=20) #debe ser clave foranea
    observaciones = models.CharField(max_length=150,blank=True)
    total_venta = models.DecimalField(decimal_places=2,max_digits=10)

class ItemVenta(models.Model):
    venta = models.ForeignKey(Venta,on_delete=models.SET_NULL,null=True,related_name='venta')
    producto = models.ForeignKey(Producto,on_delete=models.SET_NULL,null=True)
    cantidad = models.IntegerField(null=False)
    sub_total = models.DecimalField(decimal_places=2,max_digits=10)