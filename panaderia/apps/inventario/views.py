from django.http import JsonResponse
from .models import Producto


# Create your views here.


##Esta vista enviará al Frontend todos los productos
def listar_productos(request):

    #obtengo todos los productos y los trasformo en un diccionario
    productos = Producto.objects.all().values('codigo','nombre','cantidad','cantidad_minima','unidad_de_medida','estado','precio','precio_mayorista','categoria')
    lista_productos = list(productos)
    return JsonResponse(lista_productos,safe=False)