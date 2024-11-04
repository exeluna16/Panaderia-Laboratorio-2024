from django.shortcuts import render,redirect,get_object_or_404
from .models import Pedido,ItemPedido
from ..inventario.models import Insumo
from .forms import PedidoForm,ItemPedidoFormSet,ItemRecepcionPedidoFormSet,RecepcionPedidoForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='usuario:login')
def generar_pedido(request):
    #por defecto la peticion es GET asi que instancio un formulario para pedido
    pedido_form = PedidoForm()
    #conjunto de formularios de items para pedidos
    form_item_pedido = ItemPedidoFormSet()

    if request.method == 'POST':
        pedido_form = PedidoForm(request.POST)

        if pedido_form.is_valid():
            #si el pedido es valido se guarda
            pedido = pedido_form.save()
            #ahora debo comprobar que los formset sean validos
            form_item_pedido = ItemPedidoFormSet(request.POST,instance=pedido)

            if form_item_pedido.is_valid(): #controlo que el conjunto de formularios sea valido
                #guardo todos los items
                form_item_pedido.save() 
                return redirect('pedido:lista_pedidos')
                #-----------FALTA REDIRECIONAR A LA PAGINA NECESARIA
    return render(request,'pedido/registrar_pedido.html',{'pedido_form':pedido_form,'form_item_pedido':form_item_pedido})

@login_required(login_url='usuario:login')
def lista_pedidos(request):
    pedidos = Pedido.objects.all().select_related('id_proveedor')
    return render(request,'pedido/lista_pedidos.html',{'pedidos':pedidos})

@login_required(login_url='usuario:login')
def recibir_pedido(request,pk):
    
    #traigo el pedido que acaba de ingresar
    pedido = get_object_or_404(Pedido, id=pk)
    
    recepcion_form = RecepcionPedidoForm()
    #creo el conjunto de formularios y le paso el pedido que acaba de llegar
    formset = ItemRecepcionPedidoFormSet(request.POST or None, instance=pedido)
    
    if request.method == 'POST' and formset.is_valid():
        recepcion_form = RecepcionPedidoForm(request.POST)
        
        if recepcion_form.is_valid():
            
            recepcion = recepcion_form.save(commit=False)
            recepcion.empleado = request.user #coloco el usuario
            recepcion.proveedor_id = pedido.id_proveedor_id #coloco el proveedor
            recepcion.pedido_id = pedido.id
            recepcion.save()
            pedido.estado = 'RECIBIDO' 
            pedido.save()
        for form in formset:
            item = form.save(commit=False) #evito que se guarde el formulario
            #actualizo la cantidad de los insumos
            insumo = Insumo.objects.get(id=item.insumo_id)
            
            insumo.cantidad = insumo.cantidad + item.cantidad_recibida
            #guardo el insumo
            insumo.save()

        formset.save()
        return redirect('pedido:lista_pedidos')
        
    return render(request,'pedido/recepcion_pedido.html',{'formset':formset,'recepcion_form':recepcion_form})