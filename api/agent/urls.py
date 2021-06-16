from django.urls import path

from agent.views import agent_home_view

urlpatterns = [
    path('', agent_home_view, name='agent_home_view')
]