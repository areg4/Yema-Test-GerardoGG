from django.urls import path, include
from .views import solicitarCita

urlpatterns = [
    path('api/solicitarCita/', solicitarCita),
]
