from rest_framework import serializers

from .models import Heroes


class HeroesSerializer(serializers.ModelSerializer):
    item = serializers.CharField(source="item.item_name", read_only=True)

    class Meta:
        model = Heroes
        fields = (
            'hero_name',
            'release_date',
            'description',
            'origin',
            'role',
            'item',
        )