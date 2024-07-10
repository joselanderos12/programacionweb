from django.urls import path  
from . import views
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('index', views.index, name='index'),
    path('index2', views.index2, name='index2'),
    path('contacto', views.contacto, name='contacto'),
    path('clientesAdd', views.clientesAdd, name='clientesAdd'),
    path('productos', views.productos, name='productos'),
    path('producto_del/<str:pk>', views.producto_del, name='producto_del'),
    path('carrito', views.carrito, name='carrito'),
    path('agregar_producto', views.agregar_producto, name='agregar_producto'),
    path('crud', views.crud, name='crud'),
    path('clientes_del/<str:pk>', views.clientes_del, name='clientes_del'),
    path('index_cliente', views.index, name='index_cliente'),
    path('clientesUpdate', views.clientesUpdate, name='clientesUpdate'),
    path('clientes_finEdit/<str:pk>', views.clientes_finEdit, name='clientes_finEdit'),    
    path('clientes_Add', views.clientes_Add, name='clientes_Add'), 

]