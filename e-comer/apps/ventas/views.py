# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import JsonResponse
import json

from django.shortcuts import render

from ..Acceso import acceso
from ..manejo_fecha import fecha_hoy
from ..inventario.models import Inventario_producto
from .models import Asignacion_caja, Ticket, Cliente, Producto_ticket

# Create your views here.


def index(request):
    return acceso(request, 'ventas/index.html', {})


# api Asignacion
class AsignacionView(APIView):
    def get(self, request):
        data = {}

        return JsonResponse(data)


class TicketView(APIView):
    def get(self, request):
        tiket = self.verificarTicket(id_usuario=request.session["id_usuario"])
        client = Cliente.objects.filter(id=tiket.folio_cliente)
        data = {
            'ticket': tiket.id,
            'id_cliente': tiket.folio_cliente,
            'cliente': client[0].Nombre,
            'cantidad': 0,
            'total': 0,
            'tipoPago': TiposDePagos(t=tiket.tipo_pago),
            'totalPaga': 0,
            'descuento': 0,
            'fecha': tiket.fecha
        }
        return JsonResponse(data)

    def post(self, request):
        data = {"respuesta": False}
        ticket = Ticket.objects.filter(
            id=request.data.get('ticket')
        ).update(
            productos=request.data.get('cantidad'),
            total=request.data.get('totalPaga'),
            descuento=request.data.get('descuento'),
            estatus="P",
            fecha=fecha_hoy(),
            tipo_pago=AbreviaturaPago(request.data.get('tipoPago'))
        )
        productos = json.loads(json.dumps(request.data.get("productos")))
        for prod in productos:
            Producto_ticket(
                folio_ticket=request.data.get('ticket'),
                folio_producto=prod["folio"],
                camtidad=prod["cantidad"],
                total=prod["total"],
                descuento=prod["descuento"]
            ).save()
            inv = Inventario_producto.objects.filter(
                folio_producto=prod["folio"]
            )
            inv.update(
                cantidad=(inv[0].cantidad - prod["cantidad"]),
                fecha_modificacion=fecha_hoy(),
            )
        data["respuesta"] = True
        return JsonResponse(data)

    def verificarTicket(self, id_usuario):
        asignacion = self.verificarAsignacion(id_usuario=id_usuario)

        t = Ticket.objects.filter(
            folio_asignacion=asignacion.id, estatus="V")
        if (t.exists()):
            t.update(fecha=fecha_hoy())
            return t[0]
        else:
            t = Ticket(
                folio_asignacion=asignacion.id,
                productos=0,
                total=0,
                descuento=0,
                folio_cliente=1,
                estatus="V",
                fecha=fecha_hoy(),
                tipo_pago="EF"
            )
            t.save()
            return t

    def verificarAsignacion(self, id_usuario):
        asignacion = Asignacion_caja.objects.filter(
            id_usuario=id_usuario, fecha=fecha_hoy())
        if(asignacion.exists()):
            return asignacion[0]
        else:
            asignacion = Asignacion_caja(
                id_usuario=id_usuario,
                fondo_caja=0,
                usuario_creo=id_usuario,
                usuario_modifico=id_usuario,
                estatus="V",
                fecha=fecha_hoy(),
                fecha_modificacion=fecha_hoy())
            asignacion.save()
            return asignacion


def TiposDePagos(t):
    if(t == "EF"):
        return "Efectivo"
    elif(t == "TA"):
        return "Tarjeta"
    else:
        return "Credito"


def AbreviaturaPago(t):
    if(t == "Efectivo"):
        return "EF"
    elif(t == "Tarjeta"):
        return "TA"
    else:
        return "CR"
