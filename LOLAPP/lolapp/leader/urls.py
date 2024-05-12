from django.urls import path
from .views import AmericanApiView,EuropeApiView,OtherApiView

urlpatterns = [
    path('usa/', AmericanApiView.as_view(), name='leader_usa'),
    path('eu/', EuropeApiView.as_view(), name='leader_eu'),
    path('other/', OtherApiView.as_view(), name='leader_other'),
]