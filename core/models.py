from django.db import models
from django.contrib.auth.models import User

class Empresa(models.Model):
    cnpj = models.CharField(max_length=100)
    nome = models.CharField(max_length=100)

class Turno(models.Model):
    nome = models.CharField(max_length=100)
    quantidade_refeicoes = models.IntegerField()
    inicio = models.TimeField()
    fim = models.TimeField()

    def __str__(self):
        return self.nome
        
class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome_completo = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.nome_completo

class Funcionario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cpf = models.CharField(max_length=14, unique=True)
    cargo = models.CharField(max_length=100)
    # Outros campos adicionais para informações do funcionário

    def __str__(self):
        return self.cpf

class Estudante(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cpf = models.CharField(max_length=14, unique=True)
    matricula = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    nome_completo = models.CharField(max_length=100)
    turno = models.ForeignKey(Turno, on_delete=models.CASCADE, null=True)
    # Outros campos adicionais para informações do estudante

    def __str__(self):
        return self.cpf


class Refeicao(models.Model):
    estudante = models.ForeignKey(Estudante, on_delete=models.CASCADE)
    data = models.DateField()

    def __str__(self):
        return f"Refeição de {self.estudante.perfil.nome_completo} em {self.data}"
