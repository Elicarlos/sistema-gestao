from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Estudante, Refeicao, Turno, Perfil  
from .forms import FuncionarioCadastroForm, EstudanteCadastroForm, EmpresaForm, TurnoForm
from django.contrib.admin.views.decorators import staff_member_required
from datetime import datetime

def home(request):
    return render(request, 'home.html')

def cadastrar_empresa(request):
    if request.method == 'POST':
        form = EmpresaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pagina_sucesso')  # Redirecionar para a página de sucesso após o cadastro
    else:
        form = EmpresaForm()
    
    return render(request, 'cadastro_empresa.html', {'form': form})

def pagina_sucesso(request):
    return render(request, 'pagina_sucesso.html')

def cadastrar_turno(request):
    if request.method == 'POST':
        form = TurnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pagina_sucesso')  # Redirecionar para a página de sucesso após o cadastro
    else:
        form = TurnoForm()
    
    return render(request, 'cadastro_turno.html', {'form': form})

def listar_turnos(request):
    turnos = Turno.objects.all()
    return render(request, 'listar_turnos.html', {'turnos': turnos})

def cadastrar_estudante(request):
    if request.method == 'POST':
        form = EstudanteCadastroForm(request.POST)
        if form.is_valid():
            cpf = form.cleaned_data['cpf']
            
            # Verifica se já existe um usuário com o mesmo CPF
            if User.objects.filter(username=cpf).exists():
                return render(request, 'cpf_duplicado.html')  # Renderiza uma página informando que o CPF já está em uso
            
            user = User.objects.create_user(username=cpf)
            user.set_unusable_password()
            user.save()
            
            estudante = Estudante(user=user)
            estudante.cpf = cpf
            estudante.email = form.cleaned_data['email']
            estudante.save()
            
            return redirect('pagina_sucesso')
    else:
        form = EstudanteCadastroForm()
    
    return render(request, 'cadastro_estudante.html', {'form': form})


@staff_member_required
def cadastrar_funcionario(request):
    if request.method == 'POST':
        form = FuncionarioCadastroForm(request.POST)
        if form.is_valid():
            funcionario = form.save(commit=False)
            funcionario.username = form.cleaned_data['cpf']  # Usar o CPF como o nome de usuário
            funcionario.email = form.cleaned_data['email']
            funcionario.save()
            return redirect('pagina_inicial')
    else:
        form = FuncionarioCadastroForm()
    
    return render(request, 'cadastro_funcionario.html', {'form': form})

def registrar_refeicao(request):
    if request.method == 'POST':
        matricula = request.POST.get('matricula')

        # Verifica se a carteirinha é válida e pertence a um estudante registrado
        estudante = Estudante.objects.filter(matricula=matricula).first()
        if estudante:
            turno = estudante.turno

            # Verifica se o horário atual está dentro do intervalo de início e fim do turno
            now = datetime.now().time()
            if turno.inicio <= now <= turno.fim:
                # Verifica se o estudante já fez uma refeição hoje
                if not Refeicao.objects.filter(estudante=estudante, data=datetime.now().date()).exists():
                    # O estudante ainda não almoçou hoje, registra a refeição
                    refeicao = Refeicao(estudante=estudante, data=datetime.now().date())
                    refeicao.save()
                    return render(request, 'refeicao_sucesso.html')
                else:
                    return render(request, 'refeicao_duplicada.html')  # O estudante já fez uma refeição hoje
            else:
                return render(request, 'horario_invalido.html')  # Horário fora do intervalo permitido
        else:
            return render(request, 'matricula_invalida.html')  # Carteirinha inválida

    # Exibe o formulário para fazer o pedido da refeição
    return render(request, 'fazer_refeicao.html')
