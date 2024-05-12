from django.urls import path
from rest_framework.routers import SimpleRouter

from . import views

app_name = 'posts'

router = SimpleRouter()

router.register('', views.PostsViewSet, basename='Posts')

urlpatterns = router.urls