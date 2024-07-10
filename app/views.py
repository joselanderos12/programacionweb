from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
# Create your views here.
from .models import  Producto
from .models import Cliente

def contacto(request):
    return render(request, 'app/contacto.html')

def crud(request):
    clientes= Cliente.objects.all()
    context= {'clientes':clientes}
    return render(request, 'app/clientes_crud.html', context)

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




def clientes_del(request, pk):
    context = {}
    try:
        cliente = Cliente.objects.get(rut=pk)
        cliente.delete() 

        mensaje = "Datos eliminados"
        clientes = Cliente.objects.all()
        context = {'clientes': clientes, 'mensaje': mensaje}
    except Cliente.DoesNotExist:
        mensaje = "El cliente no existe"
        clientes = Cliente.objects.all()
        context = {'clientes': clientes, 'mensaje': mensaje}
    except Exception as e:
        mensaje = f"Error: {str(e)}"
        clientes = Cliente.objects.all()
        context = {'clientes': clientes, 'mensaje': mensaje}

    return render(request, 'app/clientes_crud.html', context)



def clientes_finEdit(request, pk):
    cliente = get_object_or_404(Cliente, rut=pk)
    context = {'cliente': cliente}
    return render(request, 'app/clientes_up.html', context)




def clientesUpdate(request, pk):
    cliente = get_object_or_404(Cliente, pk=rut)
    if request.method == "POST":
        rut = request.POST.get("rut")
        

        nombre = request.POST["nombre"]
        apellido = request.POST["apellido"]
        fecha_nacimiento = request.POST["fecha_nacimiento"]
        email = request.POST["email"]
        password = request.POST["password"]

        cliente.nombre = nombre
        cliente.apellido = apellido
        cliente.fecha_nacimiento = fecha_nacimiento
        cliente.email = email
        cliente.password = password

        cliente.save()
        context = {'mensaje': "Datos actualizados", 'cliente': cliente}
        return render(request, 'app/index.html', context)
    else:
        clientes = Cliente.objects.all()
        context = {'clientes': clientes}
        return render(request, 'app/clientes_up.html', context)
    



def clientes_Add(request):
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

        return redirect('crud')  

    return render(request, 'app/clientes_add.html')