from django.urls import path, include

from apps.accounts.views import IndexView, edit_user_details, my_profile


urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("update_user/", edit_user_details, name="user-edit"),
    path("accounts/profile/", my_profile, name="profile"),
    path("accounts/", include("allauth.urls")),
]
