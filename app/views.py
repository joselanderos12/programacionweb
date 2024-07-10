from django.shortcuts import render, redirect
from django.contrib import messages
# Create your views here.
from .models import  Producto
from .models import Cliente

def contacto(request):
    return render(request, 'app/contacto.html')



def index(request):
    context = {}
    return render(request, 'app/index.html',context)

def index2(request):
    context = {}
    return render(request, 'app/index2.html',context)


def carrito(request):
    productos= Producto.objects.all()
    context= {'productos':productos}
    return render(request, 'app/carrito.html', context)


def agregar_producto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        precio = request.POST.get('precio')
        imagen_url = request.POST.get('imagen_url')
        
        producto = Producto(nombre=nombre, descripcion=descripcion, precio=precio, imagen_url=imagen_url)
        producto.save()
        
        return redirect('productos')
    return render(request, 'app/productos.html', {'mensaje': 'Producto agregado correctamente.'})       
        



def producto_del(request, pk):
    context = {}
    try:
        producto = Producto.objects.get(id=pk)
        producto.delete()

        mensaje = "Producto eliminado correctamente"
        productos = Producto.objects.all()
        context = {'productos': productos, 'mensaje': mensaje}
    except Producto.DoesNotExist:
        mensaje = "El producto no existe"
        productos = Producto.objects.all()
        context = {'productos': productos, 'mensaje': mensaje}
    except Exception as e:
        mensaje = f"Error al eliminar el producto: {str(e)}"
        productos = Producto.objects.all()
        context = {'productos': productos, 'mensaje': mensaje}

    return render(request, 'app/carrito.html', context)
    

def productos(request):
    productos = Producto.objects.all()
    return render(request, 'app/productos.html', {'productos': productos})




def clientesAdd(request):
    if request.method == 'POST':
        rut = request.POST.get('rut')
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        fecha_nacimiento = request.POST.get('fecha_nacimiento')
        email = request.POST.get('email')
        password = request.POST.get('password')

        cliente = Cliente(
            rut=rut,
            nombre=nombre,
            apellido=apellido,
            fecha_nacimiento=fecha_nacimiento,
            email=email,
            password=password
        )
        cliente.save()  

        return redirect('index2')  

    return render(request, 'app/registro.html')




