from django import forms
from django.forms import inlineformset_factory
from .models import Pedido,ItemPedido

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['observacion','id_proveedor','numero_pedido']
        widgets = {
            'observacion':forms.TextInput(attrs={'class':'form-control'}),
            'id_proveedor':forms.HiddenInput(),
            'numero_pedido':forms.NumberInput(attrs={'class':'form-control'}),
        }


class ItemPedidoForm(forms.ModelForm):
    class Meta:
        model = ItemPedido
        fields = ['pedido','insumo','cantidad']
        widgets = {
            'cantidad':forms.HiddenInput(attrs={'class':'form-control cantidad-insumo'}),
            'pedido': forms.HiddenInput(),
            'insumo': forms.HiddenInput(attrs={'class':'insumo-seleccionado'}),
        }


#formulario de tipo formset, crea varias instancias de un formulario
ItemPedidoFormSet = inlineformset_factory (
    Pedido, #modelo principal
    ItemPedido, #modelo relacionado
    form = ItemPedidoForm,
    extra = 1,
    can_delete=True,
)