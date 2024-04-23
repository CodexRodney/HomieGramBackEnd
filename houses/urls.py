from django.urls import path
from .views import HouseAPIView, SearchApiView

urlpatterns = [
    path('gethouses/', HouseAPIView.as_view(), name="get_houses"),
    path("search/<str:name>", SearchApiView.as_view(), name="search_house")
]