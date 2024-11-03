from django.db import models
from ..inventario.models import Producto
from ..cliente_mayorista.models import ClienteMayorista
from ..usuario.models import Usuario
# Create your models here.
'''Esta es la version de prueba de la venta, hay datos que deben ser claves foraneas para poder
hacer referencia a modelos que se encuentran en otras apps'''
class Venta(models.Model):
    FORMA_PAGO = [
        ('EFECTIVO','EFECTIVO'),
        ('TRASNFERENCIA','TRASNFERENCIA'),
        ('TARJETA','TARJETA'),
        ('QR','QR'),          
    ]
    TIPO_COMPROBANTE=[
        ('TICKET','TICKET'),
        ('FACTURA','FACTURA'),
    ]
    empleado = models.ForeignKey(Usuario,on_delete=models.CASCADE) # debe llevar una clave foranea
    fecha_venta = models.DateField(auto_now_add=True) # esto guarda la fheca actual de la venta
    forma_de_pago= models.CharField(max_length=20,choices=FORMA_PAGO)
    tipo_comprobante = models.CharField(max_length=20,choices=TIPO_COMPROBANTE)
    comprador = models.ForeignKey(ClienteMayorista,on_delete=models.CASCADE) #debe ser clave foranea
    observaciones = models.CharField(max_length=150,blank=True)
    total_venta = models.DecimalField(decimal_places=2,max_digits=10)


#una venta puede tener muchos items, la idea es que se carguen dinamicamente en la vista
class ItemVenta(models.Model):
    venta = models.ForeignKey(Venta,on_delete=models.SET_NULL,null=True,related_name='venta')
    producto = models.ForeignKey(Producto,on_delete=models.SET_NULL,null=True)
    cantidad = models.IntegerField(null=False)
    sub_total = models.DecimalField(decimal_places=2,max_digits=10)