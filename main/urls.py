from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home, name='casa'),
    path('home', views.home, name='casa'),
    #Solo se usa para testear base:
    path('base', views.base, name='base'),
]