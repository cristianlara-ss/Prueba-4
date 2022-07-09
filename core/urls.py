from django.urls import path, include
from .views import index, admindj, contactanos, registro, agregar_producto, listar_productos, modificar_producto, eliminar_producto, registro1, carrito, ProductoViewset, MarcaViewset, SuscripcionViewset, agregar_membresia, listar_membresia, eliminar_membresia, agregar_envio, listar_envio, listar_envio_usuario, modificar_envio
from rest_framework import routers
from .viewsLogin import login

router = routers.DefaultRouter()
router.register('producto', ProductoViewset)
router.register('marca', MarcaViewset)
router.register('suscripciones', SuscripcionViewset)

#localhost:7000
urlpatterns = [
    path('', index, name="index"),
    path('contactanos/', contactanos, name="contactanos"),
    path('admindj/', admindj, name="admindj"),
    path('registro/', registro, name="registro"),
    path('agregar-sub/', agregar_membresia, name="agregar_membresia"),
    path('listar-sub/', listar_membresia, name="listar_membresia"),
    path('eliminar-sub/<id>/', eliminar_membresia, name="eliminar_membresia"),
    path('agregar-producto/', agregar_producto, name="agregar_producto"),
    path('listar-productos/', listar_productos, name="listar_productos"),
    path('modificar-producto/<id>/', modificar_producto, name="modificar_producto"),
    path('eliminar-producto/<id>/', eliminar_producto, name="eliminar_producto"),
    path('registro-per/', registro1, name="registro1"),
    path('carrito/', carrito, name="carrito"),
    path('api/', include(router.urls)),
    path('login', login, name="login"),
    path('agregar-envio/', agregar_envio, name="agregar_envio"),
    path('listar-envio/', listar_envio, name="listar_envio"),
    path('historial/', listar_envio_usuario, name="listar_envio_usuario"),
    path('modificar-envio/<id>/',modificar_envio,name="modificar_envio"),
]