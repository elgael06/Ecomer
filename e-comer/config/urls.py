
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('',include('apps.compras.urls')),
    path('usuarios/',include('apps.empleados.urls')),
    path('admin/', admin.site.urls),
]
