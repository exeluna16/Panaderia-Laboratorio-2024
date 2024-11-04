from django import forms
from .models import ClienteMayorista

class ClienteMayoristaForm(forms.ModelForm):
    
    class Meta:
        model = ClienteMayorista
        fields = ['nombre','telefono','mail','tipo_persona','calle','localidad','numero_calle','condicionIVA','cuit_cuil']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese nombre...', 'required': True}),
            'mail': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el mail..', 'required': True}),
            'localidad': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la localidad..', 'required': True}),
            'tipo_persona': forms.Select(attrs={'class': 'form-select'}),
            'calle': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la calle..', 'required': True}),
            'numero_calle': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'ingrese la Numero de calle..'}),
            'condicionIVA': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Ingrese condicion ante el IVA','required':True}),
            'cuit_cuil':forms.TextInput(attrs={'class': 'form-control','placeholder':'Ingrese el CUIT/CUIL','required':True}),
            'telefono': forms.TextInput(attrs={'placeholder': '+1234567890', 'class': 'form-control'}),
        }

class ModificarClienteMayoristaForm(forms.ModelForm):
    
    class Meta:
        model = ClienteMayorista
        fields = ['nombre','telefono','mail','tipo_persona','calle','localidad','numero_calle','condicionIVA','estado','cuit_cuil']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ingrese el nombre...', 'required': True}),
            'mail': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'ingrese el mail..', 'required': True}),
            'localidad': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ingrese la localidad..', 'required': True}),
            'tipo_persona': forms.Select(attrs={'class': 'form-select'}),
            'calle': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ingrese la calle..', 'required': True}),
            'numero_calle': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'ingrese la Numero de calle..'}),
            'condicionIVA': forms.TextInput(attrs={'class': 'form-control','placeholder': 'ingrese condicion ante el IVA','required':True}),
            'estado': forms.CheckboxInput(attrs={'class':'form-check-input','role':'switch','id':'flexSwitchCheckChecked'}),
            'cuit_cuil':forms.TextInput(attrs={'class': 'form-control','placeholder':'ingrese el cuit','required':True,'maxlength':10,'minlength':10}),
            'telefono': forms.TextInput(attrs={'placeholder': '+1234567890', 'class': 'form-control'}),
        }