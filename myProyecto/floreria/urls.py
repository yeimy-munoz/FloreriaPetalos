#tendra todas las url del sitio web
from django.contrib import admin
from django.urls import path,include
#from django.conf import settings #importar el archivo de configuracion
#from django.conf.urls.static import static #importa el uso de ubicaciones estaticas
from .views import home,galeria,eliminar_flor,formulario,login,cerrar_sesion,login_iniciar,agregar_carro,carrito,vacio_carrito

urlpatterns = [
    path('',home,name='HOME'),
    path('galeria/',galeria,name='GALE'),
    path('formulario/',formulario,name='FORMU'),
    path('eliminar_flor/<id>/',eliminar_flor,name='ELIMINAR_FLOR'),
    path('login/',login,name='LOGIN'),
    path('cerrar_sesion/',cerrar_sesion,name='CERRAR_SESION'),
    path('login_iniciar/',login_iniciar,name='LOGIN_INICIAR'),
    path('agregar_carro/<id>/',agregar_carro,name='AGREGAR_CARRO'),
    path('carrito/',carrito,name='CARRITO'),
    path('vaciar_carrito/',vacio_carrito,name='VACIARCARRITO'),
]