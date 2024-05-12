from django.urls import path
from rest_framework.routers import SimpleRouter

from . import views

app_name = 'heroes'

router = SimpleRouter()

router.register('', views.HeroesViewSet, basename='Heroes')

urlpatterns = router.urls