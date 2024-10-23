from django import forms
from .models import Producto


class AgregarProducto(forms.ModelForm):
    class Meta:
        model = Producto
        labels = ['codigo','nombre','cantidad','cantidad_minima','unidad_de_medida','precio','precio_mayorista','categoria']
        exclude = ['estado']

