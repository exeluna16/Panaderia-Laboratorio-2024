from django.shortcuts import render,redirect
from .models import Pedido,ItemPedido
from ..inventario.models import Insumo
from .forms import PedidoForm,ItemPedidoFormSet

# Create your views here.
def generar_pedido(request):
    #por defecto la peticion es GET asi que instancio un formulario para pedido
    pedido_form = PedidoForm()
    #conjunto de formularios de items para pedidos
    form_item_pedido = ItemPedidoFormSet()

    if request.method == 'POST':
        print('algo')
        pedido_form = PedidoForm(request.POST)

        if pedido_form.is_valid():
            #si el pedido es valido se guarda
            pedido = pedido_form.save()

            #ahora debo comprobar que los formset sean validos
            form_item_pedido = ItemPedidoFormSet(request.Post,instance=pedido)
            print(form_item_pedido.data)

            if form_item_pedido.is_valid(): #controlo que el conjunto de formularios sea valido
                #guardo todos los items
                form_item_pedido.save() 
                
                
                #-----------FALTA REDIRECIONAR A LA PAGINA NECESARIA

    return render(request,'pedido/pedidos.html',{'pedido_form':pedido_form,'form_item_pedido':form_item_pedido})