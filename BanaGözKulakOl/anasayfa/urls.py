from django.urls import path, include 
from .views import IndexView, LogOutView, AboutUsView, ProfileView

urlpatterns = [
    path('', IndexView, name = 'index-page'),
    path("accounts/", include("accounts.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("logoutsuccess/", LogOutView, name = 'log-out-success'),
    path("about/", AboutUsView, name = 'about-us-page'),
    path("profile/", ProfileView, name = 'my-profile-page'),
]