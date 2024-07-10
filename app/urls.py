from django.urls import path  
from . import views



urlpatterns = [
    path('index', views.index, name='index'),
    path('index2', views.index2, name='index2'),
    path('contacto', views.contacto, name='contacto'),
    path('clientesAdd', views.clientesAdd, name='clientesAdd'),
    path('productos', views.productos, name='productos'),
    path('producto_del/<str:pk>', views.producto_del, name='producto_del'),
    path('carrito', views.carrito, name='carrito'),
    path('agregar_producto', views.agregar_producto, name='agregar_producto'),
    
    


]