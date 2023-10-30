#Creating custom forms
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField() #agrega campo email

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2'] #y pasa estos campos al user recien creado.