from django.urls import path

from users.views import (
    login_view,
    logout_view,
    register_view,
    profile
)

urlpatterns = [
    path("login/", login_view, name='login_view'),
    path("logout/", logout_view, name='logout_view'),
    path("register/", register_view, name='register_view'),
    path("profile/", profile, name='profile_view')
]
