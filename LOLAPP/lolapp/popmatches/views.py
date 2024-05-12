from django.shortcuts import render
import django_filters
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import PopMatchesSerializer
from .models import Popmatches


class PopmatchesViewSet(viewsets.ModelViewSet):
    serializer_class = PopMatchesSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Popmatches.objects.all()
    search_fields = ['win_team']
    ordering_fields = ['date']
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, SearchFilter, OrderingFilter)

