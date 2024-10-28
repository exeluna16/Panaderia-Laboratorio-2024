from django.contrib.auth.forms import UserCreationForm
from .models import Usuario

#Formulario para la creacion de usuarios
class UsuarioForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = UserCreationForm.Meta.fields + ('nombre','cuit')