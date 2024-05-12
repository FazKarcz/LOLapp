from django.urls import path, include
from rest_framework.routers import SimpleRouter
from . import views

app_name = 'bets'

router = SimpleRouter()
router.register('bets', views.BetViewSet)
router.register('matches', views.MatchViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
