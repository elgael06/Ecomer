# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import JsonResponse

from django.shortcuts import render

from ..Acceso import acceso
from ..manejo_fecha import fecha_hoy
from ..productos.models import Producto ,Codigo_producto,Costo_producto

# Create your views here.
from .models import Proveedor,Orden,Productos_orden

def index(request):
    return acceso(request, 'compras/index.html', {}) 

def proveedores(request):
    return acceso(request, 'compras/proveedores.html', {}) 

# Api
class ProveedorView(APIView):
    def get(self, request):
        id = request.GET.get("id")
        data = None
        if id :
            data = Obtener_proveedor(id)
        else:
          data = Obtener_proveedores()
        return JsonResponse(data)

    def post(self, request):
        id = request.data.get("Id")
        Nombre = request.data.get("Nombre")
        RFC = request.data.get("RFC")
        Direccion = request.data.get("Direccion")
        Email = request.data.get("Email")
        Telefono = request.data.get("Telefono")
        Representante = request.data.get("Representante")
        Descripcion = request.data.get("Descripcion")
        estatus = request.data.get("estatus")
        usuario = request.session["id_usuario"]
        data = ""
        if id == 0:
            guardar_proveedor(Nombre,RFC,Direccion,Email,Telefono,Representante,Descripcion,estatus,usuario)
            data = "Guardado..."
        else:
          actualizar_proveedor(id,Nombre,RFC,Direccion,Email,Telefono,Representante,Descripcion,estatus,usuario)
          data = "Actualizado..."
        return JsonResponse({"respuesta":data})

    def put(self, request):
        id = request.data.get("id")
        data = "Eliminado..."
        Proveedor.filter(id=id).update(
            estatus='C'
        )
        return JsonResponse({"proveedor":data})


class OrdenView(APIView):
    def get(self, request):
        data = None
        id = request.GET.get("id")
        if id == 0 :
              data = Obtener_ordenes()
        else :
            data  = Obtener_orden(id)
        return JsonResponse({"orden":data})

    def post(self, request):
        id = request.data.get("id")
        data = {}
        return JsonResponse({"orden":data})
            
    def put(self, request):
        id = request.data.get("id")
        data = {}
        return JsonResponse({"orden":data})

class Producto_orden(APIView):
    def get(self, request):
        id = request.GET.get("id")
        print(id)
        producto = self.existe(id)
        data = {
            'id':'',
            'descripcion':'',
            'costo':'',
            'venta':'',
            'margen':'',
            'iva':'',
            'cantidad':'',
            'total':'',
        }
        if producto:
            costo_p = self.costo(producto.id)
            if costo_p:
                data = {
                    'id':producto.id,
                    'descripcion':producto.descripcion,
                    'costo':costo_p.costo,
                    'venta':costo_p.venta,
                    'margen':costo_p.margen,
                    'iva':costo_p.iva,
                    'cantidad':1,
                    'total':costo_p.costo,
                }
        return JsonResponse({"producto":data})

    def existe(self,id):
        print("Existe...")
        prod = Producto.objects.filter(id=id,estatus="V")
        if not prod.exists():
            id_alterno = Codigo_producto.objects.filter(Codigo=id)
            if id_alterno.exists():
                 prod = Producto.objects.filter(id=id_alterno[0].id_producto,estatus="V")
            else:
                prod =[None]
        return prod[0]

    def costo(self,id):
        costo = Costo_producto.objects.filter(folio_producto=id, estatus="V")
        if costo.exists():
            return costo[0]
        return None

###Proveedores
def Obtener_proveedor(id):
    data = {'Id':0,
            'Nombre':'',
            'RFC':'',
            'Direccion':'',
            'Email':'',
            'Telefono':'',
            'Representante':'',
            'Descripcion':'',
            'estatus':'',
            }
    prov = Proveedor.objects.filter(id=id)
    if prov.exists():
        data = {
            'Id':prov[0].id,
            'Nombre':prov[0].Nombre,
            'RFC':prov[0].RFC,
            'Direccion':prov[0].Direccion,
            'Email':prov[0].Email,
            'Telefono':prov[0].Telefono,
            'Representante':prov[0].Representante,
            'Descripcion':prov[0].Descripcion,
            'estatus':prov[0].estatus,
        }
    return data

def Obtener_proveedores():
    data =[]
    proveedores = Proveedor.objects.all()
    for prov in proveedores:
            data.append({
                'Id':prov.id,
                'Nombre':prov.Nombre,
                'RFC':prov.RFC,
                'Direccion':prov.Direccion,
                'Email':prov.Email,
                'Telefono':prov.Telefono,
                'Representante':prov.Representante,
                'Descripcion':prov.Descripcion,
                'estatus':prov.estatus,
            })
    return {'Lista':data}

def guardar_proveedor(Nombre,RFC,Direccion,Email,Telefono,Representante,Descripcion,estatus,usuario):
    Proveedor(
        Nombre=Nombre,
        RFC=RFC,
        Direccion=Direccion,
        Email=Email,
        Telefono=Telefono,
        Representante=Representante,
        Descripcion=Descripcion,
        estatus=estatus,
        usuario_creo=usuario,
        usuario_modifico=usuario,
    ).save()

def actualizar_proveedor(id,Nombre,RFC,Direccion,Email,Telefono,Representante,Descripcion,estatus,usuario):
    Proveedor.objects.filter(id=id).update(
        Nombre=Nombre,
        RFC=RFC,
        Direccion=Direccion,
        Email=Email,
        Telefono=Telefono,
        Representante=Representante,
        Descripcion=Descripcion,
        estatus=estatus,
        fecha_modificacion=fecha_hoy(),
        usuario_modifico=usuario,
    )

###Ordenes
def Obtener_orden(id):
    data ={}
    ord = Orden.objects.filter(id=id)
    if ord.exists():
        prov = Proveedor.objects.filter(id= ord[0].Folio_proveedor)
        prod_in = Productos_orden.objects.filter(folio_producto = id)
        productos =[]
        for prod in prod_in:
            p = Producto.objects.filter(id=prod.folio_producto)
            productos.append({
                'id':p[0].id,
                'Descripcion':p[0].descripcion,
                'costo':prod.costo,
                'venta':prod.venta,
                'iva':prod.iva,
                'margen':prod.margen,
                'Cantidad':prod.Cantidad,
                'Total':prod.Total,
            })
        data={
            'id':ord[0].id,
            'Folio_proveedor':ord[0].Folio_proveedor,
            'proveedor':prov[0].Nombre,
            'productos':ord[0].productos,
            'Total':ord[0].Total,
            'Descripcion':ord[0].Descripcion,
            'estatus':ord[0].estatus,
            'fecha':ord[0].fecha,
            'fecha_modificacion':ord[0].fecha_modificacion,
            'usuario_creo':ord[0].usuario_creo,
            'usuario_modifico':ord[0].usuario_modifico,
            'Productos_lista':productos
        }
    return data

def Obtener_ordenes():
    data =[]
    orden = Orden.objects.all()
    for ord in orden:
        data.append({
            'id':ord.id,
            'Folio_proveedor':ord.Folio_proveedor,
            'proveedor':ord.proveedor,
            'productos':ord.productos,
            'Total':ord.Total,
            'Descripcion':ord.Descripcion,
            'estatus':ord.estatus,
            'fecha':ord.fecha,
            'fecha_modificacion':ord.fecha_modificacion,
            'usuario_creo':ord.usuario_creo,
            'usuario_modifico':ord.usuario_modifico,
        })
    return {'lista':data}

def guardar_ordenes(Folio_proveedor,productos,Total,Descripcion,usuario):
     Orden(
         Folio_proveedor=Folio_proveedor,
         productos=productos,
         Total=Total,
         Descripcion=Descripcion,
         estatus='V',
         usuario_creo=usuario,
         usuario_modifico=usuario,
    ).save()

def actualizar_ordenes(id,productos,Total,estatus,usuario):
    Orden.objects.filter(id=id).update(
        productos=productos,
         Total=Total,
         Descripcion=Descripcion,
         estatus=estatus,
         usuario_modifico=usuario,
    )

def finalizar_ordenes(id,productos,Total,estatus,usuario,lista_productos):
     Orden.objects.filter(id=id).update(
        productos=productos,
         Total=Total,
         Descripcion=Descripcion,
         estatus='F',
         usuario_modifico=usuario,
    )
    #for producto in lista_productos:
     #   Producto.objects.filter(id=producto['id']).update(
      #      costo=producto['costo'],
       # )

###Productos Orden
def Obtener_productos_orden(id):
    pass

def Obtener_productos_orden():
    pass

def guardar_productos_orden():
    pass

def actualizar_productos_orden():
    pass

