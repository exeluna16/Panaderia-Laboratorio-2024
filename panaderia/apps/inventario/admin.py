from django.contrib import admin
from .models import UnidadDeMedida, Categoria

# Register your models here.
@admin.register(UnidadDeMedida)
class UnidadDeMedidaAdmin(admin.ModelAdmin):
    list_display = ['unidad_medida_nombre']

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['descripcion']