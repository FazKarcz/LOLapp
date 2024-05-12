import django_filters
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from .models import Bet,Match
from .serializers import BetSerializer,MatchSerializer


class BetViewSet(viewsets.ModelViewSet):
    serializer_class = BetSerializer
    queryset = Bet.objects.all()
    permission_classes = (AllowAny,)
    authentication_classes = (TokenAuthentication,)
    search_fields = []
    ordering_fields = ['match', 'points']
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, SearchFilter, OrderingFilter)


class MatchViewSet(viewsets.ModelViewSet):
    serializer_class = MatchSerializer
    queryset = Match.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)
    search_fields = ['start_time']
    ordering_fields = ['team1', 'start_time']
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, SearchFilter, OrderingFilter)