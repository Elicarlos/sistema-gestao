from django.db import models
from django.contrib.auth.models import User

class Estudante(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    carteirinha = models.CharField(max_length=100)
    # Outros campos adicionais para informações do estudante

    def __str__(self):
        return self.user.username


class Refeicao(models.Model):
    estudante = models.ForeignKey(Estudante, on_delete=models.CASCADE)
    data = models.DateField()

    def __str__(self):
        return f"Refeição de {self.estudante.user.username} em {self.data}"
