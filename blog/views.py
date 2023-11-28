from django.shortcuts import render, redirect
from .forms import PostForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Post

def post_list(request):
    context = {
        'manzanas': Post.objects.all()
    }
    return render(request, 'blog/posts.html', context)

@login_required
def nuevo_posteo(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
        return redirect(reverse('main:casa'))
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {'formulario':form})

"""
    This view function handles the creation of a new post.

    The function is decorated with the `login_required` decorator, which ensures that only authenticated users can access this view.

    If the request method is 'POST', it means the form is being submitted. The function then checks if the form is valid. If it is, it saves the form but with commit=False to prevent it from being saved immediately. This is done so that the author of the post can be added before saving the post to the database.

    If the form is not valid or if the request method is not 'POST' (which means the form is being accessed for the first time), an empty form is created and passed to the template.

    Parameters:
    request (WSGIRequest): A HTTP Request instance.

    Returns:
    HTTPResponse: The HTTP Response instance.
    """
