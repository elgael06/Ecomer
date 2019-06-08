
from django.urls import path

from .views import index, AsignacionView, TicketView

urlpatterns = [
    path('', index, name='index'),
    path('Asignacion/api', AsignacionView.as_view()),
    path('Ticket/api', TicketView.as_view()),
]
