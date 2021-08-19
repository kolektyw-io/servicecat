from django.db import models
from django.db.models import CASCADE


class IssueSchema(models.Model):
    """

    """
    pass


class IssueSchemaPosition(models.Model):
    """

    """
    pass


class Project(models.Model):
    name = models.CharField(max_length=500)
    mnemonic = models.CharField(max_length=5)
    description = models.TextField()

    def __str__(self):
        return self.name + f" ({self.mnemonic})"


class ProjectSchema(models.Model):
    pass


class IssueType(models.Model):
    pass


class IssueState(models.Model):
    pass


class Workflow(models.Model):
    pass


class WorkflowStep(models.Model):
    pass


class Issue(models.Model):
    project = models.ForeignKey(Project, on_delete=CASCADE)
    number = models.BigIntegerField()


class IssueComment(models.Model):
    pass


class IssueHistory(models.Model):
    pass
