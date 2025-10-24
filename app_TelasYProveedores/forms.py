from django import forms
from .models import Productos_telas, Proveedor

class ProductoTelaForm(forms.ModelForm):
    class Meta:
        model = Productos_telas
        fields = ['nombre', 'categoria', 'precio', 'stock', 'unidad_medida', 'id_proveedor', 'imagen_tela']

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['nombre', 'contacto', 'telefono', 'correo', 'direccion']