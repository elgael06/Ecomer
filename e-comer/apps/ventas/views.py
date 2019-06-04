# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import JsonResponse
import json

from django.shortcuts import render

from ..Acceso import acceso
from ..manejo_fecha import fecha_hoy
from .models import Asignacion_caja

# Create your views here.


def index(request):
    return acceso(request, 'ventas/index.html', {})


# api Asignacion
class AsignacionView(APIView):
    def get(self, request):
        data = {}

        return JsonResponse(data)
