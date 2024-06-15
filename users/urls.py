from django.urls import path

from .views import LoginView, SignUpView, UserProfile

urlpatterns = [
    path("login/", LoginView.as_view()),
    path("signup/", SignUpView.as_view()),
    path("", UserProfile.as_view()),
]
