from django.contrib import admin

# Register your models here.
from .models import Producto, Cliente
admin.site.register(Producto)
admin.site.register(Cliente)