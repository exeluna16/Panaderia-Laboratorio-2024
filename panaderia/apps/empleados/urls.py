from django.urls import path
from .views import agregar_empleado,lista_empleados,modificar_empleado,eliminar_empleado

app_name = 'empleados'

urlpatterns = [
    path('agregar_empleado',agregar_empleado,name='agregar_empleado'),
    path('modificar_empleado/<int:pk>/',modificar_empleado,name='modificar_empleado'),
    path('lista_empleados',lista_empleados,name='lista_empleados'),
    path('eliminar_empleado/<int:pk>',eliminar_empleado,name='eliminar_empleado'),
]