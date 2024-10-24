from django.contrib import messages
from django.http import JsonResponse
from .forms import AgregarProductoForm
from .models import Producto, Categoria, UnidadDeMedida
from django.shortcuts import render, redirect


# Create your views here.
def stock_productos(request):
    productos = Producto.objects.all()
    return render(request,'inventario/stock_productos.html', {'productos': productos})

#
def agregar_producto(request):

    form_producto = AgregarProductoForm() #formulario para producto

    if request.method == 'POST':
        form_producto = AgregarProductoForm(request.POST)

        if form_producto.is_valid():

            categoria = request.POST.get('categoria')
            medida = request.POST.get('unidad_de_medida')

            form_producto.save()#se guarda el producto
            messages.success(request,'Producto agregado exitosamente')
            return redirect('agregar_producto')
    return render(request,'inventario/agregar_producto.html',{'form_producto':form_producto})


##Esta vista enviará al Frontend todos los productos, mediante un JSON
def listar_productos(request):

    #obtengo todos los productos y los trasformo en un diccionario
    productos = Producto.objects.all().values('codigo','nombre','cantidad','cantidad_minima','unidad_de_medida','estado','precio','precio_mayorista','categoria')
    lista_productos = list(productos)
    return JsonResponse(lista_productos,safe=False)