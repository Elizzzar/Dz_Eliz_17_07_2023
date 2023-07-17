from django.db import models

# Create your models here.

class Animal(models.Model):
    name_animal = models.CharField(max_length=100)
