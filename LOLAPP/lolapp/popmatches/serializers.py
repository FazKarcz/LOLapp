from rest_framework import serializers
from .models import Popmatches


class PopMatchesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Popmatches
        fields = (
            'first_team',
            'second_team',
            'date',
            'win_team',
            'result',
            'time',
            'video',
        )