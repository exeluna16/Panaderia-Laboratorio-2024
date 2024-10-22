from django.shortcuts import render
from .models import Venta
from ..inventario.models import Producto
from .forms import VentaForm

# Create your views here.
def primera_vista(request): ##CAMBIARLE EL NOMBRE

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
    return render(request,'ventas/venta.html', {'venta':venta}) #NECESITO QUE SE QUEDE EN LA MISMA PAGINA

def principal(request):


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
    return render(request,'ventas/gestion_de_venta.html',{'venta':venta})


