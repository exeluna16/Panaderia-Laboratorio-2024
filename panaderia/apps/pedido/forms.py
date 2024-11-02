from django import forms
from .models import Pedido

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['observacion','cuit_proveedor']
        widgets = {
            'observacion':forms.TextInput(attrs={'class':'form-control'}),
            'cuit_proveedor':forms.HiddenInput(),
        }