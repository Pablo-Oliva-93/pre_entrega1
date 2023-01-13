from django.shortcuts import render
from django.http import HttpResponse
from lista_vendedores.models import Vendedor
from lista_vendedores.form import Vendedorformulario
# Create your views here.
def lista_de_vendedores(request):
    var_vendedores = Vendedor.objects.all()
    context = {
        "vendedores":var_vendedores,
    }
    return render(request, "tem_vendedores/lista_vendedores.html", context=context)
    
def cargar_los_vendedores (request):
    if request.method == "GET":
        context = {
            "formulario" : Vendedorformulario()
        }
        return render(request, "tem_vendedores/crear_vendedores.html", context=context)
    elif request.method == "POST": 
        Vendedor.objects.create(nombre = request.POST["nombre"], nivel = request.POST["nivel"])
    return HttpResponse("Vendedor creado")