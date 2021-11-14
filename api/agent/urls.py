from django.urls import path

from agent.views import agent_home_view, AgentHomeView

urlpatterns = [
    path('', AgentHomeView.as_view(), name='agent_home_view')
]