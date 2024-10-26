from django import forms
from .models import ClienteMayorista

class ClienteMayoristaForm(forms.ModelForm):
    class Meta:
        model = ClienteMayorista
        fields = ['nombre','mail','tipo_persona','calle','localidad','numero_calle','fecha_nacido','codicionIVA']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ingrese el nombre...', 'required': True}),
            'mail': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'ingrese el mail..', 'required': True}),
            'localidad': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ingrese la localidad..', 'required': True}),
            'tipo_persona': forms.Select(attrs={'class': 'form-select'}),
            'calle': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ingrese la calle..', 'required': True}),
            'numero_calle': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'ingrese la Numero de calle..'}),
            'fecha_nacido': forms.DateTimeInput(attrs={'class': 'form-control'}),
            'codicionIVA': forms.TextInput(attrs={'class': 'form-control','placeholder': 'ingrese condicion ante el IVA','requiered':True}),

        }
