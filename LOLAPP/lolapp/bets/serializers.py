from rest_framework import serializers
from .models import Bet,Match


class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = (
            'start_time',
            'team1',
            'team2'
            )


class BetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bet
        fields = (
            'match',
            'selected_team',
            'points',
        )