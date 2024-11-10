from django.urls import path
from .views import listar_productos,agregar_producto,stock_productos,agregar_insumo,modificar_producto,modificar_insumo,almacen_insumos,eliminar_producto,listar_insumos,eliminar_insumo,descontar_insumos,reporte_insumos_faltantes

app_name = 'inventario'

urlpatterns = [
    path('stock_productos',stock_productos,name='stock_productos'),
    path('agregar_producto',agregar_producto,name='agregar_producto'),
    path('modificar_producto/<int:pk>/',modificar_producto,name='modificar_producto'),
    path('eliminar_producto/<int:pk>/',eliminar_producto,name='eliminar_producto'),
    path('listar_productos',listar_productos,name='listar_productos'),
    path('agregar_insumo',agregar_insumo,name='agregar_insumo'),
    path('modificar_insumo/<int:pk>/',modificar_insumo,name='modificar_insumo'),
    path('eliminar_insumo/<int:pk>/',eliminar_insumo,name='eliminar_insumo'),
    path('almacen_insumos/',almacen_insumos,name='almacen_insumos'),
    path('listar_insumos',listar_insumos,name='listar_insumos'),
    path('descontar_insumos',descontar_insumos,name='descontar_insumos'),
    path('reporte/',reporte_insumos_faltantes,name='reporte_insumos_faltantes'),
]