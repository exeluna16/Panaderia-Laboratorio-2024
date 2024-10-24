from django.urls import path
from .views import agregar_empleado

app_name = 'empleados'

urlpatterns = [
    path('agregar_empleado',agregar_empleado,name='agregar_empleado'),
]