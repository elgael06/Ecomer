# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import JsonResponse
from django.shortcuts import render

from .models import Usuario

# Create your views here.
def index(request):
    return render(request, 'empleados/index.html', {}) 

def  login(request):
     return render(request, 'empleados/login.html', {}) 

def  about(request):
    return render(request, 'empleados/about.html', {}) 


class UsuariosView(APIView):
    def get(self,request):
        users =  Usuario.objects.all()
        data =  list( users.values( 'id', 'nombre' , 'nombre_completo','password', 'estatus', 'usuario_creo', 'usuario_modifico') )
        return JsonResponse({'usuarios':data}, safe=False)

    def put(self,request):
        nom = request.data.get('nombre')
        nom_c = request.data.get('nombre_completo')
        passw = request.data.get('password')
        creo = request.data.get('creo')
        foto = " "
        usr = Usuario(nombre=nom, nombre_completo=nom_c, password=passw, foto=foto,usuario_creo = creo)
        print(usr.nombre)
        usr.save()
        return Response({"Usuario ":usr.id})
    def update(self, instance, validated_data):
        instance.nombre = validated_data.get('nombre',instance.nombre)
        instance.nombre_completo = validated_data.get('nombre_completo',instance.nombre_completo)
        instance.password = validated_data.get('password',instance.password)
        instance.foto = validated_data.get('foto',instance.foto)
        instance.estatus = validated_data.get('estatus',instance.estatus)
        instance.nombre = validated_data.get('usuario_creo',instance.usuario_creo)
        instance.nombre = validated_data.get('usuario_modifico',instance.usuario_modifico)
        instance.save()
        return instance
    
class LoginView():
    def post(self,request):
        return "ok"