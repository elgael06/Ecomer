
from django.urls import path

from .views import index, AsignacionView

urlpatterns =[  
    path('',index,name='index'), 
    path('Asugnacion/api',AsignacionView.as_view()),
]