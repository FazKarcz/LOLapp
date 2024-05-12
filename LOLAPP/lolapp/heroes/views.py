from django.shortcuts import render
import django_filters
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Heroes
from .serializers import HeroesSerializer


class HeroesViewSet(viewsets.ModelViewSet):
    serializer_class = HeroesSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Heroes.objects.all()
    search_fields = ['hero_name']
    ordering_fields = ['hero_name', 'role']
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, SearchFilter, OrderingFilter)
