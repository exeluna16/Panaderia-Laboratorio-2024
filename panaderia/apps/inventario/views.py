from django.contrib import messages
from django.http import JsonResponse
from .forms import AgregarProductoForm, AgregarInsumoForm
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
            #messages.success(request,'Producto agregado exitosamente')

            #return redirect('agregar_producto')
    return render(request,'inventario/agregar_producto.html',{'form_producto':form_producto})


##Esta vista enviará al Frontend todos los productos, mediante un JSON
def listar_productos(request):
    # Obtiene todos los productos y sus datos de unidad de medida usando select_related()
    productos = Producto.objects.select_related('unidad_de_medida').all()
    print(productos.dates)
    # creo un diccionario con los datos de los productos para porder enviarlos como un JSON.
    #
    lista_productos = [
        {
            'id': producto.id,
            'codigo': producto.codigo,
            'nombre': producto.nombre,
            'cantidad': producto.cantidad,
            'cantidad_minima': producto.cantidad_minima,
            'unidad_de_medida': producto.unidad_de_medida.unidad_medida_nombre,
            'estado': producto.estado,
            'precio': producto.precio,
            'precio_mayorista': producto.precio_mayorista,
            'categoria': producto.categoria.id
        }
        #acá recorro cada instancia del Qeryset de productos
        for producto in productos #Este tipo de bucle es una lista por comprensión que crea una nueva lista en el mismo paso en que recorre los productos.
    ]
    return JsonResponse(lista_productos, safe=False)


def agregar_insumo(request):
    form = AgregarInsumoForm()
    if request.method=='POST':
        form = AgregarInsumoForm(request.POST)

        if form.is_valid():
            form.save()
            print('el insumo se guardo correctamente')

    return render(request,'inventario/agregar_insumo.html',{'form':form})