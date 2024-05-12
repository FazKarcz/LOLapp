from django.db import models
from items.models import Items

class Heroes(models.Model):
    """Heroes model"""
    hero_name = models.CharField(max_length=256, unique=True)  # Nazwa Bohatera
    release_date = models.DateField()  # Data wydania
    description = models.TextField(max_length=500)  # Opis
    origin = models.CharField(max_length=256)  # Pochodzenie
    role = models.CharField(max_length=4)  # Rola
    item = models.ForeignKey(Items, on_delete=models.CASCADE) # Najpopularniejszy Przedmiot dla postaci

    def __str__(self):
        return f"{self.hero_name}"