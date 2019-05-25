
from django.urls import path

from .views import index,proveedores,ProveedorView

urlpatterns =[
    path('',index,name='compras'),
    path('proveedores',proveedores,name='proveedores'),
    path('proveedores/api',ProveedorView.as_view()),
]