from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('post/new/', views.nuevo_posteo, name='post-nuevo'),
    path('posts', views.post_list, name='posts'),
]
