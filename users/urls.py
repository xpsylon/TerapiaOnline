from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('register/', views.registro, name='registro'),    
    path('login/', views.login, name='login'), #funciona sin view explicita, xq usa por default la basica built in de
    path('logout/', views.logout, name='logout'), #funciona sin view explicita, xq usa por default la basica built in    
]