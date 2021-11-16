from django.urls import path

from users.views import (
    login_view,
    logout_view,
    profile,
    user_not_agent,
    user_not_authenticated,
    RegisterUserView,
    PasswordChangeView
)

urlpatterns = [
    path("login/", login_view, name='login_view'),
    path("logout/", logout_view, name='logout_view'),
    path("register/", RegisterUserView.as_view(), name='register_view'),
    path("profile/", profile, name='profile_view'),
    path("change_password", PasswordChangeView.as_view(), name='change_password'),
    path("errors/client_only", user_not_agent, name='error_user_not_an_agent'),
    path("errors/unauthenticated", user_not_authenticated, name='error_user_not_authenticated'),
]
