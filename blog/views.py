from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


# With class based views, the system renders by default a template with the following convention name:
# <app>/<model>_<viewtype>.html>
# So in this case, the default template name would be:
# blog/post_list.html
class PostListView(ListView):
    model = Post
    ordering = ['-date_posted'] # Orden negativo date_posted. Del ultimo al primer posteo. Como en los mails.
    paginate_by = 5
    
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
    
class PostCreateView(LoginRequiredMixin, CreateView): # El mixin siempre a la izquierda.
    model = Post
    fields = ['title', 'content']
    # Overriding form_valid() method from CreateView, so only logged-in users can post new:
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
 
# UserPassesTestMixin: only the author can update his own post. The test we are creating as a function in the end of the PostUpdateClass.
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    # Test function of the UserPassesTestMixin:
    def test_func(self) -> bool | None:
        post = self.get_object() # Getting the post that we are trying to update. It will return a pk.
        if self.request.user == post.author: # Checking if the current (logged in) user is the author of the post.
            return True
        return False
    
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/blog/'
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    
    """ 
    The `form_valid` method is a part of Django's class-based views, specifically the `FormView` class, which `CreateView` inherits from²³. 

    In your `PostCreateView` class, you're overriding the `form_valid` method. This method is called when valid form data has been POSTed¹. It's used to define what happens if the form is valid²³.

    In the case of `CreateView`, the parent's `form_valid` method might do some processing (it will call `form.save()` for example)²³. So, when you call `super().form_valid(form)`, you're ensuring that this processing still occurs²³.

    In your specific implementation, you're setting the `author` of the `Post` instance to be the currently logged-in user before calling the parent's `form_valid` method⁴. This means that when a post is created, it's automatically associated with the currently logged-in user.
    
    
    The `PostUpdateView` class you've provided is a Django class-based view that inherits from `LoginRequiredMixin`, `UserPassesTestMixin`, and `UpdateView`. It's used to update an instance of the `Post` model. The class has two methods: `form_valid` and `test_func`.

    1. `form_valid(self, form)`: This method is called when the user submits a valid form. The `form` parameter is the form with data. The method sets the `author` of the `Post` instance to the current logged-in user. It then calls the parent class's `form_valid` method, which saves the form's data to the database.

    2. `test_func(self)`: This method is part of the `UserPassesTestMixin`. It's called to check if the current user passes a certain test condition. In this case, the test is whether the current user is the author of the post. If the user is the author, the method returns `True`; otherwise, it returns `False`. If the test fails (i.e., the method returns `False`), Django will redirect the user to a specified page.
    """
