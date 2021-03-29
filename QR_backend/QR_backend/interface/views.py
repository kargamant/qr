from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from .forms import UserLoginForm
from django.contrib.auth import login, logout
import time

app = 'interface/'
# Create your views here.
def index(request):
    return render(request, f'{app}index.html')

def books(request):
    return render(request, f'{app}books.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы зарегистрированы!')
            time.sleep(3)
            return redirect('login')
        else:
            messages.error(request, 'Произошла ошибка при регистрации')
    else:
        form = UserCreationForm()
    return render(request, f'{app}register.html', {'form': form})

def User_login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
    else:
        form = UserLoginForm()
    return render(request, f'{app}lonin.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('/')