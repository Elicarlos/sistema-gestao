from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('registrar-refeicao/', views.registrar_refeicao, name='registrar_refeicao'),
    path('cadastrar-estudante/', views.cadastrar_estudante, name='cadastrar_estudante'),
    path('cadastrar-funcionario/', views.cadastrar_funcionario, name='cadastrar_funcionario'),
    path('cadastrar-empresa/', views.cadastrar_empresa, name='cadastrar_empresa'),
    path('cadastrar-turno/', views.cadastrar_turno, name='cadastrar-turno'),
    path('pagina-sucesso/', views.pagina_sucesso, name='pagina_sucesso'),
    
]
