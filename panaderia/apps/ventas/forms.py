from django import forms
from django.forms import inlineformset_factory

from .models import Venta, ItemVenta,ItemMayorista
from ..inventario.models import Producto

class ItemVentaForm(forms.ModelForm):

    #acá se dice que modelo de la BD usar
    class Meta:
        model = ItemVenta
        fields = ['venta','cantidad','producto','sub_total']

        widgets = {
            'cantidad':forms.NumberInput(attrs={'class':'form-control cantidad-producto'}),
            'venta': forms.HiddenInput(),
            'producto': forms.HiddenInput(attrs={'class':'producto-seleccionado'}),
            'sub_total': forms.HiddenInput(attrs={'class':'sub-total'}),
        }

#Formulario DE VENTA
class VentaForm(forms.ModelForm):

    class Meta:
        model = Venta
        fields = ['forma_de_pago','tipo_comprobante','observaciones','total_venta','numero_comprobante'] #SE DEBEN DEFINIR TODOS LOS CAMPOS AUNQUE NO SE USEN
        widgets = {
            #'comprador': forms.Select(attrs={'class': 'form-select'}),
            'tipo_comprobante': forms.Select(attrs={'class': 'form-select'}),
            'forma_de_pago': forms.Select(attrs={'class': 'form-select'}),
            'observaciones': forms.Textarea(attrs={'class': 'form-control'}),
            'total_venta': forms.HiddenInput(),
            'numero_comprobante':forms.HiddenInput(attrs={'class': 'form-control'}),
        }

ItemVentaFormSet = inlineformset_factory(
    Venta,  # Modelo principal
    ItemVenta,  # Modelo relacionado
    form=ItemVentaForm,
    extra=1,  # Formularios vacíos adicionales
    can_delete=True  # Permitir que el usuario elimine elementos
)

class ItemMayoristaForm(forms.ModelForm):
    class Meta:
        model = ItemMayorista
        fields = ['cliente_mayorista']
        widgets = {
            'cliente_mayorista' : forms.HiddenInput(attrs={'class':'cliente mayorista'})
        }