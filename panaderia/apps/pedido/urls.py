from django.urls import path
from .views import generar_pedido

app_name = 'pedido'

urlpatterns = [
    path('pedido',generar_pedido,name='generar_pedido'),
]
