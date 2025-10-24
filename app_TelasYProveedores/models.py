from django.db import models

class Proveedor(models.Model):
    nombre = models.CharField(max_length=200, help_text="Nombre del proveedor")
    contacto = models.CharField(max_length=200, help_text="Persona de contacto")
    telefono = models.CharField(max_length=15, help_text="Teléfono de contacto")
    correo = models.EmailField(max_length=100)
    direccion = models.TextField(help_text="Dirección completa")

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Proveedor"
        verbose_name_plural = "Proveedores"

class Productos_telas(models.Model):
    UNIDAD_MEDIDA_CHOICES = [
        ('metro', 'Metro'),
        ('yarda', 'Yarda'),
        ('rollo', 'Rollo'),
        ('pieza', 'Pieza'),
    ]
    
    nombre = models.CharField(max_length=200, help_text="Nombre de la tela")
    categoria = models.CharField(max_length=100, help_text="Categoría de la tela")
    precio = models.DecimalField(max_digits=10, decimal_places=2, help_text="Precio por unidad")
    stock = models.IntegerField(help_text="Cantidad en stock")
    unidad_medida = models.CharField(max_length=10, choices=UNIDAD_MEDIDA_CHOICES)
    id_proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, related_name='telas')
    imagen_tela = models.ImageField(upload_to='img_telas/', blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} - ${self.precio}"

    class Meta:
        verbose_name = "Producto Tela"
        verbose_name_plural = "Productos Telas"