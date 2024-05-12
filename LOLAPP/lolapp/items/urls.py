from django.urls import path
from rest_framework.routers import SimpleRouter

from . import views

app_name = 'items'

router = SimpleRouter()

router.register('', views.ItemsViewSet, basename='Items')

urlpatterns = router.urls