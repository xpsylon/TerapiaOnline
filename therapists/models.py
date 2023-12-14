from django.db import models

class Therapist(models.Model):
    name = models.CharField(max_lengtth=100)
    image = models.ImageField(upload_to='therapist_pics')
    speciality = models.CharField(max_length=100)
    availability = models.CharField(max_length=100)
    bio = models.TextField()    

    class Meta:
        verbose_name = _("Therapist")
        verbose_name_plural = _("Therapists")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Therapist_detail", kwargs={"pk": self.pk})
