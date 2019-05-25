# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Cliente(models.Model):
    Nombre =  models.CharField(max_length=200)
    RFC =  models.CharField(max_length=20,default='X0X0X0X0X0X0')
    Direccion =  models.CharField(max_length=200,default='Conosido.')
    Email =  models.CharField(max_length=50,default='NA')
    Telefono =  models.CharField(max_length=10)
    Representante =  models.CharField(max_length=100)
    Descripcion =  models.CharField(max_length=100,default="NA")
    estatus = models.CharField(max_length=1,default='V')
    fecha = models.DateField(auto_now_add=True)
    fecha_modificacion = models.DateField(auto_now=True)
    usuario_creo = models.IntegerField()
    usuario_modifico = models.IntegerField() 


class Pedido(models.Model):
    usuario_creo = models.IntegerField()
    usuario_modifico = models.IntegerField()
    estatus = models.CharField(max_length=1)
    fecha = models.DateField(auto_now_add=True)
    fecha_modificacion = models.DateField(auto_now=True)


class Producto_pedido(models.Model):
    id_pedido  = models.IntegerField()
    id_producto  = models.IntegerField()
    cantidad =  models.FloatField()
