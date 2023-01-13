from django.shortcuts import render
from django.http import HttpResponse
from lista_producto.models import Producto
from lista_producto.form import Produtoformulario
# Create your views here.

def lista_de_productos(request):
    var_productos = Producto.objects.all()
    context = {
        "productos":var_productos,
    }
    return render(request, "tem_productos/lista_productos.html", context=context)
    
#def cargar_los_productos (request):
 #   Producto.objects.create(name = "papas", precio = 200, stock= True)
  #  return HttpResponse("Producto creado")

def cargar_los_productos (request):
    if request.method == "GET":
        context = {
            "formulario" : Produtoformulario()
        }
        return render(request, "tem_productos/crear_productos.html", context=context)
    elif request.method == "POST": 
        Producto.objects.create(name = request.POST["name"], precio = request.POST["precio"])
    return HttpResponse("Producto creado")
