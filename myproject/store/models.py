from django.db import models

# Create your models here.
class About(models.model):
    description = models.CharField(max_length=500)
    designtion = models.CharField(max_length=200)
    shot_description = models.CharField(max_length=100)
    Birth = models.DateFieldField()
    website_link = models.URLField(max_length=1000)
    phone = models.PositiveIntegerField()
    ctiy = models.CharField(max_length=100)
    age = models.IntegerField(max_length=10)
    degree = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    freelance = models.CharField(max_length=100)