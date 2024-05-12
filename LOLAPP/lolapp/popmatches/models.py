from django.db import models

class Popmatches(models.Model):
    first_team = models.CharField(max_length=25)
    second_team = models.CharField(max_length=25)
    date = models.DateField()  # Data meczu
    time = models.FloatField(default=30)  # Czas trwania meczu w minutach
    win_team = models.CharField(max_length=25) # Drużyna która wygrała
    result = models.CharField(max_length=20) # Wynik
    video = models.CharField(max_length= 255) # video


def __str__(self):
    return f"{self.first_team} vs {self.second_team}, Wygrana: {self.win_team} Wynik: {self.result}"
