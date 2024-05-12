from django.urls import path
from rest_framework.routers import SimpleRouter

from . import views

app_name = 'popmatches'

router = SimpleRouter()

router.register('', views.PopmatchesViewSet, basename='Popmatches')

urlpatterns = router.urls