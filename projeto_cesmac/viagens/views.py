from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, UserProfileForm, ViagemForm
from .models import Viagem


def signup(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        user_form = CustomUserCreationForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            messages.success(request, 'Cadastro realizado com sucesso! Faça login.')
            return redirect('login')
    else:
        user_form = CustomUserCreationForm()
        profile_form = UserProfileForm()

    return render(request, 'viagens/signup.html', {'user_form': user_form, 'profile_form': profile_form})


def user_login(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Usuário ou senha inválidos.')

    return render(request, 'viagens/login.html')


def user_logout(request):
    logout(request)
    return redirect('login')


@login_required
def home(request):
    return render(request, 'viagens/home.html')


@login_required
def criar_viagem(request):
    if request.method == 'POST':
        form = ViagemForm(request.POST)
        if form.is_valid():
            viagem = form.save(commit=False)
            viagem.motorista = request.user
            viagem.save()
            messages.success(request, 'Viagem criada com sucesso!')
            return redirect('listar_viagens')
    else:
        form = ViagemForm()

    return render(request, 'viagens/criar_viagem.html', {'form': form})


@login_required
def listar_viagens(request):
    viagens = Viagem.objects.all()
    return render(request, 'viagens/listar_viagens.html', {'viagens': viagens})


@login_required
def detalhar_viagem(request, viagem_id):
    viagem = get_object_or_404(Viagem, id=viagem_id)
    return render(request, 'viagens/detalhar_viagem.html', {'viagem': viagem})


@login_required
def reservar_viagem(request, viagem_id):
    viagem = get_object_or_404(Viagem, id=viagem_id)
    if viagem.vagas > 0:
        viagem.vagas -= 1
        if viagem.vagas == 0:
            viagem.delete()
            messages.success(request, 'Reserva concluída. A viagem foi removida pois não há mais vagas.')
            return redirect('listar_viagens')
        else:
            viagem.save()
            messages.success(request, 'Reserva concluída com sucesso.')
            return redirect('detalhar_viagem', viagem_id=viagem.id)
    else:
        messages.error(request, 'Não há vagas disponíveis para esta viagem.')
        return redirect('listar_viagens')
