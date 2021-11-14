from django.urls import path

from agent.views import (
    AgentHomeView,
    AgentProjectsView,
    AgentIssuesView,
    AgentSettingsView
)

urlpatterns = [
    path('settings/', AgentSettingsView.as_view(), name='agent_settings_view'),
    path('mailbox/', AgentIssuesView.as_view(), name='agent_mailbox_view'),
    path('issues/', AgentIssuesView.as_view(), name='agent_issues_view'),
    path('projects/', AgentProjectsView.as_view(), name='agent_projects_view'),
    path('', AgentHomeView.as_view(), name='agent_home_view')
]
