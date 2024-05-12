from django.db import models
from news.models import News


class Comment(models.Model):
    "Comment models"
    news = models.ForeignKey('news.News', to_field="title", on_delete=models.CASCADE, related_name='com')
    user = models.CharField(max_length=25, default="Anonim")
    content = models.TextField()
    time = models.DateTimeField(auto_now_add=True)


class Meta:
    verbose_name = "Comment"
    verbose_name_plural = "Comments"
