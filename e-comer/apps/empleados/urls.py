
from django.urls import path

from . import views
from .views import UsuariosView

urlpatterns =[
    path('',views.index,name='Usuarios'),    
    path('login',views.login,name='Login'),  
    path('about',views.about,name='about'),
    path('api/',UsuariosView.as_view()),
]