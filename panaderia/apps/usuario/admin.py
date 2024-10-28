from django.contrib import admin
from .models import Usuario
from .forms import UsuarioForm
from django.contrib.auth.admin import UserAdmin

# Register your models here.
@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    add_form = UsuarioForm()
    fieldsets = UserAdmin.fieldsets + ((None,{'fields':('nombre','cuit')}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None,{'fields':('nombre','cuit')}),)
    search_fields = ('email','username','cuit',)

