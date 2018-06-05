from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.urls import reverse 

# Create your models here.
class Producto(models.Model):
    """ Producto """

    marca=models.CharField(max_length=50)
    nombre=models.CharField(max_length=50)
    foto=models.ImageField(upload_to='foto/')      
    precio=models.IntegerField()    
    caracteristica = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.nombre
    def get_absolute_url(self):
        return reverse('producto-list')

class Venta(models.Model):
    
    producto=models.ForeignKey('producto',on_delete=models.CASCADE)
    descripcion=models.TextField(blank=True)
    cantidad=models.IntegerField('cantidad')        
    precio=models.IntegerField('precio')

    def __str__(self):
        return self.descripcion
    def get_absolute_url(self):
        return reverse('venta-list')