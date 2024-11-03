from django import forms
from django.forms import inlineformset_factory
from .models import Pedido,ItemPedido,RecepcionPedido

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['observacion','id_proveedor','numero_pedido']
        widgets = {
            'observacion':forms.TextInput(attrs={'class':'form-control'}),
            'id_proveedor':forms.HiddenInput(),
            'numero_pedido':forms.NumberInput(attrs={'class':'form-control'}),
        }

class RecepcionPedidoForm(forms.ModelForm):
    class Meta:
        model = RecepcionPedido
        fields = ['total_pedido','numero_comprobante','observaciones']
        widgets = {
            'total_pedido':forms.NumberInput(attrs={'class':'form-control'}),
            'numero_comprobante':forms.NumberInput(attrs={'class':'form-control','required':True}),
            'observaciones':forms.Textarea(attrs={'class':'form-control'}),
        }

class ItemPedidoForm(forms.ModelForm):
    class Meta:
        model = ItemPedido
        fields = ['pedido','insumo','cantidad_pedida']
        widgets = {
            'cantidad_pedida':forms.HiddenInput(attrs={'class':'form-control cantidad-insumo'}),
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

ItemRecepcionPedidoFormSet = inlineformset_factory(
    Pedido,
    ItemPedido,
    form=ItemPedidoForm,
    fields=['id','cantidad_recibida','cantidad_pedida'],
    widgets = {
            'cantidad_recibida':forms.NumberInput(attrs={'class':'form-control cantidad-insumo-recibido'}),
            'id': forms.HiddenInput(attrs={'class':'insumo-seleccionado'}),
            'cantidad_pedida':forms.TextInput(attrs={'class': 'form-control', 'readonly': True}),
        },
    extra=0,
    can_delete=False,
)

