from django.shortcuts import render,redirect,get_object_or_404
from .models import Proveedor
from .forms import AgregarProveedorForm,ModificarProveedorForm
from django.http import JsonResponse

# Create your views here.
def agregar_proveedor(request):

    form = AgregarProveedorForm()
    if request.method == 'POST':
        form = AgregarProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('proveedor:listar_proveedores')
    
    return render(request,'proveedores/agregar_proveedor.html',{'form':form})


def modificar_proveedor(request,pk):
    proveedor = get_object_or_404(Proveedor,id=pk)
    form = ModificarProveedorForm(instance=proveedor)
    if request.method == 'POST':
        form = ModificarProveedorForm(request.POST,instance=proveedor)
        if form.is_valid():
            form.save()
            return redirect('proveedor:listar_proveedores')

    return render(request,'proveedores/modificar_proveedor.html',{'form':form})


def listar_proveedores(request):
    proveedores=Proveedor.objects.all()
    return render(request,'proveedores/listar_proveedores.html',{'proveedores':proveedores})


def ver_proveedores(request):
    #filtro los proveedores que estan activos unicamente
    proveedores = Proveedor.objects.filter(estado=True)
    lista_proveedores = [
        {
            'id': proveedor.id,
            'nombre':proveedor.nombre,
        }
        for proveedor in proveedores
    ]

    return JsonResponse(lista_proveedores,safe=False)