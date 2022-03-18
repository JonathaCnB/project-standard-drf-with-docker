
from django.urls import path

from .views import GetProfileAPIView, ProfileListAPIView, UpdateProfileAPIView

urlpatterns = [
    path("me/", GetProfileAPIView.as_view(), name="get_profile"),
    path(
        "update/<str:username>/",
        UpdateProfileAPIView.as_view(),
        name="update_profile"
    ),
    path("all/", ProfileListAPIView.as_view(), name="all-profiles"),
]
