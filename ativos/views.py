from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url='/login/')
def main(request):
    return render(request, 'main.html')


def index(request):
    return render(request, 'index.html')


def aboutus(request):
    return render(request, 'aboutus.html')


def login_user(request):
    return render(request, 'login.html')


def logout_user(request):
    print(request.user)
    logout(request)
    return redirect('/')


@csrf_protect
def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/main/')
        else:
            messages.error(request, 'Usuário ou Senha inválida')
    return redirect('/login/')