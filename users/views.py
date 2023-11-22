from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib.auth import login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def registro(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()            
            username = form.cleaned_data.get('username')
            messages.success(request, f'Cuenta creada para {username}. Ya puede iniciar sesion')
            return redirect ('users:login')
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'formulario':form})

login_required
def profile(request):
    return render(request, 'users/profile.html')