from django.urls import path
from .views import limpiar_carro, restar_producto, agregar_producto, eliminar_producto, limpiar_carro

app_name="carro"
urlpatterns = [
    path('agregar/<producto_id>', agregar_producto, name = "agregar"),
    path('eliminar/<producto_id>', eliminar_producto, name = "eliminar"),
    path('restar/<producto_id>', restar_producto, name = "restar"),
    path('limpiar/', limpiar_carro, name = "limpiar"),

]