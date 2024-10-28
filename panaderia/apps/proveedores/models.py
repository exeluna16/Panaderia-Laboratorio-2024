from django.db import models
from ..usuario.models import Persona
# Create your models here.
class Proveedor(Persona):
    cuit = models.CharField(unique=True,null=False)
