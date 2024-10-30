from django.contrib import messages
from django.shortcuts import render,redirect,get_object_or_404
from .forms import AgregarEmpleadoForm,ModificarEmpleadoForm
from .models import Empleado


# Create your views here.
def agregar_empleado(request):
    formulario = AgregarEmpleadoForm()
    if(request.method == 'POST'):
        formulario = AgregarEmpleadoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('empleados:lista_empleados')
    return render(request,'empleados/agregar_empleado.html',{'formulario':formulario})

def modificar_empleado(request,pk):
    empleado = get_object_or_404(Empleado,id=pk)
    if request.method == 'POST':
        form = ModificarEmpleadoForm(request.POST,instance=empleado)
        if form.is_valid():
            form.save()
            return redirect('empleados:lista_empleados')
    form = ModificarEmpleadoForm(instance=empleado)
    return render(request,'empleados/modificar_empleado.html',{'form':form})

def lista_empleados(request):
    empleados = Empleado.objects.all()
    return render(request,'empleados/empleados.html',{'empleados':empleados})