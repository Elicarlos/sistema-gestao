from django.urls import path
from . import views

urlpatterns = [
    path('registrar-refeicao/', views.registrar_refeicao, name='registrar_refeicao'),
   
]