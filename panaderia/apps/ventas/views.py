from django.shortcuts import render, redirect
from .models import Venta
from ..inventario.models import Producto
from .forms import VentaForm, ItemVentaForm
from django.forms import formset_factory ## crea varios formularios del mismo tipo
from django.contrib import messages

# Create your views here.
def primera_vista(request): ##CAMBIARLE EL NOMBRE
    productos = Producto.objects.all()

    if request.method == 'POST': ## ---> se reazlia la venta
        venta = VentaForm(request.POST) ##--> se mandan los datos de la pagina al formulario de la venta para ver si coincide con el modelo
        if venta.is_valid(): # --> si la venta es valida


            #se guarda la venta
            venta.save()
            print('se guardo la venta')
        else:
            print(venta.is_valid())
            print('el formulario no es valido')
    else:
        print('request.method = ' + request.method)

        venta = VentaForm() ##crea un nuevo formulario
        print('venta abajo')
        print(venta)
    return render(request,'ventas/venta.html', {'venta':venta , 'productos':productos}) #NECESITO QUE SE QUEDE EN LA MISMA PAGINA

def principal(request):

    productos = Producto.objects.all() ##se traen todos los productos de la base de datos.
    # aca voy a crear tantos items de venta como productos ingrese el usuario
    form_item_venta = formset_factory(ItemVentaForm, extra=1,can_delete=True)

    if request.method == 'POST': ## ---> se reazlia la venta
        venta = VentaForm(request.POST) ##--> se mandan los datos de la pagina al formulario de la venta para ver si coincide con el modelo


        print(request.POST.get('total_venta'))
        print(request.POST.get('comprador'))
        '''INGRESAR LOGICA PARA OIDENTIFICAR AL EMPLEADO QUE HACE LA VENTA'''
        venta_2 = venta.save(commit=False)  # Evitar guardar de inmediato
        venta_2.empleado = 1
        print(f'el id de esta venta es: {venta_2.id}')
        #tengo que poner ese id en todos los items
        for item in form_item_venta:
            item.venta = venta_2.id
        if venta.is_valid() and form_item_venta.is_valid(): # --> si la venta es valida
            print('son validos los campos')
            #se guarda la venta
            venta.save()
            messages.success(request, 'La venta se guardó correctamente')  #puedo hacer que el mensaje salga en la esquina
            print('se guardo la venta')

        else:
            print('la venta es no valida')
    else: #si la peticion es GET

        venta = VentaForm() ##crea un nuevo formulario
        print('no pasa nada')
    return render(request,'ventas/gestion_de_venta.html',{'venta':venta ,'productos':productos, 'form_item_venta':form_item_venta})



