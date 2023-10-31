from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib.auth import login

def registro(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            #guarda los datos del form en variable user:
            user = form.save()
            #aparte loginea al user recien creado (previamente hay que importar el metodo login)
            #en Project Three es diferente, se crea perfil y el redirect es a login para obviamente loginearse:
            login(request, user)
            return redirect('main:casa')
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'formulario':form})