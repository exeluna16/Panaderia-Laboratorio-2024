from django.urls import path
from .views import principal,reporte_ventas,reporte_productos_mas_vendidos

app_name = 'ventas'

urlpatterns = [
    path('principal',principal,name='principal'),
    path('reporte',reporte_ventas,name='reporte_ventas'),
    path('producto_mas_vendido',reporte_productos_mas_vendidos,name='reporte_productos_mas_vendidos'),
]