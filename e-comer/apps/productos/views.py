# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import JsonResponse

from django.shortcuts import render

from .models import Producto, Costo_producto, Clase_producto, Categoria_producto, Familia_producto
from ..Acceso import acceso
from ..manejo_fecha import fecha_hoy

# Create your views here.
def index(request):
    return acceso(request, 'productos/index.html', {}) 

#api

##clases
class ProductosViwe(APIView):
    def get(self, request):

        productos = Producto.objects.all()

        data = list( productos.values('id','descripcion','estatus', 'folio_familia','fecha','fecha_modificacion','usuario_creo','usuario_modifico'))
        
        return JsonResponse({"productos":data})

    def post(self,request):
        descripcion = request.data.get('descripcion')
        folio_familia = request.data.get('folio_familia')
        costo = request.data.get('costo')
        venta = request.data.get('venta')
        margen = request.data.get('margen')
        iva = request.data.get('iva')

        prod = Producto(
            descripcion = descripcion,
            folio_familia = folio_familia,
            fecha = fecha_hoy(),
            fecha_modificacion = fecha_hoy(),
            usuario_creo = request.session["id_usuario"],
            usuario_modifico = request.session["id_usuario"],
        )
        prod.save()
        
        agregar_costo(prod.id,costo,venta,margen,iva,request.session["id_usuario"])

        return JsonResponse({"producto":'Guardado...','id':prod.id})

    def put(self,request):
        id = request.data.get('id')
        descripcion = request.data.get('descripcion')
        folio_familia = request.data.get('folio_familia')
        cambio_costo = request.data.get('cambio_costo')
        costo = request.data.get('costo')
        venta = request.data.get('venta')
        margen = request.data.get('margen')
        iva = request.data.get('iva')

        Producto.filter(id = id).update(
            descripcion = descripcion,
            folio_familia = folio_familia,
            fecha_modificacion = fecha_hoy(),
            usuario_modifico = request.session["id_usuario"],
            )
        if cambio_costo==0:
            agregar_costo(id,costo,venta,margen,iva,request.session["id_usuario"])

        return JsonResponse({"producto":'Actualizado...'})
    
    def patch(self,request):
        id = request.data.get('id')
        Producto.filter(id = id).update(
            estatus = "C",
            fecha_modificacion = fecha_hoy(),
            usuario_modifico = request.session["id_usuario"],
            )
        return JsonResponse({"producto":'Eliminado...'})
     

class ClasesView(APIView):
    def get(self,request):
        return JsonResponse({"Clases":'data'})

    def post(self,request):
        return JsonResponse({"Clases":'Guardado...'})

    def put(self,request):
        return JsonResponse({"Clases":'Actualizado...'})

    def patch(self,request):
        return JsonResponse({"Clases":'Borrado...'})


class CategoriasView(APIView):
    def get(self,request):
        return JsonResponse({"Categorias":'data'})

    def post(self,request):
        return JsonResponse({"Categorias":'Guardado...'})

    def put(self,request):
        return JsonResponse({"Categorias":'Actualizado...'})

    def patch(self,request):
        return JsonResponse({"Categorias":'Borrado...'})


class FamiliasView(APIView):
    def get(self,request):
        return JsonResponse({"Familias":'data'})

    def post(self,request):
        return JsonResponse({"Familias":'Guardado...'})

    def put(self,request):
        return JsonResponse({"Familias":'Actualizado...'})

    def patch(self,request):
        return JsonResponse({"Familias":'Borrado...'})



##Metodos
def agregar_costo(id,costo,venta,margen,iva,id_usuario):
    Costo_producto.filter(folio_producto = id).update(estatus = "C")

    costo_prod = Costo_producto(
        folio_producto = id,
        costo = costo,
        venta = venta,
        margen = margen,
        iva = iva,
        fecha = fecha_hoy(),
        fecha_modificacion = fecha_hoy(),
        usuario_creo = id_usuario,
        usuario_modifico = id_usuario,
    )
    costo_prod.save()