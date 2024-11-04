from django import forms
from .models import Proveedor

class AgregarProveedorForm(forms.ModelForm):
    class Meta:
        model= Proveedor
        fields = ['nombre','telefono','mail','calle','localidad','numero_calle','cuit_cuil','dias_de_pedido','dias_de_reparto','tipo_persona']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control','placeholder':'nombre completo...','required':True}),
            'mail':forms.EmailInput(attrs={'class': 'form-control','placeholder':'ingrese el mail...','required':True}),
            'calle':forms.TextInput(attrs={'class': 'form-control','placeholder':'ingrese la calle','required':True}),
            'localidad':forms.TextInput(attrs={'class': 'form-control','placeholder':'ingrese la localidad','required':True}),
            'numero_calle':forms.NumberInput(attrs={'class': 'form-control','placeholder':'ingrese la calle'}),
            #'fecha_nacido':forms.DateInput(attrs={'class': 'form-control'}),
            'cuit_cuil':forms.NumberInput(attrs={'class': 'form-control','placeholder':'ingrese el cuit','required':True,'maxlength':10,'minlength':10}),
            'tipo_persona':forms.Select(attrs={'class':'form-select'}),
            'dias_de_pedido':forms.TextInput(attrs={'class':'form-control'}),
            'dias_de_reparto':forms.TextInput(attrs={'class':'form-control'}),
            'telefono': forms.TextInput(attrs={'placeholder': '+1234567890', 'class': 'form-control'}),
        }

class ModificarProveedorForm(forms.ModelForm):
    class Meta:
        model= Proveedor
        fields = ['nombre','telefono','mail','calle','localidad','numero_calle','cuit_cuil','dias_de_pedido','dias_de_reparto','tipo_persona','estado']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control','placeholder':'nombre completo...','required':True}),
            'mail':forms.EmailInput(attrs={'class': 'form-control','placeholder':'ingrese el mail...','required':True}),
            'calle':forms.TextInput(attrs={'class': 'form-control','placeholder':'ingrese la calle','required':True}),
            'localidad':forms.TextInput(attrs={'class': 'form-control','placeholder':'ingrese la localidad','required':True}),
            'numero_calle':forms.NumberInput(attrs={'class': 'form-control','placeholder':'ingrese la calle'}),
            #'fecha_nacido':forms.DateInput(attrs={'class': 'form-control'}),
            'cuit_cuil':forms.NumberInput(attrs={'class': 'form-control','placeholder':'ingrese el cuit','required':True,'maxlength':10,'minlength':10}),
            'tipo_persona':forms.Select(attrs={'class':'form-select'}),
            'dias_de_pedido':forms.TextInput(attrs={'class':'form-control'}),
            'dias_de_reparto':forms.TextInput(attrs={'class':'form-control'}),
            'estado': forms.CheckboxInput(attrs={'class':'form-check-input','role':'switch','id':'flexSwitchCheckChecked'}),
            'telefono': forms.TextInput(attrs={'placeholder': '+1234567890', 'class': 'form-control'}),        
        }