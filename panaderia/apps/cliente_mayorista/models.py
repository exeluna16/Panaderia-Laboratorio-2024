from django.db import models
from ..usuario.models import Persona

# Create your models here.
class ClienteMayorista(Persona):
    condicionIVA = models.CharField(max_length=15)
