from django.shortcuts import render, redirect
from .models import Venta, ItemVenta
from ..inventario.models import Producto
from .forms import VentaForm, ItemVentaForm, ItemVentaFormSet ,ItemMayoristaForm
from django.forms import formset_factory,inlineformset_factory ## crea varios formularios del mismo tipo
from django.contrib import messages
from django.contrib.auth.decorators import login_required,permission_required
from ..inventario.utils import generar_reporte_tabla
from django.db.models import Sum

# Create your views here.
@login_required(login_url='usuario:login')
@permission_required('inventario.add_venta',raise_exception=True)
def principal(request):
    #POR defecto el metodo de ingreso es GET por lo tanto debemos crear amos focmularios
    venta_form = VentaForm()  #crea un nuevo formulario
    form_item_venta = ItemVentaFormSet()#crea un nuevo formulario
    item_mayorista = ItemMayoristaForm()

    if request.method == 'POST': #cuando el formulario es enviado se comprueban sus datos

        venta_form = VentaForm(request.POST) ##--> se mandan los datos de la pagina al formulario de la venta para ver si coincide con el modelo

        if venta_form.is_valid(): # --> si la venta es valida

            venta = venta_form.save(commit=False)  # Se guarda la venta y se intancia un modelo
            venta.empleado = request.user ##toma el usuario que esta loguado
            #
            item_mayorista = ItemMayoristaForm(request.POST)
            
            #se guarda la venta
            venta.save()
            form_item_venta = ItemVentaFormSet(request.POST, instance=venta) #se le envia al formset la clase padre de la que debe heredar
            
            if form_item_venta.is_valid(): #si los formset son validos ingresara
                #AHORA SE EVITA QUE SE GUARDE EL FORMULARIO HASTA QUE SE ACTUALICEN LAS CANTIDADES DE LOS PRODUCTOS
                items = form_item_venta.save(commit=False) 
                for item in items:
                    #se trae el producto por su id
                    producto = Producto.objects.get(id = item.producto.id)
                    #descuento la cantidad del producto
                    producto.cantidad -= item.cantidad
                    #actualizo la cantidad en la BD
                    producto.save()
                #se guardan todos los formset
                form_item_venta.save()
                
                if item_mayorista.is_valid(): #si no es valido es porque no se selecciono un mayorista
                    carga_mayorista = item_mayorista.save(commit=False)
                    carga_mayorista.venta = venta
                    carga_mayorista.save()
                    
                    return redirect('ventas:principal') #RECARGA LA PAGINA

            return redirect('ventas:principal') #RECARGA LA PAGINA
        
    return render(request,'ventas/gestion_de_venta.html',{'venta':venta_form ,'form_item_venta':form_item_venta,'item_mayorista':item_mayorista})


@login_required(login_url='usuario:login')
@permission_required('inventario.view_venta',raise_exception=True)
def reporte_ventas(request):
    fecha_inicio = request.POST.get('fecha_inicio')
    fecha_fin = request.POST.get('fecha_fin')
    
    ventas = Venta.objects.filter(fecha_venta__range=(fecha_inicio,fecha_fin)).select_related('empleado')
    
    datos = [
        ['Fecha','vendedor','Forma de Pago','Total']
    ]
    for venta in ventas:
        datos.append([
            venta.fecha_venta,
            venta.empleado,
            venta.forma_de_pago,
            venta.total_venta
        ])

    return generar_reporte_tabla(datos,"Ventas",nombre_archivo="Registro de Ventas.pdf")


def reporte_productos_mas_vendidos(request):
    fecha_inicio = request.POST.get('fecha_inicio')
    fecha_fin = request.POST.get('fecha_fin')
    #consulta para traer los productos vendidos durante el rango de fechas indicado
    productos = ItemVenta.objects.filter(venta__fecha_venta__range=(fecha_inicio,fecha_fin)).values('producto__nombre').annotate(total_vendido=Sum('cantidad')).order_by('-total_vendido')
    
    datos = [
        ['Producto','Total Vendido']
    ]
    
    for producto in productos:
        datos.append([
            producto.get('producto__nombre'),
            producto.get('total_vendido')
        ])

    return generar_reporte_tabla(datos,"Productos más vendidos",nombre_archivo="Productos más vendidos.pdf")