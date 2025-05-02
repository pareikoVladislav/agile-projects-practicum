from datetime import timedelta, datetime
from lib2to3.fixes.fix_input import context

from django.template.context_processors import request
from django.utils import timezone
from rest_framework.exceptions import ValidationError
from rest_framework.generics import (
    get_object_or_404,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    ListAPIView
)
from rest_framework.permissions import SAFE_METHODS
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status

from projects.serializers.projects import (
    ProjectsListSerializer,
    CreateProjectSerializer,
    ProjectDetailSerializer,
    AllProjectFilesSerializer,
    CreateUpdateFileSerializer
)

from projects.models import Project, ProjectFile


class ProjectsListCreateAPIView(ListCreateAPIView):
    DATE_FORMAT = '%Y-%m-%d'

    def parse_date(self, date_str: str, name: str) -> timezone.datetime:
        try:
            naive = datetime.strptime(date_str, self.DATE_FORMAT)
        except ValueError:
            raise ValidationError({name: f'Неверный формат даты, ожидается YYYY-MM-DD.'})
        return timezone.make_aware(naive)

    def get_queryset(self):
        qs = Project.objects.all()
        date_from = self.request.query_params.get('date_from')
        date_to = self.request.query_params.get('date_to')

        if date_from:
            dt_from = self.parse_date(date_from, 'date_from')
            qs = qs.filter(date_started__gte=dt_from)

        if date_to:
            dt_to = self.parse_date(date_to, 'date_to')
            dt_to = dt_to + timedelta(days=1) - timedelta(microseconds=1)
        else:
            dt_to = timezone.now()

        qs = qs.filter(date_started__lte=dt_to)
        return qs

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return ProjectsListSerializer
        return CreateProjectSerializer

    def get(self, request: Request, *args, **kwargs) -> Response:
        projects = self.get_queryset()

        if not projects.exists():
            return Response(
                data=[],
                status=status.HTTP_204_NO_CONTENT
            )

        serializer = self.get_serializer(projects, many=True)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK,
        )

    def post(self, request: Request, *args, **kwargs) -> Response:
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()

            return Response(
                serializer.validated_data,
                status=status.HTTP_201_CREATED,
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )


class ProjectRetrieveUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
   def get_object(self) -> Project:
       return get_object_or_404(Project, pk=self.kwargs['pk'])

   def get_serializer_class(self):
       if self.request.method in SAFE_METHODS:
           return ProjectDetailSerializer
       return CreateProjectSerializer

   def get(self, request: Request, *args, **kwargs) -> Response:
       project = self.get_object()
       serializer = self.get_serializer(project)

       return Response(
           serializer.data,
           status=status.HTTP_200_OK,
       )

   def put(self, request: Request, *args, **kwargs) -> Response:
       project = self.get_object()

       serializer = self.get_serializer(
           instance=project,
           data=request.data,
           partial=True
       )

       if serializer.is_valid(raise_exception=True):
           serializer.save()
           return Response(
               serializer.validated_data,
               status=status.HTTP_200_OK,
           )

       return Response(
           serializer.errors,
           status=status.HTTP_400_BAD_REQUEST,
       )

   def delete(self, request: Request, *args, **kwargs) -> Response:
       project = self.get_object()
       project.delete()

       return Response(
           data={
               "message": "Project was deleted successfully"
           },
           status=status.HTTP_200_OK,
       )



class ProjectFilesListGenericView(ListCreateAPIView):
    def get_queryset(self):
        queryset = ProjectFile.objects.all()
        project_name = self.request.query_params.get("project-name")

        if project_name:
            queryset = queryset.filter(projects__name=project_name)
        return queryset

    def get_serializer_class(self, *args, **kwargs):
        if self.request.method == "GET":
            return AllProjectFilesSerializer
        return CreateUpdateFileSerializer

    def create(self, request, *args, **kwargs):
        file = request.FILES.get("file")
        serializer = self.get_serializer(data=request.data, context={"raw_file": file})
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(data={"Message": "the File successfully saved"}, status=status.HTTP_201_CREATED)
