import os

from rest_framework import serializers
from projects.models import Project, ProjectFile
from projects.utils.file_helpers import (
    check_extension,
    ALLOWED_EXTENSIONS,
    check_file_size,
    create_file_path,
    save_file
)


class ProjectsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'name', 'date_started')


class ProjectDetailSerializer(serializers.ModelSerializer):
   class Meta:
       model = Project
       fields = ('id', 'name', 'description', 'count_of_files')


class CreateProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('name', 'description', 'date_started')
        read_only_fields = ('date_started', )

    def validate_description(self, value: str) -> str:
        if len(value) < 30:
            raise serializers.ValidationError(
                "Description must be at least 30 characters long"
            )

        return value


class AllProjectFilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectFile
        # fields = "__all__"
        exclude = ('file',)


