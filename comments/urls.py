from django.urls import path
from .views import CommentsApi

urlpatterns = [
    path('post/', CommentsApi.as_view(), name="post"),
]