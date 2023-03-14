from django.db import models

# Create your models here.
class Cliente(models.Model):
  nombre = models.CharField(max_length=30,verbose_name='Nombre')
  direccion = models.CharField(max_length=50,verbose_name='Dirección')
  email = models.EmailField(max_length=50,verbose_name='Email')
  telefono = models.CharField(max_length=50,verbose_name='Telefono')
  
  def __str__(self):
    return self.nombre