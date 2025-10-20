from django.db import models

# Create your models here.
class Proyecto(models.Model):
    nombre = models.CharField(max_length=200)


class Proveedor(models.Model):
    rut = models.CharField(max_length=13, primary_key=True)
    nombre = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Provedores"

class Product(models.Model):
    codigo = models.CharField(max_length=6, primary_key=True)
    descripcion = models.CharField(max_length=50)
    precio = models.IntegerField()
    stock = models.IntegerField()
    proveedor = models.ForeignKey(Proveedor)



class Contacto (models.Model):
    nombre = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)

    def __str__ (self):
        return self.nombre + "  -  " + self.mensaje