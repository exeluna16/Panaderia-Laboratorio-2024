from django.urls import path
from .views import listar_productos

app_name = 'inventario'

urlpatterns = [
    path('listar_productos',listar_productos,name='listar_productos'),
]