from django.shortcuts import render,get_object_or_404, redirect
from .forms import ClienteMayoristaForm,ModificarClienteMayoristaForm
from django.contrib.auth.decorators import login_required #controla el usaurio logueado
from .models import ClienteMayorista
from django.contrib import messages
from django.http import JsonResponse
# Create your views here.
#controla que el usuario este logueado, si no lo esta lo redireciona al login
@login_required(login_url='usuario:login')
def agregar_cliente_mayorista(request):
    form = ClienteMayoristaForm()
    if request.method=='POST':
        form = ClienteMayoristaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('cliente_mayorista:listado_clientes')
    return render(request,'cliente_mayorista/registro_de_mayorista.html',{'form':form})

@login_required(login_url='usuario:login')
def modificar_cliente_mayorista(request,pk):
    cliente = get_object_or_404(ClienteMayorista,id=pk)
    if request.method == 'POST':
        form = ModificarClienteMayoristaForm(request.POST,instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('cliente_mayorista:listado_clientes')
    form = ModificarClienteMayoristaForm(instance=cliente)
    return render(request,'cliente_mayorista/modificar_cliente_mayorista.html',{'form':form})

def eliminar_cliente(request,pk):
    cliente = get_object_or_404(ClienteMayorista, id=pk)
    
    if request.method == 'POST':
        cliente.estado = False
        cliente.save()
        return redirect('cliente_mayorista:listado_clientes')
    
    else:
        messages.error(request, "La cancelación no se pudo completar.")
        return redirect('cliente_mayorista:listado_clientes')

@login_required(login_url='usuario:login')
def listar_clientes(request):
    clientes = ClienteMayorista.objects.all()
    return render(request,'cliente_mayorista/listado_clientes.html',{'clientes':clientes})


def ver_clientes_mayoristas(render):
    clientes_mayoristas = ClienteMayorista.objects.filter(estado=True)
    lista_clientes = [
        {   
            'id':mayorista.id,
            'nombre': mayorista.nombre,
        }
        for mayorista in clientes_mayoristas
    ]
    return JsonResponse(lista_clientes,safe=False)