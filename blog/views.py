from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Post
from django.views.generic import ListView, DetailView, CreateView


# With class based views, the system renders by default a template with the following convention name:
# <app>/<model>_<viewtype>.html>
# So in this case, the default template name would be:
# blog/post_list.html
class PostListView(ListView):
    model = Post
    ordering = ['-date_posted'] # Orden negativo date_posted. Del ultimo al primer posteo. Como en los mails.
    
    # IF OLD TEMPLATE AND LOOPING NAMES WOULD HAVE BEEN KEPT:
    # context_object_name = 'manzanas'
    # template_name = 'posts.html'

""" def post_list(request):
    context = {
        'manzanas': Post.objects.all()
    }
    return render(request, 'blog/posts.html', context) """
    
class PostDetailView(DetailView):
    model = Post
    
class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']
    # Overriding form_valid() method from CreateView, so only logged-in users can post new:
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    """ 
    The `form_valid` method is a part of Django's class-based views, specifically the `FormView` class, which `CreateView` inherits from²³. 

    In your `PostCreateView` class, you're overriding the `form_valid` method. This method is called when valid form data has been POSTed¹. It's used to define what happens if the form is valid²³.

    In the case of `CreateView`, the parent's `form_valid` method might do some processing (it will call `form.save()` for example)²³. So, when you call `super().form_valid(form)`, you're ensuring that this processing still occurs²³.

    In your specific implementation, you're setting the `author` of the `Post` instance to be the currently logged-in user before calling the parent's `form_valid` method⁴. This means that when a post is created, it's automatically associated with the currently logged-in user.
    """
