from django.urls import path
from .views import HouseAPIView

urlpatterns = [
    path('gethouses/', HouseAPIView.as_view(), name="get_houses"),
]