from django.shortcuts import render
import django_filters
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny

from .serializers import PostsSerializer
from .models import Posts


class PostsViewSet(viewsets.ModelViewSet):
    serializer_class = PostsSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)
    queryset = Posts.objects.all()
    search_fields = ['author']
    ordering_fields = ['title', 'date', 'author']
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, SearchFilter, OrderingFilter)
