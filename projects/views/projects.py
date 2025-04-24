from rest_framework.generics import  ListCreateAPIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from projects.serializers.projects import ProjectsListSerializer, ProjectCreateSerializer



from projects.models import Project


class ProjectsListAPIView(ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectsListSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ProjectsListSerializer
        return ProjectCreateSerializer




