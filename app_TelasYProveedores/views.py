from django.shortcuts import render, get_object_or_404, redirect
from .models import Productos_telas, Proveedor
from .forms import ProductoTelaForm, ProveedorForm

def listar_telas(request):
    telas = Productos_telas.objects.all()
    return render(request, 'listar_telas.html', {'telas': telas})

def detalle_tela(request, tela_id):
    tela = get_object_or_404(Productos_telas, id=tela_id)
    return render(request, 'detalle_tela.html', {'tela': tela})

def crear_tela(request):
    if request.method == 'POST':
        form = ProductoTelaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('app_TelasYProveedores:listar_telas')
    else:
        form = ProductoTelaForm()
    return render(request, 'formulario_tela.html', {'form': form, 'titulo': 'Crear Producto Tela'})

def editar_tela(request, tela_id):
    tela = get_object_or_404(Productos_telas, id=tela_id)
    if request.method == 'POST':
        form = ProductoTelaForm(request.POST, request.FILES, instance=tela)
        if form.is_valid():
            form.save()
            return redirect('app_TelasYProveedores:detalle_tela', tela_id=tela.id)
    else:
        form = ProductoTelaForm(instance=tela)
    return render(request, 'formulario_tela.html', {'form': form, 'titulo': 'Editar Producto Tela'})

def borrar_tela(request, tela_id):
    tela = get_object_or_404(Productos_telas, id=tela_id)
    if request.method == 'POST':
        tela.delete()
        return redirect('app_TelasYProveedores:listar_telas')
    return render(request, 'confirmar_borrar.html', {'tela': tela})

# Vistas para Proveedores
def listar_proveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'listar_proveedores.html', {'proveedores': proveedores})

def detalle_proveedor(request, proveedor_id):
    proveedor = get_object_or_404(Proveedor, id=proveedor_id)
    telas = proveedor.telas.all()
    return render(request, 'detalle_proveedor.html', {'proveedor': proveedor, 'telas': telas})

def crear_proveedor(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('app_TelasYProveedores:listar_proveedores')
    else:
        form = ProveedorForm()
    return render(request, 'formulario_proveedor.html', {'form': form, 'titulo': 'Crear Proveedor'})