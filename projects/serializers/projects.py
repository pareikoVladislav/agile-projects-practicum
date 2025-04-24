from rest_framework import serializers
from projects.models import Project

class ProjectsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id',
                  'name',
                  'date_started'
                  ]


class ProjectCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['name', 'description']
        read_only_fields = ['date_started']

    def validate_description(self, value):
        if len(value) < 30:
            raise serializers.ValidationError("Описание: длина должна быть как минимум 30 символов")
        return value