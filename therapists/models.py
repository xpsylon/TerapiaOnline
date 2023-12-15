from django.db import models
from django.urls import reverse

class Therapist(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='therapist_pics')
    speciality = models.CharField(max_length=100)
    availability = models.CharField(max_length=100)
    bio = models.TextField()    

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("therapist_detail", kwargs={"pk": self.pk})
