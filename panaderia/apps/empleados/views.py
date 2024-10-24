from django.contrib import messages
from django.shortcuts import render
from .forms import AgregarEmpleadoForm


# Create your views here.
def agregar_empleado(request):
    formulario = AgregarEmpleadoForm()
    if(request.method == 'POST'):
        formulario = AgregarEmpleadoForm(request.POST)
        if formulario.is_valid():

            formulario.save()
            messages.success(request,'El empleado se agregó correctamente')


    return render(request,'empleados/agregar_empleado.html',{'formulario':formulario})