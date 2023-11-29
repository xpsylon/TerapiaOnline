from django.forms import ModelForm
from .models import Post

# Formulario para CreatePost
class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']