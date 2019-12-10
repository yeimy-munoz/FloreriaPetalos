from django.shortcuts import render
from .models import Flores #importar el modelo
# para lograr el ingreso de usuarios regsitrados al sistema, se debe
# incorporar el modelo de usuarios registrados de Django
from django.contrib.auth.models import User
# importar el sistema de autentificacion
from django.contrib.auth import authenticate,logout,login as auth_login
# importar los "decorators" que permiten evitar el ingreso a una pagina
# sin estar logeado
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
# Create your views here. crear los controladores
# para las paginas web
@login_required(login_url='/login/')
def vacio_carrito(request):
    request.session["carro"]=""
    lista=request.session.get("carro","")
    return render(request,"core/carrito.html",{'lista':lista})

@login_required(login_url='/login/')
def home(request):
    return render(request,'core/home.html')
    # retorna la pagina renderizada

@login_required(login_url='/login/')
def cerrar_sesion(request):
    logout(request)
    return HttpResponse("<script>alert('cerro sesion');window.location.href='/';</script>")

@login_required(login_url='/login/')
def agregar_carro(request, id):
    flores=Flores.objects.filter(name__contains=id)
    valor=Flores.precio   
    sesion=request.session.get("carro","")

    arr=sesion.split(";")

    arr2=''
    sw=0
    cant=1
    for f in arr:
        pel=f.split(":")        
        if pel[0]==id:
            cant=int(pel[1])+1
            sw=1
            arr2=arr2+str(pel[0])+":"+str(cant)+":"+str(valor)+";"            
        elif not pel[0]=="":
            cant=pel[1]
            arr2=arr2+str(pel[0])+":"+str(cant)+":"+str(valor)+";"
        

    if sw==0:
        arr2=arr2+str(id)+":"+str(1)+":"+str(valor)+";"

   
    request.session["carro"]=arr2

    flor=Flores.objects.all()
 
    msg='Se agrego'
    return render(request,'core/galeria.html',{'listaFlor':flor,'msg':msg})


@login_required(login_url='/login/')
def carrito(request):
    lista=request.session.get("carro","")
    arr=lista.split(";")
    return render(request,"core/carrito.html",{'lista':arr})

def login(request):
    return render(request,'core/login.html')

def login_iniciar(request):
    if request.POST:
        u=request.POST.get("txtUsuario")
        p=request.POST.get("txtPass")
        usu=authenticate(request,username=u,password=p)
        if usu is not None and usu.is_active:
            if usu.is_staff:
                auth_login(request, usu)
                arreglo={'nombre':u,'contraseña':p, 'tipo':'administrador'}
                return render(request,'core/home.html',arreglo)
            else:
                arreglo={'nombre':u,'contraseña':p, 'tipo':'cliente'}
                return render(request,'core/home2.html,arreglo')
        variable={
            'msg':'no existe nada'
        }

    return render(request,'core/login.html')
    
@login_required(login_url='/login/')
def eliminar_flor(request,id):
    mensaje=''    
    flores=Flores.objects.get(name=id)
    try:
        flores.delete()
        mensaje='elimino Flor'
    except:
        mensaje='no pudo elimiar Flor'
    
    flor=Flores.objects.all()
    return render(request,'core/galeria.html',{'listaFlor':flor,'msg':mensaje})

@login_required(login_url='/login/')
def galeria(request):
    flor=Flores.objects.all()# select * from flores funciona c:
    return render(request, 'core/galeria.html',{'listaFlor':flor})

@login_required(login_url='/login/')
def formulario(request):
  
    if request.POST:
        name=request.POST.get("txtNombre")
        precio=request.POST.get("txtPrecio")
        stock=request.POST.get("txtStock")
        descripcion=request.POST.get("txtDescripcion")
        estado=request.POST.get("txtEstado")
        #recuperar la imagen desde el formulario
        imagen=request.FILES.get("txtImagen")
        #crear una instancia de Flores (modelo)
        flores=Flores(
            name=name,
            stock=stock,
            precio=precio,
            descripcion=descripcion,
            estado=estado,
            fotografia=imagen
        )
        flores.save() #graba el objeto e bdd
        return render(request,'core/formulario.html',{'msg':'grabo','sw':True})
    return render(request,'core/formulario.html')#pasan los datos a la web


