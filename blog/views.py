from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User


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
    
class UserPostListView(ListView):
    model = Post
    paginate_by = 5
    template_name = 'blog/user_posts.html'
        
    # Is a method that Django calls to get the list of items to display. In this case, it’s getting a list of Post objects:
    def get_queryset(self):
        # This line is getting the User object that matches the username passed in the URL. If no such user exists, it raises a 404 error:
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')
        
    
    
    
    
    """ 
    The `form_valid` method is a part of Django's class-based views, specifically the `FormView` class, which `CreateView` inherits from²³. 

    In your `PostCreateView` class, you're overriding the `form_valid` method. This method is called when valid form data has been POSTed¹. It's used to define what happens if the form is valid²³.

    In the case of `CreateView`, the parent's `form_valid` method might do some processing (it will call `form.save()` for example)²³. So, when you call `super().form_valid(form)`, you're ensuring that this processing still occurs²³.

    In your specific implementation, you're setting the `author` of the `Post` instance to be the currently logged-in user before calling the parent's `form_valid` method⁴. This means that when a post is created, it's automatically associated with the currently logged-in user.
    
    
    The `PostUpdateView` class you've provided is a Django class-based view that inherits from `LoginRequiredMixin`, `UserPassesTestMixin`, and `UpdateView`. It's used to update an instance of the `Post` model. The class has two methods: `form_valid` and `test_func`.

    1. `form_valid(self, form)`: This method is called when the user submits a valid form. The `form` parameter is the form with data. The method sets the `author` of the `Post` instance to the current logged-in user. It then calls the parent class's `form_valid` method, which saves the form's data to the database.

    2. `test_func(self)`: This method is part of the `UserPassesTestMixin`. It's called to check if the current user passes a certain test condition. In this case, the test is whether the current user is the author of the post. If the user is the author, the method returns `True`; otherwise, it returns `False`. If the test fails (i.e., the method returns `False`), Django will redirect the user to a specified page.
    """


    """  
    user = get_object_or_404(User, username=self.kwargs.get('username')): This line is getting the User object that matches the username passed in the URL. If no such user exists, it raises a 404 error.
    
    So, if you were to navigate to a URL like http://yourwebsite.com/user/johndoe, Django would call the UserPostListView view with username='johndoe'. The get_object_or_404(User, username=self.kwargs.get('username')) line in the view would then attempt to fetch a User object with username='johndoe'. If no such user exists, it would raise a 404 error. If the user does exist, it would return the User object, and the view would proceed to fetch and display all posts authored by that user. 
    """
    
    """ The ordering attribute in Django’s class-based views specifies the default ordering for the entire queryset. However, in this case, the ordering is not uniform for all objects in the queryset. The ordering depends on the specific user, which is determined dynamically based on the username parameter in the URL.

    The get_queryset method allows for more complex queries and dynamic ordering. In this case, it’s used to filter the posts by author and then order them by date_posted. This wouldn’t be possible with a static ordering attribute because the author is not known until the view is called with a specific username. """