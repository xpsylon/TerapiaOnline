from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return reverse('blog:post-detalle', kwargs={"pk": self.pk})
    
    
       
    """ 
    In Django, the get_absolute_url method is used to get the canonical URL for an object. It tells Django how to calculate the URL for an object. In your Post model, the get_absolute_url method is using the reverse function to return the URL for the detail view of the post.

    The reverse function in Django is used to generate URLs by reversing the URL patterns defined in your urls.py. It takes a URL pattern name as its first argument and any arguments for the URL pattern as keyword arguments. In your case, reverse('post-detail', kwargs={'pk': self.pk}) is generating a URL for the post-detail view, passing the posts primary key (self.pk) as an argument.

    On the other hand, redirect is a function that returns an HttpResponseRedirect to the appropriate URL for the arguments passed. It can take a model, view name, or URL as its argument, and it will use get_absolute_url if a model is passed.

    So, the main difference between redirect and reverse is that redirect actually sends a redirect response to the user, while reverse simply calculates a URL. You would use reverse when you want to calculate a URL to use elsewhere in your code, and redirect when you want to send the user to a different page in response to an action (like creating a new post). 
    """
    
    