from django.db import models

# Create your models here.
class About(models.Model):
    description = models.CharField(max_length=500)
    designtion = models.CharField(max_length=100)
    shot_description = models.CharField(max_length=500)
    birth = models.DateField()
    website_link = models.URLField(max_length=1000)
    phone = models.PositiveIntegerField()
    ctiy = models.CharField(max_length=100)
    age = models.IntegerField(max_length=10)
    degree = models.CharField(max_length=100)
    email = models.EmailField()