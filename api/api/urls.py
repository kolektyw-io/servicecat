"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.landing, name='landing')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='landing')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import administration
import agent.urls
import home.urls
import setup.urls
import users.urls

urlpatterns = [
    path('administration/', include(administration.urls)),
    path('system64/', admin.site.urls),
    path('agent/', include(agent.urls)),
    path('setup/', include(setup.urls)),
    path('user/', include(users.urls)),
    path('', include(home.urls))
]
