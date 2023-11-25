from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) #Delete profile when user is deleted.
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    
    def __str__(self):
        return f'{self.user.username} Profile' #show how we want it to be displayed.
    
#we are creating a table so remember to makemigrations/migrate inmediately afterwards.
#after that, register the model in the admin.py page.