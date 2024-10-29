from django.shortcuts import render, redirect
from django.views.generic import FormView

from .models import Venta, ItemVenta
from ..inventario.models import Producto
from .forms import VentaForm, ItemVentaForm, ItemVentaFormSet
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

    if request.method == 'POST': #cuando el formulario es enviado se comprueban sus datos

        venta_form = VentaForm(request.POST) ##--> se mandan los datos de la pagina al formulario de la venta para ver si coincide con el modelo

        if venta_form.is_valid(): # --> si la venta es valida

            venta = venta_form.save()  # Se guarda la venta y se intancia un modelo

            form_item_venta = ItemVentaFormSet(request.POST, instance=venta) #se le envia al formset la clase padre de la que debe heredar
            
            if form_item_venta.is_valid(): #si los formset son validos ingresara
                print(form_item_venta.data)
                #AHORA SE EVITA QUE SE GUARDE EL FORMULARIO HASTA QUE SE ACTUALICEN LAS CANTIDADES DE LOS PRODUCTOS
                items = form_item_venta.save(commit=False) 
                for item in items:
                    #se trae el producto por su id
                    producto = Producto.objects.get(id = item.producto.id)
                    #descuento la cantidad del producto
                    producto.cantidad -= item.cantidad
                    #actualizo la cantidad en la BD
                    producto.save()

                    print(f'nueva cantidad del producto {producto.cantidad}')
                    
                #se guardan todos los formset
                form_item_venta.save() 
                
                #messages.success(request, 'La venta se guardó correctamente')  #puedo hacer que el mensaje salga en la esquina
                print('se guardo la venta')
                
            return redirect('ventas:principal') #RECARGA LA PAGINA
        
    return render(request,'ventas/gestion_de_venta.html',{'venta':venta_form ,'form_item_venta':form_item_venta})

