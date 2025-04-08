from django.core.validators import MinLengthValidator
from django.db import models

from projects.choices import Statuses, Priorities
from projects.models.project import Project
from projects.models.tag import Tag
from projects.models.user import User


class Task(models.Model):
    title = models.CharField(
        max_length=255, unique=True, validators=[MinLengthValidator(10)]
    )
    description = models.TextField(null=True, blank=True)
    status = models.CharField(
        max_length=15,
        choices=Statuses.choices(),
        default=Statuses.NEW.value
    )
    tags = models.ManyToManyField(Tag)
    priority = models.CharField(
        max_length=15,
        choices=Priorities.choices(),
        default=Priorities.MEDIUM.db_value
    )
    assignee = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True)
    deleted = models.BooleanField(default=False)
    project = models.ForeignKey(Project, on_delete=models.PROTECT)
    due_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
        default_related_name = "tasks"
        ordering = ['-due_date', '-priority']
        unique_together = (('title', 'project'),)

