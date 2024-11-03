from django.contrib import messages
from django.http import JsonResponse
from .forms import AgregarProductoForm, AgregarInsumoForm ,ModificarProductoForm, ModificarInsumoForm
from .models import Producto, Insumo
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='usuario:login')
def stock_productos(request):
    productos = Producto.objects.all()
    return render(request,'inventario/stock_productos.html', {'productos': productos})

@login_required(login_url='usuario:login')
def agregar_producto(request):

    form_producto = AgregarProductoForm() #formulario para producto

    if request.method == 'POST':
        form_producto = AgregarProductoForm(request.POST)

        if form_producto.is_valid():

            categoria = request.POST.get('categoria')
            medida = request.POST.get('unidad_de_medida')

            form_producto.save()#se guarda el producto
            messages.success(request,'Producto agregado exitosamente')
            return redirect('inventario:stock_productos')
    return render(request,'inventario/agregar_producto.html',{'form_producto':form_producto})

@login_required(login_url='usuario:login')
def modificar_producto(request,pk):
    #Se pasa como dato el modelo (Producto) y se comprara el id con la pk(primary key)
    producto = get_object_or_404(Producto,id=pk)
    if request.method =='POST':
        formulario = ModificarProductoForm(request.POST,instance=producto)
        if formulario.is_valid():
            formulario.save()
            print('se guardo correctamente')
            return redirect('inventario:stock_productos')
    formulario = ModificarProductoForm(instance=producto)
    return render(request,'inventario/modificar_producto.html',{'form_producto':formulario})

def eliminar_producto(request, pk):
    producto = get_object_or_404(Producto, id=pk)
    
    if request.method == 'POST':
        producto.estado = False
        producto.save()
        return redirect('inventario:stock_productos')
    
    else:
        messages.error(request, "La cancelación no se pudo completar.")
        return redirect('inventario:stock_productos')

##Esta vista enviará al Frontend todos los productos, mediante un JSON
def listar_productos(request): #el request se muestra en otro color porque no se usa, la solicitud siempre es GET
    #Esta funcion solo necesita los productos activos por lo tanto se hace uso de .filter()
    # Obtiene todos los productos y sus datos de unidad de medida usando select_related()
    productos = Producto.objects.filter(estado=True).select_related('unidad_de_medida')
    # creo un diccionario con los datos de los productos para porder enviarlos como un JSON.
    
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

@login_required(login_url='usuario:login')
def agregar_insumo(request):
    form = AgregarInsumoForm()
    if request.method=='POST':
        form = AgregarInsumoForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('inventario:almacen_insumos')

    return render(request,'inventario/agregar_insumo.html',{'form':form})

@login_required(login_url='usuario:login')
def modificar_insumo(request,pk):
    insumo = get_object_or_404(Insumo,id=pk)
    if request.method == 'POST':
        form = ModificarInsumoForm(request.POST, instance=insumo)
        if form.is_valid():
            form.save()
            return redirect('inventario:almacen_insumos')
    form = ModificarInsumoForm(instance=insumo)
    return render(request,'inventario/modificar_insumo.html',{'form':form})

def eliminar_insumo(request, pk):
    insumo = get_object_or_404(Insumo, id=pk)
    
    if request.method == 'POST':
        insumo.estado = False
        insumo.save()
        return redirect('inventario:almacen_insumos')
    
    else:
        messages.error(request, "La cancelación no se pudo completar.")
        return redirect('inventario:almacen_insumos')

@login_required(login_url='usuario:login')
def almacen_insumos(request):
    insumos = Insumo.objects.all()
    return render(request,'inventario/almacen_insumos.html',{'insumos':insumos})


def listar_insumos(request):
    insumos = Insumo.objects.filter(estado = True).select_related('unidad_de_medida')

    lista_insumos = [
        {
            'id': insumo.id,
            'nombre':insumo.nombre,
            'cantidad':insumo.cantidad,
            'cantidad_minima':insumo.cantidad_minima,
            'unidad_de_medida':insumo.unidad_de_medida.unidad_medida_nombre,
            'ultimo_precio':insumo.ultimo_precio,
        }
        for insumo in insumos
    ]
    return JsonResponse(lista_insumos,safe=False)