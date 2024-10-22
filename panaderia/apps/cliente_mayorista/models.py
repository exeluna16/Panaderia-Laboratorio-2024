from django.db import models
from ..usuario.models import Persona

# Create your models here.
class ClienteMayorista(Persona):
    codicionIVA = models.CharField(max_length=15)
