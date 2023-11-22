from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('register/', views.registro, name='registro'),
    #funcionan sin view explicita, xq usa por default la basica built ins:    
    path('login/', views.login, name='login'), 
    path('logout/', views.logout, name='logout'), 
    path('profile/', views.profile, name='perfil'),
]