from django.db import models

# Create your models here.


class Posts(models.Model):
    """ Posts model"""
    author = models.CharField(max_length=25)
    title = models.CharField(max_length=35)  # Tytuł posta
    date = models.DateField(auto_now=True)  # Data posta
    text = models.TextField(max_length=1500)  # Środek posta