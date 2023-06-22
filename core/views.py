

from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Estudante, Refeicao

from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Estudante, Refeicao

from .forms import EstudanteForm


def cadastrar_estudante(request):
    if request.method == 'POST':
        form = EstudanteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pagina_sucesso')  # Redirecionar para a página de sucesso após o cadastro
    else:
        form = EstudanteForm()
    
    return render(request, 'cadastro_estudante.html', {'form': form})


def registrar_refeicao(request):
    if request.method == 'POST':
        carteirinha = request.POST.get('carteirinha')
        
        # Verifica se a carteirinha é válida e pertence a um estudante registrado
        estudante = Estudante.objects.filter(carteirinha=carteirinha).first()
        if estudante:
            # Verifica se o estudante já fez uma refeição hoje
            if not Refeicao.objects.filter(estudante=estudante, data=timezone.now().date()).exists():
                # O estudante ainda não almoçou hoje, registra a refeição
                refeicao = Refeicao(estudante=estudante, data=timezone.now().date())
                refeicao.save()
                return render(request, 'refeicao_sucesso.html')
    
    # Exibe o formulário para fazer o pedido da refeição
    return render(request, 'fazer_refeicao.html')
