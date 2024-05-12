from django.db import models


class Items(models.Model):
    """Items model"""
    item_name = models.CharField(max_length=256, unique=True)  # Nazwa Bohatera
    description = models.TextField(max_length=500)  # Opis
    item_price = models.IntegerField()  # Cena
    is_mythic = models.BooleanField()  # Czy jest Mythicem

    def __str__(self):
        return f"{self.item_name}"
