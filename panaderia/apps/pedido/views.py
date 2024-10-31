from django.shortcuts import render

# Create your views here.
def generar_pedido(request):
    return render(request,'pedido/pedidos.html')