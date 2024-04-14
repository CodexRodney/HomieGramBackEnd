from django.urls import path
from .views import CommentsApi

urlpatterns = [
    path('post/', CommentsApi.as_view(), name="post"),
    path('getComments/', CommentsApi.as_view(), name="getComment")
    # path("getComments/",CommentsApi.as_view(), name="getComments")
]