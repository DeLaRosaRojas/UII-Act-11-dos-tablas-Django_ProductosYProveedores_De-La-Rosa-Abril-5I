from django.contrib import admin
from .models import Proveedor, Productos_telas

@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'contacto', 'telefono', 'correo']
    search_fields = ['nombre', 'contacto']

@admin.register(Productos_telas)
class ProductosTelasAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'categoria', 'precio', 'stock', 'unidad_medida', 'id_proveedor']
    list_filter = ['categoria', 'unidad_medida']
    search_fields = ['nombre', 'categoria']