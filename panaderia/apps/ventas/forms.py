from django import forms
from django.forms import inlineformset_factory

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
        fields = ['empleado','forma_de_pago','tipo_comprobante','comprador','observaciones','total_venta'] #SE DEBEN DEFINIR TODOS LOS CAMPOS AUNQUE NO SE USEN
        widgets = {
            'total_venta': forms.HiddenInput(),
        }

ItemVentaFormSet = inlineformset_factory(
    Venta,  # Modelo principal
    ItemVenta,  # Modelo relacionado
    form=ItemVentaForm,
    extra=1,  # Formularios vacíos adicionales
    can_delete=True  # Permitir que el usuario elimine elementos
)