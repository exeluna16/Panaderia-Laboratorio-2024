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


'''Insumo y Producto comparten atributos asi que se optará por una relacion de herencia con la clase
Articulo la cual será abstracta'''
class Articulo(models.Model):

    codigo = models.IntegerField(unique=True)
    nombre = models.CharField(max_length=150)
    cantidad = models.IntegerField()
    cantidad_minima = models.IntegerField()
    unidad_de_medida = models.ForeignKey(UnidadDeMedida,on_delete=models.CASCADE)
    estado = models.BooleanField(default=True)

    #esta clase hace que el modelo no persista en la BD pero sus hijos si lo harán
    class Meta:
        abstract = True

'''Se define el modelo de insumo'''
class Insumo(Articulo):
    ultimo_precio = models.DecimalField(decimal_places=2,max_digits=10,blank=True)

'''Se define el modelo Producto'''
class Producto(Articulo):
    precio = models.DecimalField(decimal_places=2,max_digits=10)
    precio_mayorista = models.DecimalField(decimal_places=2,max_digits=10)
    categoria = models.ForeignKey(Categoria,on_delete=models.SET_NULL,null=True,related_name='categoria')