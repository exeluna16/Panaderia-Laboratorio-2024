from django.urls import path
from .views import agregar_proveedor,modificar_proveedor,listar_proveedores,ver_proveedores

app_name = 'proveedor'

urlpatterns = [
    path('agregar_proveedor',agregar_proveedor,name='agregar_proveedor'),
    path('modificar_proveedor/<int:pk>',modificar_proveedor,name='modificar_proveedor'),
    path('listar_proveedores',listar_proveedores,name='listar_proveedores'),
    path('ver_proveedores',ver_proveedores,name='ver_proveedores'),
]