from django.contrib import admin

from Globemaster_Aplicación.models import *


# Register your models here.
admin.site.register(Administrador)
admin.site.register(Inventario)
admin.site.register(Cliente)
admin.site.register(Producto)
admin.site.register(Pedidos)
admin.site.register(Ventas)
admin.site.register(Comprobante_ventas)
admin.site.register(Gastos)
admin.site.register(Estado_de_Resultados)

