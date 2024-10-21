from django.shortcuts import render
from .models import Venta

# Create your views here.
def primera_vista(request):
    venta = Venta.objects.get(id=1)
    print(venta.comprador)
    return render(request,'ventas/venta.html',{'venta':venta})

def principal(request):
    return render(request,'ventas/gestion_de_venta.html')

