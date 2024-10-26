from django.urls import path
from .views import listar_productos,agregar_producto,stock_productos,agregar_insumo

app_name = 'inventario'

urlpatterns = [
    path('stock_productos',stock_productos,name='stock_productos'),
    path('agregar_producto',agregar_producto,name='agregar_producto'),
    path('listar_productos',listar_productos,name='listar_productos'),
    path('agregar_insumo',agregar_insumo,name='agregar_insumo')
]