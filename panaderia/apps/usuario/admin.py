from django.contrib import admin
from .models import Usuario
from .forms import UsuarioForm
from django.contrib.auth.admin import UserAdmin

# Register your models here.
@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    # Usa la clase en lugar de la instancia de UsuarioForm
    add_form = UsuarioForm
    model = Usuario
    
    # Asegúrate de que UserAdmin tenga configurado el campo 'add_fieldsets'
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Información Personal', {'fields': ('nombre', 'cuit', 'email')}),
        ('Permisos', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'nombre', 'cuit', 'email'),
        }),
    )

    # Campo de búsqueda configurado para cuit, email y username
    search_fields = ('email', 'username', 'cuit',)
    ordering = ('username',)