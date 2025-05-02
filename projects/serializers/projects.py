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


class CreateUpdateFileSerializer(serializers.ModelSerializer):
    project_id = serializers.PrimaryKeyRelatedField(
        write_only=True,
        queryset=Project.objects.all()
    )

    class Meta:
        model = ProjectFile
        fields = ["project_id"]


    def validate(self, attrs):
        file_context = self.context.get("raw_file")

        if not file_context:
            raise serializers.ValidationError("Файл обязателен")

        if not file_context.name.isascii():
            raise serializers.ValidationError("Название не соответствует параметрам ASCII")

        if not check_extension(file_context.name):
            raise serializers.ValidationError(f"Расширение файлов должно быть одним из {ALLOWED_EXTENSIONS}")

        if not check_file_size(file_context):
            raise serializers.ValidationError("Размер превышает 2 Мегабайта")

        return attrs

    def create(self, validated_data):
        proj_id = validated_data.pop("project_id")

        raw_file = self.context.get("raw_file")

        file_name = raw_file.name

        file_path = create_file_path(proj_id.name, file_name)

        os.makedirs(name=os.path.dirname(file_path), exist_ok=True)

        proj_file = ProjectFile.objects.create(
            name= file_name,
            file= file_path,
        )

        proj_file.projects.add(proj_id)

        return proj_file














