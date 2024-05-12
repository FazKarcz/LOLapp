from django.db import models


class Match(models.Model):
    team1 = models.CharField(max_length=20)
    team2 = models.CharField(max_length=20)
    start_time = models.DateTimeField()


class Bet(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    selected_team = models.CharField(max_length=20)
    points = models.FloatField(default=0.0)
