from django.shortcuts import render
from .forms import UserRegisterForm

def registro(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
    else:
        form = UserRegisterForm()

    return render(request, 'users/sign_up.html', {'formulario':form})