from django.utils import timezone
from rest_framework import serializers

from projects.choices import Priorities
from projects.models import Task, Project, Tag

class CreateTaskSerializer(serializers.ModelSerializer):
    project = serializers.SlugRelatedField(
        slug_field='name',
        queryset=Project.objects.all()
    )
    tags = serializers.SlugRelatedField(
        slug_field='name',
        queryset=Tag.objects.all(),
        many=True
    )
    priority = serializers.CharField(
        choices=Priorities.choices(),
        error_messages={'ValidationError': f'Priority have to be one of {Priorities.choices()}'}
    )


    class Meta:
        model = Task
        fields = ['title', 'description', 'priority', 'project', 'tags', 'due_date']

    def validate_title(self, value):
        if len(value) < 7:
            raise serializers.ValidationError(
                "Title have to be at least 7 chars long"
            )
        return value

    def validate_description(self,value):
        if len(value) < 15:
            raise serializers.ValidationError(
                "Description have to be at least 15 chars long")
        return value

    def validate_due_date(self,value):
        if value <  timezone.now():
            raise serializers.ValidationError('Due date can not be in the past')
        return value


class AllTasksSerializer(serializers.ModelSerializer):

    project = serializers.SlugRelatedField(
        read_only=True,
        slug_field="name"
    )
    assignee = serializers.SlugRelatedField(
        read_only=True,
        slug_field="email"
    )

    class Meta:
        model = Task
        fields = ("title", "status", "priority", "project", "assignee", "due_date")


