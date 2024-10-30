from django import forms
from .models import Empleado


class AgregarEmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['nombre','mail','calle','localidad','numero_calle','fecha_nacido','cuit','cargo','tipo_persona']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control','placeholder':'nombre completo...','required':True}),
            'mail':forms.EmailInput(attrs={'class': 'form-control','placeholder':'ingrese el mail...','required':True}),
            'calle':forms.TextInput(attrs={'class': 'form-control','placeholder':'ingrese la calle','required':True}),
            'localidad':forms.TextInput(attrs={'class': 'form-control','placeholder':'ingrese la localidad','required':True}),
            'numero_calle':forms.NumberInput(attrs={'class': 'form-control','placeholder':'ingrese la calle'}),
            'fecha_nacido':forms.DateInput(attrs={'class': 'form-control'}),
            'cuit':forms.NumberInput(attrs={'class': 'form-control','placeholder':'ingrese el cuit','required':True,'maxlength':10,'minlength':10}),
            'cargo':forms.Select(attrs={'class':'form-select'}),
            'tipo_persona':forms.HiddenInput(),
        }

class ModificarEmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['nombre','mail','calle','localidad','numero_calle','fecha_nacido','cuit','cargo','estado']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control','placeholder':'nombre completo...','required':True}),
            'mail':forms.EmailInput(attrs={'class': 'form-control','placeholder':'ingrese el mail...','required':True}),
            'calle':forms.TextInput(attrs={'class': 'form-control','placeholder':'ingrese la calle','required':True}),
            'localidad':forms.TextInput(attrs={'class': 'form-control','placeholder':'ingrese la localidad','required':True}),
            'numero_calle':forms.NumberInput(attrs={'class': 'form-control','placeholder':'ingrese la calle'}),
            'fecha_nacido':forms.DateInput(attrs={'class': 'form-control'}),
            'cuit':forms.NumberInput(attrs={'class': 'form-control','placeholder':'ingrese el cuit','required':True,'maxlength':10,'minlength':10}),
            'cargo':forms.Select(attrs={'class':'form-select'}),
            'estado': forms.CheckboxInput(attrs={'class':'form-check-input','role':'switch','id':'flexSwitchCheckChecked'}),        
        }
