from django.urls import path
from . import views

app_name = 'app_TelasYProveedores'

urlpatterns = [
    # URLs para Telas
    path('', views.listar_telas, name='listar_telas'),
    path('tela/<int:tela_id>/', views.detalle_tela, name='detalle_tela'),
    path('crear-tela/', views.crear_tela, name='crear_tela'),
    path('editar-tela/<int:tela_id>/', views.editar_tela, name='editar_tela'),
    path('borrar-tela/<int:tela_id>/', views.borrar_tela, name='borrar_tela'),
    
    # URLs para Proveedores
    path('proveedores/', views.listar_proveedores, name='listar_proveedores'),
    path('proveedor/<int:proveedor_id>/', views.detalle_proveedor, name='detalle_proveedor'),
    path('crear-proveedor/', views.crear_proveedor, name='crear_proveedor'),
]