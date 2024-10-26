from django.db import models
from ..usuario.models import Persona
# Create your models here.
class Proveedor(Persona):
    cuit = models.IntegerField(unique=True,null=False)
