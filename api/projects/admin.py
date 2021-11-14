from django.contrib import admin

from .models import *

admin.site.register(Project)
admin.site.register(Issue)
admin.site.register(FieldType)
admin.site.register(IssueType)
admin.site.register(IssueState)
admin.site.register(Workflow)
admin.site.register(WorkflowStep)
admin.site.register(Priority)
admin.site.register(IssueField)
admin.site.register(IssueComment)
admin.site.register(IssueHistory)
admin.site.register(IssueSchema)
admin.site.register(IssueSchemaField)
admin.site.register(DataType)
