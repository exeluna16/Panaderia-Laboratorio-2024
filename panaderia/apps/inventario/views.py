from django.http import JsonResponse
from .models import Producto
from django.shortcuts import render

# Create your views here.
def agregar_producto(request):
    return render(request,'inventario/agregar_producto.html')

##Esta vista enviará al Frontend todos los productos, mediante un JSON
def listar_productos(request):

    #obtengo todos los productos y los trasformo en un diccionario
    productos = Producto.objects.all().values('codigo','nombre','cantidad','cantidad_minima','unidad_de_medida','estado','precio','precio_mayorista','categoria')
    lista_productos = list(productos)
    return JsonResponse(lista_productos,safe=False)