from rest_framework import serializers
from projects.models import Project


class ProjectsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id',
                  'name',
                  'date_started'
                  ]
