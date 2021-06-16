from django.urls import path

from home.views import (
    logged_out,
    home_view
)

urlpatterns = [
    path('logged_out/', logged_out, name='logged_out'),
    path('', home_view, name="home"),
]
