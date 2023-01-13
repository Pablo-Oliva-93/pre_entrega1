from django.shortcuts import render
from django.http import HttpResponse
from lista_usuarios.models import Usuario
from lista_usuarios.form import Usuarioformulario
# Create your views here.
def lista_de_usuarios(request):
    var_usuario = Usuario.objects.all()
    context = {
        "usuarios":var_usuario,
    }
    return render(request, "tem_usuarios/lista_usuarios.html", context=context)
    
def cargar_los_usuarios (request):
    if request.method == "GET":
        context = {
            "formulario" : Usuarioformulario()
        }
        return render(request, "tem_usuarios/crear_usuarios.html", context=context)
    elif request.method == "POST": 
        Usuario.objects.create(usuario = request.POST["usuario"], precio = request.POST["nombre"])
    return HttpResponse("Usuario creado")