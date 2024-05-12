from django.urls import path
from rest_framework.routers import SimpleRouter

from . import views

app_name = 'comments'

router = SimpleRouter()

router.register('', views.CommentsViewSet, basename='Comments')

urlpatterns = router.urls