from django.contrib.auth.models import User
from django.db import models
from django.db.models import CASCADE, Choices


class DataType(models.Model):
    class DataTypes(models.TextChoices):
        CHOICE_FIELD = 'CF', "Choice field"
        MULTISELECT_CHOICE_FIELD = 'MCF', "Multiselect choice field"
        LABEL = 'L', "Label"
        MULTISELECT_LABEL = 'ML', "Multiselect label"
        DATE = 'D', "Date"
        TIME = 'T', "Time"
        DURATION = 'Du', "Duration"
        DATETIME = 'DT', "Date with time"

    name = models.CharField(max_length=500)
    type = models.CharField(max_length=5, choices=DataTypes.choices)

    def __str__(self):
        return self.name + f" ({self.type})"
class FieldType(models.Model):
    """
        Defines field types. Allowed data types are:
        ChoiceField, Label,
    """

    name = models.CharField(max_length=100)
    data_type = models.CharField(max_length=100)


class FieldValues(models.Model):
    """
        Defines allowed values for fields
    """
    key = models.ForeignKey(FieldType, on_delete=models.deletion.CASCADE)
    value = models.CharField(max_length=500, null=True, blank=True)
    default_value = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)


class Project(models.Model):
    name = models.CharField(max_length=500)
    mnemonic = models.CharField(max_length=5)
    icon = models.TextField(blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return self.name + f" ({self.mnemonic})"


class IssueType(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class IssueState(models.Model):
    name = models.CharField(max_length=100)
    as_draft = models.BooleanField(default=True)
    as_done = models.BooleanField(default=False)

    def __str__(self):
        if self.as_done:
            return f"(Done) {self.name}"
        if self.as_draft:
            return f"(Draft) {self.name}"
        return self.name


class Workflow(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class WorkflowStep(models.Model):
    workflow = models.ForeignKey(Workflow, on_delete=models.deletion.CASCADE)
    step_name = models.CharField(max_length=100)


class Priority(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

class IssueSchema(models.Model):
    """

    """
    name = models.CharField(max_length=200)
    project = models.ForeignKey(Project, on_delete=models.deletion.CASCADE)
    issue_type = models.ForeignKey(IssueType, on_delete=models.deletion.CASCADE)
    workflow = models.ForeignKey(Workflow, blank=True, null=True,
                                 on_delete=models.deletion.SET_NULL)

    def __str__(self):
        return f"{self.project.mnemonic}: {self.name} for {self.issue_type.name}"


class IssueSchemaField(models.Model):
    """

    """
    schema = models.ForeignKey(IssueSchema, on_delete=models.deletion.CASCADE)
    field = models.ForeignKey(FieldType, on_delete=models.deletion.CASCADE)
    default_value = models.CharField(max_length=500, null=True, blank=True)
    allow_empty = models.BooleanField()

class Issue(models.Model):
    project = models.ForeignKey(Project, on_delete=CASCADE)
    number = models.BigIntegerField()
    summary = models.CharField(max_length=250)
    issue_type = models.ForeignKey(IssueType,
                                   on_delete=models.deletion.PROTECT)
    priority = models.ForeignKey(Priority, null=True,
                                 on_delete=models.deletion.SET_NULL)
    assignee = models.ForeignKey(User, null=True,
                                 on_delete=models.deletion.SET_NULL,
                                 related_name="assignee")
    creator = models.ForeignKey(User, null=True,
                                on_delete=models.deletion.SET_NULL,
                                related_name="creator")
    schema = models.ForeignKey(IssueSchema, null=True, on_delete=models.deletion.SET_NULL)


class IssueField(models.Model):
    issue = models.ForeignKey(Issue, on_delete=models.deletion.CASCADE)
    field_type = models.ForeignKey(FieldType, on_delete=models.deletion.CASCADE)
    value = models.CharField(max_length=500, null=True, blank=True)
    state = models.ForeignKey(IssueState, on_delete=models.deletion.PROTECT)


class IssueComment(models.Model):
    issue = models.ForeignKey(Issue, on_delete=CASCADE)
    user = models.ForeignKey(User, null=True,
                             on_delete=models.deletion.SET_NULL)
    date = models.DateTimeField(auto_created=True)
    comment = models.CharField(max_length=4096)
    internal = models.BooleanField(default=True)


class IssueHistory(models.Model):
    issue = models.ForeignKey(Issue, on_delete=CASCADE)
    user = models.ForeignKey(User, null=True,
                             on_delete=models.deletion.SET_NULL)
    date = models.DateTimeField(auto_created=True)
    data = models.CharField(max_length=8192)
