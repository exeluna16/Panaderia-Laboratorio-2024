from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            return redirect('usuario:menu_principal')
        else:
            return render(request, 'usuario/login.html', {"msj": "Credenciales incorrectas"})
    return render(request,'usuario/login.html') 

#vista de deslogueo
def logout_view(request):
    logout(request)
    return render(request,'usuario/login.html',{"msj":"deslogueado"})


@login_required
def menu_principal(request):
    # Solo los usuarios autenticados pueden acceder a esta vista
    return render(request, 'menu.html')