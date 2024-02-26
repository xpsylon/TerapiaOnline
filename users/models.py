from collections.abc import Iterable
from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) #Delete profile when user is deleted.
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    
    def __str__(self):
        return f'{self.user.username} Profile' #show how we want it to be displayed.
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        imagen = Image.open(self.image.path) # Open image
        
        # Resize image:
        if imagen.height > 300 or imagen.width > 300:
            output_size = (300, 300)
            imagen.thumbnail(output_size) # Resize image to 300, 300
            imagen.save(self.image.path) # Save it again and override the larger image.
        
        
    
#we are creating a table so remember to makemigrations/migrate inmediately afterwards.
#after that, register the model in the admin.py page.

#CHECK WHOLE EXPLANATION HERE:
#https://sl.bing.net/gWkHeOTkd1E