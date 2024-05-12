from rest_framework import serializers
from .models import Comment
from news.serializers import NewsSerializer

class CommentSerializer(serializers.ModelSerializer):
    time = serializers.DateTimeField(format="%Y-%m-%d %H:%M", read_only=True)


    class Meta:
        model = Comment
        fields = (
            'news',
            'user',
            'content',
            'time')
