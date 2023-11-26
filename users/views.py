from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
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

@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        prof_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        
        if user_form.is_valid() and prof_form.is_valid():
            user_form.save()
            prof_form.save()
            messages.success(request, f'Su cuenta ha sido actualizada')
            return redirect('users:perfil')
    
    else:
        user_form = UserUpdateForm(instance=request.user)
        prof_form = ProfileUpdateForm(instance=request.user.profile)
    
    context = {'form_usuario':user_form, 'form_perfil':prof_form }
    
    return render(request, 'users/profile.html', context)