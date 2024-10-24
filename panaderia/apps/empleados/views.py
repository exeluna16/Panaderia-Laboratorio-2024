from django.contrib import messages
from django.shortcuts import render
from .forms import AgregarEmpleadoForm
from .models import Empleado


# Create your views here.
def agregar_empleado(request):
    formulario = AgregarEmpleadoForm()
    if(request.method == 'POST'):
        formulario = AgregarEmpleadoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,'El empleado se agregó correctamente')


    return render(request,'empleados/agregar_empleado.html',{'formulario':formulario})


def lista_empleados(request):
    empleados = Empleado.objects.all()
    return render(request,'empleados/empleados.html',{'empleados':empleados})