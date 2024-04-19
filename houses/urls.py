from django.urls import path
from .views import HouseAPIView

urlpatterns = [
    path('gethouse/', HouseAPIView.as_view(), name="get_house_by_id"),
]