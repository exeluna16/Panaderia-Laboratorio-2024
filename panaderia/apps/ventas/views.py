from django.shortcuts import render, redirect
from django.views.generic import FormView

from .models import Venta, ItemVenta
from ..inventario.models import Producto
from .forms import VentaForm, ItemVentaForm, ItemVentaFormSet ,ItemMayoristaForm
from django.forms import formset_factory,inlineformset_factory ## crea varios formularios del mismo tipo
from django.contrib import messages

# Create your views here.
def primera_vista(request): ##CAMBIARLE EL NOMBRE
    venta = Venta.objects.get(id=1)

    if request.method == 'POST':
        formset = ItemVentaFormSet(request.POST, instance=venta)
        print(formset)
        print('request.pots')
        if formset.is_valid():
            print('se guardo')
            formset.save()
    else:
        formset =ItemVentaFormSet()
    return render(request,'ventas/venta.html', {'formset':formset}) #NECESITO QUE SE QUEDE EN LA MISMA PAGINA

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

