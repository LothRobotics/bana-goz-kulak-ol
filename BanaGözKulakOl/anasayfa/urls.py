from django.urls import path, include 
from .views import IndexView, LogOutView, AboutUsView, ProfileView, ProfileCustomize
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', IndexView, name = 'index-page'),
    path("accounts/", include("accounts.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("logoutsuccess/", LogOutView, name = 'log-out-success'),
    path("about/", AboutUsView, name = 'about-us-page'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="registration/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),
    path('profile/', ProfileView, name='profile-page'),
    path ('profile/customize', ProfileCustomize, name='profile-customize-page')
]