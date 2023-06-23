from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Funcionario, Estudante, Turno, Perfil
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

class EmpresaForm(forms.Form):
    pass

class CustomUserCreationForm(UserCreationForm):
    nome_completo = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)

    class Meta:
        model = User
        fields = ['nome_completo', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['email']  # Usar o e-mail como o nome de usuário
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
    
class TurnoForm(forms.ModelForm):
    class Meta:
        model = Turno
        fields = ['nome', 'quantidade_refeicoes', 'inicio', 'fim']


class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['nome_completo', 'email']


class FuncionarioCadastroForm(UserCreationForm):
    matricula = forms.CharField(max_length=100)
    cpf = forms.CharField(max_length=100)
    nome_completo = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    cargo = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ['cpf', 'nome_completo', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['cpf']  # Usar o CPF como o nome de usuário
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            funcionario = Funcionario.objects.create(
                perfil=user,
                matricula=self.cleaned_data['matricula'],
                nome_completo=self.cleaned_data['nome_completo'],
                email=self.cleaned_data['email'],
                cargo=self.cleaned_data['cargo']
            )
        return user



class EstudanteCadastroForm(UserCreationForm):
    matricula = forms.CharField(max_length=100)
    cpf = forms.CharField(max_length=100)
    nome_completo = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    turno = forms.ModelChoiceField(queryset=Turno.objects.all())

    class Meta:
        model = User
        fields = ['cpf', 'nome_completo', 'email', 'password1', 'password2']

    def clean_turno(self):
        turno = self.cleaned_data['turno']
        if not turno:
            raise forms.ValidationError("Selecione um turno.")
        return turno

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['cpf']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            estudante = Estudante.objects.create(
                perfil=user,
                matricula=self.cleaned_data['matricula'],
                nome_completo=self.cleaned_data['nome_completo'],
                email=self.cleaned_data['email'],
                turno=self.cleaned_data['turno'].id  # Acessar o ID do objeto selecionado
            )
        return user