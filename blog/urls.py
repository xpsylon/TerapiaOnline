from django.urls import path
from . import views
from .views import PostListView
app_name = 'blog'

urlpatterns = [
    path('post/new/', views.nuevo_posteo, name='post-nuevo'),
    path('posts/', PostListView.as_view(), name='posts'),
]
