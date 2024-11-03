from django.urls import path
from .views import generar_pedido,lista_pedidos,recibir_pedido

app_name = 'pedido'

urlpatterns = [
    path('generar_pedido',generar_pedido,name='generar_pedido'),
    path('lista_pedidos',lista_pedidos,name='lista_pedidos'),
    path('recibir_pedido/<int:pk>/',recibir_pedido,name='recibir_pedido'),
]
