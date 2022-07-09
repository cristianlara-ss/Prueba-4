from django.contrib import admin
from .models import Marca, Producto, Contactanos, Suscripcion, Membresia, Envio, Seguimiento
# Register your models here.
admin.site.register(Marca)
admin.site.register(Producto)
admin.site.register(Contactanos)
admin.site.register(Suscripcion)
admin.site.register(Membresia)
admin.site.register(Envio)
admin.site.register(Seguimiento)