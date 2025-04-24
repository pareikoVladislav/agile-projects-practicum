from rest_framework.generics import  ListAPIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from projects.serializers.projects import ProjectsListSerializer

from projects.models import Project


class ProjectsListAPIView(ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectsListSerializer
