# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.response import Response
from rest_framework.views import APIView

from django.shortcuts import render

from .models import Producto

# Create your views here.
def index(request):
    return render(request, 'productos/index.html', {}) 


class ProductosViwe(APIView):
     def get(self, request):
         productos = Producto.objects.all()
         return Response({"productos":productos})