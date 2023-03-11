from django.http import HttpResponse
from django.template import Template,Context
# from Little.models import Usuarios
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout




#region Home

#FUNCION PARA ENTRAR A LA PAGINA PRINCIPAL

def home(request):
    if not request.user.is_authenticated:
     return redirect('/Usuarios/login')
     
    archivocuenta = open("Little/Templates/Home/principal.html")
    lea = Template(archivocuenta.read())
    archivocuenta.close()
    parametros = Context()
    entrarhome = lea.render(parametros)
    return HttpResponse(entrarhome)
#endregion




#region Editarperfil



    
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

 

#FUNCION PARA REGISTRO
def insertarusuario(request):
    if request.method == "POST":
     if request.POST.get('username') and request.POST.get('email') and request.POST.get('password'):

        usuario = User.objects.create_user(username=request.POST.get('username'),email=request.POST.get('email'),password=request.POST.get('password'))
  
        usuario.save()
        return redirect('/Usuarios/login')
    else:
        return render(request,'Usuarios/registro.html')
        ...



#FUNCION PARA VALIDACION LOGIN
def loginusuario(request):
    if request.method == "POST":
        if request.POST.get('username') and request.POST.get('password'):
           user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))

        if user is not None:
             login(request,user)
             return redirect('/Home/principal')
        else:
            mensaje = "Usuario o contraseña estan mal"
            return render(request,'Usuarios/login.html',{'mensaje':mensaje})
    
    else:
        return render(request,'Usuarios/login.html')

 
#FUNCION PARA CERRAR SESION
def logoutusuario(request):
    logout(request)
    return redirect('/Usuarios/crearcuenta')




#endregion




 







