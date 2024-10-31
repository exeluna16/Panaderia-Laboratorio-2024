from django.urls import path
from .views import agregar_cliente_mayorista,modificar_cliente_mayorista


app_name='cliente_mayorista'

urlpatterns = [
    path('agregar_cliente_mayorista',agregar_cliente_mayorista,name='agregar_cliente_mayorista'),
    path('modificar_cliente_mayorista/<int:pk>',modificar_cliente_mayorista,name='modificar_cliente_mayorista')
]