# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Producto(models.Model):
    descripcion = models.CharField(max_length=100)
    folio_familia = models.IntegerField()
    estatus = models.CharField(max_length=1 ,default='V')
    fecha = models.DateField(auto_now_add=True)
    fecha_modificacion = models.DateField(auto_now=True)
    usuario_creo = models.IntegerField()
    usuario_modifico = models.IntegerField()


class Clase_producto(models.Model):
    Descripcion = models.CharField(max_length=100) 
    estatus = models.CharField(max_length=1)
    fecha = models.DateField(auto_now_add=True)
    fecha_modificacion = models.DateField(auto_now=True)
    usuario_creo = models.IntegerField()
    usuario_modifico = models.IntegerField()


class Categoria_producto(models.Model):
    Descripcion = models.CharField(max_length=100) 
    folio_clase = models.IntegerField()
    estatus = models.CharField(max_length=1)
    fecha = models.DateField(auto_now_add=True)
    fecha_modificacion = models.DateField(auto_now=True)
    usuario_creo = models.IntegerField()
    usuario_modifico = models.IntegerField()


class Familia_producto(models.Model):
    Descripcion = models.CharField(max_length=100) 
    folio_categoria = models.IntegerField()
    estatus = models.CharField(max_length=1)
    fecha = models.DateField(auto_now_add=True)
    fecha_modificacion = models.DateField(auto_now=True)
    usuario_creo = models.IntegerField()
    usuario_modifico = models.IntegerField()

class Costo_producto(models.Model):
    folio_producto = models.IntegerField()
    costo = models.FloatField()
    venta = models.FloatField()
    iva = models.FloatField()
    margen = models.FloatField()
    estatus = models.CharField(max_length=1)
    fecha = models.DateField(auto_now_add=True)
    fecha_modificacion = models.DateField(auto_now=True)
    usuario_creo = models.IntegerField()
    usuario_modifico = models.IntegerField()