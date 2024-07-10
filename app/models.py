from django.db import models

# Create your models here.


class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen_url = models.URLField(default='https://ejemplo.com/imagen-default.jpg')  
    
    def __str__(self):
        return self.nombre



class Cliente(models.Model):
    rut = models.CharField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField(blank=False, null=False)
    email = models.EmailField(unique=True, max_length=100, blank=True, null=True)
    password = models.CharField(max_length=20)  

    def __str__(self):
        return f"{self.nombre} {self.apellido}"