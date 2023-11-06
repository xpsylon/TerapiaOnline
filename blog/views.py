from django.shortcuts import render, redirect
from .forms import PostForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required

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

