from django import forms
from django.forms import HiddenInput

from .models import Producto,Insumo
from django.forms import formset_factory

class AgregarProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['codigo','nombre','cantidad','cantidad_minima','unidad_de_medida','precio','categoria']
        widgets = {
            'codigo': forms.NumberInput(attrs={'class': 'form-control','placeholder':'ingrese el codigo del producto...','required':True}),
            'nombre': forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese el nombre del producto','required':True}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'ingrese la cantidad', 'required': True}),
            'cantidad_minima': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'ingrese la cantidad minima', 'required': True}),
            'unidad_de_medida': forms.Select(attrs={'class': 'form-select'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control','step':0.01, 'placeholder': 'ingrese el precio', 'required': True}),
            'categoria': forms.Select(attrs={'class':'form-select'}),
        }

class ModificarProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['codigo','nombre','cantidad','cantidad_minima','unidad_de_medida','precio','categoria','estado']
        widgets = {
            'codigo': forms.NumberInput(attrs={'class': 'form-control','placeholder':'ingrese el codigo del producto...','required':True}),
            'nombre': forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese el nombre del producto','required':True}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'ingrese la cantidad', 'required': True}),
            'cantidad_minima': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'ingrese la cantidad minima', 'required': True}),
            'unidad_de_medida': forms.Select(attrs={'class': 'form-select'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control','step':0.01, 'placeholder': 'ingrese el precio', 'required': True}),
            'categoria': forms.Select(attrs={'class':'form-select'}),
            'estado': forms.CheckboxInput(attrs={'class':'form-check-input','role':'switch','id':'flexSwitchCheckChecked'}),
            
            #<input class="form-check-input" type="checkbox" role="switch" id="flexSwitchCheckChecked" checked>
        }

class AgregarInsumoForm(forms.ModelForm):
    class Meta:
        model = Insumo
        fields = ['codigo', 'nombre', 'cantidad', 'cantidad_minima', 'unidad_de_medida','ultimo_precio']
        widgets = {
            'codigo': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'ingrese el codigo del producto...', 'required': True}),
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre del producto', 'required': True}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'ingrese la cantidad', 'required': True}),
            'cantidad_minima': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'ingrese la cantidad minima', 'required': True}),
            'unidad_de_medida': forms.Select(attrs={'class': 'form-select'}),
            'ultimo_precio': forms.NumberInput(attrs={'class': 'form-control','step':0.01, 'placeholder': 'ingrese el precio', 'required': True}),
        }

class ModificarInsumoForm(forms.ModelForm):
    class Meta:
        model = Insumo
        fields = ['codigo', 'nombre', 'cantidad', 'cantidad_minima', 'unidad_de_medida','ultimo_precio','estado']
        widgets = {
            'codigo': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'ingrese el codigo del producto...', 'required': True}),
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre del producto', 'required': True}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'ingrese la cantidad', 'required': True}),
            'cantidad_minima': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'ingrese la cantidad minima', 'required': True}),
            'unidad_de_medida': forms.Select(attrs={'class': 'form-select'}),
            'ultimo_precio': forms.NumberInput(attrs={'class': 'form-control','step':0.01, 'placeholder': 'ingrese el precio', 'required': True}),
            'estado': forms.CheckboxInput(attrs={'class':'form-check-input','role':'switch','id':'flexSwitchCheckChecked'}),
        }


class DescontarInsumoForm(forms.ModelForm):
    class Meta:
        model = Insumo
        fields = ['codigo','cantidad']
        widgets = {
            'cantidad':forms.HiddenInput(attrs={'class':'cantidad-insumo'}),
            #IMPORTANTE!! acá se define ocmo codigo pero en realidad es el id del insumo, puede que el comportamiento sea debido al formsetfactory
            'codigo': forms.HiddenInput(attrs={'class':'insumo-seleccionado'}),
        }

ItemInsumoFormSet = formset_factory(DescontarInsumoForm,extra=1)