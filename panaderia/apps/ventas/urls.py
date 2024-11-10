from django.urls import path
from .views import principal,reporte_ventas

app_name = 'ventas'

urlpatterns = [
    path('principal',principal,name='principal'),
    path('reporte',reporte_ventas,name='reporte_ventas')
]