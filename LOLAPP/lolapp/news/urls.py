from django.urls import path
from rest_framework.routers import SimpleRouter

from . import views

app_name = 'news'

router = SimpleRouter()

router.register('', views.NewsViewSet, basename='News')

urlpatterns = router.urls
