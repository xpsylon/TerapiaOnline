from unittest.util import _MAX_LENGTH
from django.db import models

class Country(models.Model):
    name = models.Model(max_length=50)

class City(models.Model):
    name = models.Model(max_lenght=50)
    