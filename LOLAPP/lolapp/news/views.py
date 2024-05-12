from django.shortcuts import render

from django.shortcuts import render
import django_filters
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .serializers import NewsSerializer
from .models import News

class NewsViewSet(viewsets.ModelViewSet):
    serializer_class = NewsSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = News.objects.all()
    search_fields = ['title']
    ordering_fields = ['title', 'date']
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, SearchFilter, OrderingFilter)
