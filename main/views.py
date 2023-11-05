from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from django.urls import reverse

@login_required
def home(request):
    return render(request, 'main/home.html')

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
    return render(request, 'main/post_form.html', {'formulario':form})


#QUEDA PARA TESTEAR base.html CADA TANTO:
def base(request):
    return render(request, 'main/base.html')

""" The `@login_required` decorator in Django is a handy tool that helps secure your views by ensuring that only authenticated users can access them. Here's a simplified explanation of how it works:

1. When you decorate a view function with `@login_required`, Django checks if the user associated with the current request is authenticated³.
2. If the user is authenticated, Django proceeds to execute the view function¹.
3. If the user is not authenticated, Django redirects them to the login page¹.

Here's an example of how you might use it in your code:

from django.contrib.auth.decorators import login_required

@login_required
def my_view(request):
    # Your view logic here
```

In this example, `my_view` is only accessible to users who are logged in. If a user who is not logged in tries to access `my_view`, they will be redirected to the login page.

Behind the scenes, `@login_required` is actually a shortcut for a more general function called `user_passes_test`. This function accepts a test function and applies it to the user. If the user passes the test, they are allowed to access the view. If they fail, they are redirected to the login page¹. The `@login_required` decorator simply uses a test function that checks if `user.is_authenticated` is `True`. """

