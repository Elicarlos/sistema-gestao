from django import forms
from .models import Estudante

class EstudanteForm(forms.ModelForm):
    class Meta:
        model = Estudante
        fields = ['nome', 'email', 'numero_carteirinha']  # Adicione os campos necessários do modelo Estudante
