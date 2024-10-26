from django.shortcuts import render
from .forms import ClienteMayoristaForm
# Create your views here.
def agregar_cliente_mayorista(request):
    form = ClienteMayoristaForm()
    if request.method=='POST':
        form = ClienteMayoristaForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request,'cliente_mayorista/registro_de_mayorista.html',{'form':form})