from django.shortcuts import render
from .forms import ClienteMayoristaForm
from django.contrib.auth.decorators import login_required #controla el usaurio logueado
# Create your views here.
#controla que el usuario este logueado, si no lo esta lo redireciona al login
@login_required(login_url='usuario:login')
def agregar_cliente_mayorista(request):
    form = ClienteMayoristaForm()
    if request.method=='POST':
        form = ClienteMayoristaForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request,'cliente_mayorista/registro_de_mayorista.html',{'form':form})