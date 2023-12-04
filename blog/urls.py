from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView
app_name = 'blog'

urlpatterns = [
    path('post/new/', PostCreateView.as_view(), name='post-nuevo'),
    path('', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detalle'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'), 
    path('post/<str:username>', UserPostListView.as_view(), name='user-posts'), 
]
