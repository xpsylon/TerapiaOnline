from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'main/home.html')

#QUEDA PARA TESTEAR base.html CADA TANTO:
def base(request):
    return render(request, 'main/base.html')