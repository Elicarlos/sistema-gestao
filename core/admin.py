from django.contrib import admin
from . models import Estudante, Refeicao, Empresa, Turno, Funcionario, Perfil

# Register your models here.
admin.site.register(Estudante)
admin.site.register(Refeicao)
admin.site.register(Empresa)
admin.site.register(Turno)
admin.site.register(Funcionario)
admin.site.register(Perfil)