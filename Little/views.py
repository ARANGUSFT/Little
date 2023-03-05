from django.http import HttpResponse
from django.template import Template,Context
from Little.models import Usuarios
from django.shortcuts import render,redirect
# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib import messages
from django.contrib.auth import authenticate, login




#region Home

#FUNCION PARA ENTRAR A LA PAGINA PRINCIPAL
def home(request):
    archivocuenta = open("Little/Templates/Home/principal.html")
    lea = Template(archivocuenta.read())
    archivocuenta.close()
    parametros = Context()
    entrarhome = lea.render(parametros)
    return HttpResponse(entrarhome)
#endregion







#region Usuarios

#FUNCION PARA CARGAR ELEGIR
def crearcuenta(request):
    archivocuenta = open("Little/Templates/Usuarios/elegir.html")
    lea = Template(archivocuenta.read())
    archivocuenta.close()
    parametros = Context()
    paginacrearcuenta = lea.render(parametros)
    return HttpResponse(paginacrearcuenta)


#FUNCION PARA CARGAR EL LOGIN

# def entrar(request):
#     archivocuenta = open("Little/Templates/Usuarios/login.html")
#     lea = Template(archivocuenta.read())
#     archivocuenta.close()
#     parametros = Context()
#     entrarcuenta = lea.render(parametros)
#     return HttpResponse(entrarcuenta)
 


def entrar(request):
    # Proveedor = Proveedor()
    username = request.POST.get('email')
    password = request.POST.get('contrasena')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        return redirect('/Home/principal')
        ...
    else:
        # Return an 'invalid login' error message.
        return render(request,'Usuarios/registro.html')
        ...



#FUNCION PARA CARGAR EL REGISTRO
def registro(request):
    if request.method == "POST":
        if request.POST.get('apodo') and request.POST.get('email') and request.POST.get('contrasena1'):
         #and request.POST.get('contrasena2')# 
            empleado = Usuarios()
            empleado.Apodo = request.POST.get('apodo')
            empleado.Email = request.POST.get('email')
            empleado.Contrasena = request.POST.get('contrasena1')
            empleado.save()
            # messages.success(request, "La cuenta se creo exitosamente")
            return redirect('/Usuarios/login') 
    else:
        return render(request,'Usuarios/registro.html')

 
#endregion




 







