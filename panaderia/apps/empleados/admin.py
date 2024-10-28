from django.contrib import admin
from .models import Empleado,Cargo

# Register your models here.
@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ['nombre','mail','tipo_persona','fecha_ingreso']

@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ['id','descripcion']
