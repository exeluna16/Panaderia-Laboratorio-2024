from django.contrib.messages.context_processors import messages
from django.http import JsonResponse
from .forms import AgregarProducto
from .models import Producto, Categoria, UnidadDeMedida
from django.shortcuts import render

# Create your views here.
def stock_productos(request):
    return render(request,'inventario/stock_productos.html')


def agregar_producto(request):

    categorias = Categoria.objects.all() ##unidades de medida
    medidas = UnidadDeMedida.objects.all() ##unidades de medida

    form_producto = AgregarProducto() #formulario para producto

    if request.method == 'POST':
        form_producto(request.POST)

        if form_producto.is_valid():

            form_producto.save()#se guarda el producto
            messages.success(request,'Producto agregado exitosamente')

    return render(request,'inventario/agregar_producto.html', {'categorias':categorias,
                                                               'medidas':medidas,
                                                               'form_producto':form_producto})

##Esta vista enviará al Frontend todos los productos, mediante un JSON
def listar_productos(request):

    #obtengo todos los productos y los trasformo en un diccionario
    productos = Producto.objects.all().values('codigo','nombre','cantidad','cantidad_minima','unidad_de_medida','estado','precio','precio_mayorista','categoria')
    lista_productos = list(productos)
    return JsonResponse(lista_productos,safe=False)