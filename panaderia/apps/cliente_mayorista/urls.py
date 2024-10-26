from django.urls import path
from .views import agregar_cliente_mayorista


app_name='cliente_mayorista'

urlpatterns = [
    path('cliente_mayorista',agregar_cliente_mayorista,name='agregar_cliente_mayorista')
]