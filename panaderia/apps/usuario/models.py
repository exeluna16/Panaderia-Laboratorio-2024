from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=150)

    def __str__(self):
        return f'{self.nombre}'