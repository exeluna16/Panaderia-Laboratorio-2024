from django.urls import path
from .views import agregar_empleado,lista_empleados

app_name = 'empleados'

urlpatterns = [
    path('agregar_empleado',agregar_empleado,name='agregar_empleado'),
    path('lista_empleados',lista_empleados,name='lista_empleados'),
]