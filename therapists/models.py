from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Therapist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()    
    speciality = models.CharField(max_length=100)
    availability = models.CharField(max_length=100)
    license_number = models.CharField(max_length=50, null=True, unique=True, blank=True)

    def __str__(self):
        return f'{ self.user.first_name } { self.user.last_name }'

    def get_absolute_url(self):
        return reverse("therapist_detail", kwargs={"pk": self.pk})
