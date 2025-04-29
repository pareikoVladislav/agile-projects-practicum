# Задачи для проекта, сотрудник с пагинацией, создание задачи
#
# В модуле serializers создайте новый файл tasks.py.
# Реализуйте сериализатор AllTasksSerializer для отображения краткой информации о задачах. Поля для отображения:
title
status
priority
project (название проекта)
assignee (email сотрудника)
due_date

from rest_framework import serializers
from projects.models import Task

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
