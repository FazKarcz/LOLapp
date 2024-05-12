import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Items
from .serializers import ItemsSerializer


class ItemsFilter:
    pass

class ItemsViewSet(viewsets.ModelViewSet):
    serializer_class = ItemsSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Items.objects.all()
    search_fields = ['item_name', 'is_mythic', 'item_price']
    ordering_fields = ['item_name','is_mythic']
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, SearchFilter, OrderingFilter)
