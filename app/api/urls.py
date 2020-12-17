
from django.urls import path
from .views import PlayersListAPIView



urlpatterns = [
path('api/players', PlayersListAPIView.as_view())
]