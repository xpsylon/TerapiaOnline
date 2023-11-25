#Creating custom forms
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField() #agrega campo email

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2'] #y pasa estos campos al user recien creado.

# Create a UserUpdateForm to update a username and email
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = ['image']