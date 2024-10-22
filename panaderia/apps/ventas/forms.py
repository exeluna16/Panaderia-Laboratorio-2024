from django import forms
from .models import Venta
from ..inventario.models import Producto

class AgregarItemVentaForm(forms.ModelForm):

    #acá se dice que modelo de la BD usar
    class Meta:

        model = Producto
        fields = [ 'nombre' ,'unidad_de_medida', 'precio']


#MODELO DE VENTA
class VentaForm(forms.ModelForm):

    class Meta:
        model = Venta
        fields = ['codigo','empleado','forma_de_pago','tipo_comprobante','comprador','observaciones','total_venta']
