'''Este modelo contendrá clases que se usaran en otros modelos,
pero NO seran persistidas en la Base de Datos
'''
from django.db import models

class Estado(models.Model):
    OPCIONES_ESTADO = [
        ('activo', 'Activo'),
        ('inactivo', 'Inactivo'),
    ]

    tipo_estado = models.CharField(max_length=15,choices=OPCIONES_ESTADO,default='activo')

    #metodo para dar el alta
    def activar(self):
        self.tipo_estado = 'activo'
        self.save() #---> puede que dé error porque es abstracto y se esta queriendo guardar

    #metodo para la baja logica
    def desactivar(self):
        self.tipo_estado = 'inactivo'
        self.save()

    '''para que el modelo no persista en la BD se agrega la clase Meta
    el campo abstract indica si se va a persistir el modelo, abstract es un campo Booleano'''
    class Meta:
        abstract = True