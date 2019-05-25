
from django.urls import path

from .views import index,proveedores,ProveedorView,Producto_orden

urlpatterns =[
    path('',index,name='compras'),
    path('proveedores',proveedores,name='proveedores'),
    path('proveedores/api',ProveedorView.as_view()),
    path('productos/api',Producto_orden.as_view()),
]