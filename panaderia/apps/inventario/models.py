from django.db import models

# Create your models here.
'''Se define la unidad de medida para los distintos productos e insumos'''
class UnidadDeMedida(models.Model):
    unidad_medida_nombre = models.CharField(max_length=15,null=False) #la clave foranea no puede ser nula

    def __str__(self): #este metodo solo me va a devolver el nombre de la unidad de medida
        return self.unidad_medida_nombre

'''Se define la categoria para los distintos productos'''
class Categoria(models.Model):
    descripcion = models.CharField(max_length=50,null=False)

    def __str__(self):
        return self.descripcion

'''Se define el modelo de insumo'''
class Insumo(models.Model):

    codigo = models.IntegerField(unique=True)
    nombre = models.CharField(max_length=150)
    cantidad = models.IntegerField()
    cantidad_minima = models.IntegerField()
    unidad_de_medida = models.ForeignKey(UnidadDeMedida,on_delete=models.CASCADE)
    estado = models.BooleanField()

'''Insumo y producto comparten atributos asi que se optará por una relacion de herencia'''
class Producto(Insumo):
    precio = models.DecimalField(decimal_places=2,max_digits=10)
    precio_mayorista = models.DecimalField(decimal_places=2,max_digits=10)
    categoria = models.ForeignKey(Categoria,on_delete=models.SET_NULL,null=True)