from django.urls import path, include

import agent.projects
from agent.views import (
    AgentHomeView,
    AgentIssuesView,
    AgentSettingsView
)

urlpatterns = [
    path('settings/', AgentSettingsView.as_view(), name='agent_settings_view'),
    path('mailbox/', AgentIssuesView.as_view(), name='agent_mailbox_view'),
    path('issues/', AgentIssuesView.as_view(), name='agent_issues_view'),
    path('projects/', include(agent.projects)),
    path('', AgentHomeView.as_view(), name='agent_home_view')
]
