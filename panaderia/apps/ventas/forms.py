from django import forms
from .models import Venta, ItemVenta
from ..inventario.models import Producto

class ItemVentaForm(forms.ModelForm):

    #acá se dice que modelo de la BD usar
    class Meta:
        model = ItemVenta
        fields = ['venta','cantidad','producto','sub_total']

        widgets = {
            'venta': forms.HiddenInput(),
            'producto': forms.HiddenInput(),
            'sub_total': forms.HiddenInput(),
        }

#Formulario DE VENTA
class VentaForm(forms.ModelForm):

    class Meta:
        model = Venta
        fields = ['forma_de_pago','tipo_comprobante','comprador','observaciones','total_venta']
        widgets = {
            'total_venta': forms.HiddenInput(),
        }
